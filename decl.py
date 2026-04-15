from dataclasses import dataclass

from exprstmt import *
from type import TType


@dataclass
class VarDef:
    type: TType
    name: str


@dataclass
class Function:
    retType: TType
    name: str
    parameters: list[VarDef]

    variables: list[tuple[VarDef, Constant]]
    body: Statement
    retExpr: Expression