import time

from datetime import datetime
from typing import Literal, Union
from dataclasses import dataclass, field


@dataclass
class Metric:
    name: str = None
    value: Union[int, float] = None
    type: Literal["trip", "service", "other"] = None
    timestamp: float = field(default_factory=lambda: time.time())

    def __repr__(self):
        return (f"The metric '{self.name}' with type '{self.type}' and "
                f"value '{self.value}' has been created at '{datetime.fromtimestamp(self.timestamp)}'")
