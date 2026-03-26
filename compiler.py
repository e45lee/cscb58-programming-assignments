import argparse
import importlib
import importlib.util
import sys

from decl import *
from type import *
from codetypes import *
from exprstmt import *
from typecheck_errors import *
from labelasm import assembleCode


type ExpressionTypes = dict[Expression|LValue, TType]
type SymbolTable = dict[str, FunctionInformation]


@dataclass
class FunctionInformation:
    paramTypes: list[TType]
    returnType: TType
    varTable: dict[str, TType]


def typecheckNode(node, f_table: SymbolTable, f_current: FunctionInformation) -> ExpressionTypes:
    # You may modify this function and its input arguments as you'd like.

    # TODO: Implement typechecking for each node type and add the types of expressions to expr_types
    # The minimum required cases for the first checkpoint have been added for you
    expr_types: ExpressionTypes = {}
    match node:
        case Function():
            # TODO: call typecheckNode on all parameters, local vars, the body, and the return expression
            pass
        case VarDef():
            # TODO: add variable definition to the current function's variable table
            pass
        case Block():
            # TODO: typcheck all contained statements/expressions
            pass
        case Call():
            # TODO: call typecheckNode on all arguments
            # TODO: Check:
            #       - called function is in f_table
            #       - called function has same number of args as it's definition
            #       - all arguments have the same type as the function definition
            # and raise the relevant exception if one of the checks dont pass (see typecheck_errors.py)
            pass
    # Add more cases for remaining node types...
    return expr_types


def generateNode(node, expr_types: ExpressionTypes, f_table: SymbolTable, f_current: FunctionInformation) -> list[LabeledAssemblyCode]:
    # You may modify this function and its input arguments as you'd like.

    # TODO: Implement assembly code generation for each node type and add the generated instructions to assembly_code
    # The minimum required cases for the first checkpoint have been added for you
    assembly_code: list[LabeledAssemblyCode] = []
    match node:
        case Function():
            pass
        case VarDef():
            pass
        case Constant():
            pass
        case VarAccess():
            pass
    # Add more cases for each node type...
    return assembly_code


def typecheck(input_fs: list[Function]) -> tuple[ExpressionTypes, SymbolTable]:
    '''Checks type constraints on an input program input_fs, which consists of a list of Function objects.

    Args:
        input_fs: list of Function objects representing the input program
    
    Returns:
        A tuple (expr_types, f_table) where:
            expr_types: a mapping from each expression and lvalue in the program to its type
            f_table: a mapping from each function name to its parameter types, return type, and variable table

    Raises:
        TypeCheckError
     
    Note:
        Do not modify the input arguments to typecheck. You may modify the body as needed.
    '''
    expr_types: ExpressionTypes = {}
    f_table: SymbolTable = {}

    # Initialize function table
    for function in input_fs:
        paramTypes: list[TType] = []        # TODO: Initialize paramTypes
        returnType: TType = TType.Int       # TODO: Initialize returnType
        f_table[function.name] = FunctionInformation(paramTypes, returnType, {})
    
    # TODO: add the 5 builtin functions to the f_table
    
    # Run typechecking on each function and add returned types to expr_types
    for function in input_fs:
        expr_types = expr_types | typecheckNode(function, f_table, f_table[function.name])

    return (expr_types, f_table)


def generate(input_fs: list[Function], expr_types: ExpressionTypes, f_table: SymbolTable) -> list[list[LabeledAssemblyCode]]:
    '''Generates assembly code for an input program input_fs, which consists of a list of Function objects.
    
    Args:
        input_fs: list of Function objects representing the input program
        expr_types: a mapping from each expression and lvalue in the program to its type
        f_table: a mapping from each function name to its parameter types, return type, and variable table

    Returns:
        A list of lists of LabeledAssemblyCode, one list for each function in the input program, containing the generated assembly code for that function

    Note:
        Do not modify the input arguments to generate. You may modify the body as you'd like, but its not reccomended.
    '''
    assembly_code: list[list[LabeledAssemblyCode]] = []

    # Generate each function's labeled assembly code
    for function in input_fs:
        asm_code = generateNode(function, expr_types, f_table, f_table[function.name])
        assembly_code.append(asm_code)

    return assembly_code


def compileCode(input_fs: list[Function], output = sys.stdout.buffer):
    try:
        expr_types, f_table = typecheck(input_fs)
        asm_fns = generate(input_fs, expr_types, f_table)
        concatAsm = [elem for sublist in asm_fns for elem in sublist]
        assembleCode(concatAsm, output)
    except TypeCheckError as tc_err:
        print(f"TypeCheck error raised: {tc_err}")

if __name__ == "__main__":
    if sys.platform == "win32":
        import os, msvcrt
        msvcrt.setmode(sys.stdout.fileno(  ), os.O_BINARY)

    parser = argparse.ArgumentParser(
                    prog="compiler",
                    description="Assembles a sequence of Function objects")
    parser.add_argument("filename")
    args = parser.parse_args()
    
    spec = importlib.util.spec_from_file_location("code", args.filename)
    assert(not spec is None and not spec.loader is None)
    code = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(code)
    compileCode(code.FUNCS) 
