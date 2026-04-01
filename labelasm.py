
#!/usr/bin/python3
import sys
from codetypes import *
from wordasm import *

def eliminateLabels(code: list[LabeledAssemblyCode | AssemblyCode]) -> tuple[list[AssemblyCode], dict[str, int]]:
    """ Lowers away LabeledAssemblyCode instructions. Returns a tuple of AssemblyCode and
        a dictionary mapping label definitions to addresses."""
    return (code, {})

def assembleCode(code: list[LabeledAssemblyCode | AssemblyCode], out = sys.stdout.buffer):
    """ Assembles a List of LabeledAssemblyCode objects to the target file. """
    newCode, labels = eliminateLabels(code)
    for label in labels:
        print("label {0} => {1}".format(label, labels[label]), file=sys.stderr)

    assembleWords(lowerAssemblyCode(newCode), out)

if __name__ == "__main__":
    if sys.platform == "win32":
        import os, msvcrt
        msvcrt.setmode(sys.stdout.fileno(  ), os.O_BINARY)

    parser = argparse.ArgumentParser(
                    prog="labelasm",
                    description="Assembles a sequence of LabeledAssemblyCode objects")
    parser.add_argument("filename")
    args = parser.parse_args()
    
    spec = importlib.util.spec_from_file_location("code", args.filename)
    code = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(code)
    assembleCode(code.CODE) 
