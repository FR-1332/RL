from typing import Any

from pydantic import BaseModel
from pydantic.dataclasses import dataclass


@dataclass
class Record(BaseModel):
    """
    Basic form of the RL data.
    """
    observation: Any
    action: int
    reward: float
