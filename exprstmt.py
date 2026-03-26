from enum import Enum
from dataclasses import dataclass


class UnaryOp(Enum):
    Not = 0
    Negate = 1
    Address = 2


class BinaryOp(Enum):
    Plus = 1
    Minus = 2
    Subtract = 3
    Divide = 4
    Ge = 5
    Le = 6
    Lt = 7
    Eq = 8
    Ne = 9


@dataclass
class Statement:
    pass


@dataclass
class Expression(Statement):
    pass


@dataclass(eq=False)
class LValue:
    pass


@dataclass(eq=False)
class VarTarget(LValue):
    name: str


@dataclass(eq=False)
class DerefTarget(LValue):
    address: Expression


@dataclass(eq=False)
class NULL:
    pass


# Expressions
@dataclass(eq=False)
class BinExp(Expression):
    left: Expression
    op: BinaryOp
    right: Expression


@dataclass(eq=False)
class UnExp(Expression):
    op: UnaryOp
    exp: Expression


@dataclass(eq=False)
class Call(Expression):
    target: str
    arguments: list[Expression]


@dataclass(eq=False)
class VarAccess(Expression):
    target: str


@dataclass(eq=False)
class Constant(Expression):
    value: int | NULL


# Statements
@dataclass
class Block(Statement):
    body: list[Statement|Expression]


@dataclass
class WhileLoop(Statement):
    test: Expression
    body: Statement


@dataclass
class Assign(Statement):
    left: LValue
    right: Expression


@dataclass
class If(Statement):
    test: Expression
    trueCase: Statement
    falseCase: Statement

