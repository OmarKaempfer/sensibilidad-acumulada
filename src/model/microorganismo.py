import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class Microorganismo:
    resistant_to: List[str]
    last_register: datetime.datetime = None
    frequency: int = 0
