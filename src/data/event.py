from datetime import datetime
from typing import Literal, Union
from dataclasses import dataclass


@dataclass
class Event:
    id: int = None
    name: str = None
    timestamp: float = None
    value: Union[int, float] = None
    agg_func: Literal["sum", "avg", "min", "max"] = None
    type: Literal["sale", "registration", "departure", "arrival", "system", "delay", "feedback"] = None

    def __repr__(self):
        return (f"The event № '{self.id}' - '{self.name}' with type '{self.type}' and "
                f"value '{self.value}' happened at '{datetime.fromtimestamp(self.timestamp)}'")
