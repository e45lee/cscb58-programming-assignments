from dataclasses import dataclass

from exprstmt import *
from type import TType

@dataclass
class VarDef:
    type: TType
    name: str

@dataclass
class Function:
    name: str
    parameters: list[VarDef]
    variables: list[tuple[VarDef, Constant]]
    retType: TType

    body: Statement
    retExpr: Expression

