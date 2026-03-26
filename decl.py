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

    local_vars: list[VarDef]
    body: Statement
    retExpr: Expression

