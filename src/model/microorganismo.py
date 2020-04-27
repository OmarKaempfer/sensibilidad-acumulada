import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class Microorganismo:
    resistant_to: List[str]
    last_register: datetime.datetime = None
    frequency: int = 0

    last_fenotype: tuple = None
    dtr_frequency: int = 0
    cr_frequency: int = 0
    ecr_frequency: int = 0
    fqr_frequency: int = 0

    last_nhc: str = None
