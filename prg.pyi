import os
import random
from time import perf_counter, perf_counter_ns
from typing import Any

import psutil

class PseudoRandomGenerator:
    def _get_variables(self) -> dict: ...
    """Get system variables that change over time (Don't use this)"""

    def _gen_rnum(self) -> float: ...
    """Generate random number from variables (Don't use this)"""

    def randint(self, min_:int=0, max_:int=10) -> int: ...
    """Generate random integer"""

    def randflaot(self, min_:float=0.0, max_:float=10) -> float: ...
    """Generate random floating point number"""

    def choices(self, lst:list, count:int=1) -> list | Any: ...
    """Choose random item(s) from given list"""

    def shuffle(self, lst:list) -> list: ...
    """Shuffle items from given list"""

    def random(self) -> float: ...
    """Generate random number from 0 to 1"""


