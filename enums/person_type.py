# -*- coding: utf-8 -*-
"""
    This is a Simple enum interface that enumerates person types form de SGB.
"""
from enum import Enum


class PersonType(Enum):
    """
        The status are:
            EMP=Employee, VIS= Visitor, BEN= Beneficiary
    """
    EMP = 0
    VIS = 1
    BEN = 2

