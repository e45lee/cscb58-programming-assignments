class TypeCheckError(Exception):
    def __init__(self, message: str, offending_node = None):
        self.offending_node = offending_node
        super().__init__(message)


class FunctionNotDefinedError(TypeCheckError):
    """Raised when trying to call a function that is not defined (i.e. not in the f table)"""
    pass


class ArgumentCountMismatchError(TypeCheckError):
    """Raised call to a function has different number of arguments than the definition"""
    pass


class ArgumentTypeMismatchError(TypeCheckError):
    """Raised when an argument in a function call has a different type than the corresponding parameter in the function definition"""
    pass


class VariableNotDefinedError(TypeCheckError):
    """Raised when trying to access a variable that is not defined in the current function"""
    pass


class AssignmentTypeMismatchError(TypeCheckError):
    """Raised when trying to assign an expression to a variable and the expression's type is different than the variable's type"""
    pass


class ExpressionTypeMismatchError(TypeCheckError):
    """Raised when an expression has subexpressions with incompatible types (e.g. adding an int and a pointer)"""
    pass


class ConditionalTypeError(TypeCheckError):
    """Raised when the condition expression in an if or while statement does not have int type"""
    pass