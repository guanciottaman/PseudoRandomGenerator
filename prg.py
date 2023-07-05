import os
import random
from time import perf_counter, perf_counter_ns
from typing import Any

import psutil


class PseudoRandomGenerator:
    def _get_variables(self) -> dict:
        return {'pfc': perf_counter(),
                'pfcns': perf_counter_ns(),
                'boot_time': psutil.boot_time(),
                'cpu_usage': ((psutil.getloadavg()[2])/os.cpu_count()) * 100,
                'ram_used': psutil.virtual_memory()[3]/1000000000,
                'psran_pid': random.choice(psutil.pids())}

    def _gen_rnum(self) -> float:
        d = self._get_variables()
        pfc, pfcns, boot_time, cpu_usage, ram_used, psran_pid = d['pfc'], d['pfcns'],\
            d['boot_time'], d['cpu_usage'], d['ram_used'], d['psran_pid']
        return ((pfcns - pfc) * 100) / (boot_time / 1000) - (cpu_usage / ram_used / (psran_pid + 5))

    def randint(self, min_:int=0, max_:int=10) -> int:
        if max_ <= min_:
            max_ += 10 ** len(str(min_)) - 10 ** 2
        rnum = self._gen_rnum()
        range_size = max_ - min_ + 1
        mapped = int((rnum % range_size) + min_)
        return mapped

    def randfloat(self, min_:float=0.0, max_:float=10.0) -> float:
        if max_ <= min_:
            max_ += 10 ** len(str(min_)) - 10 ** 2
        rnum = self._gen_rnum()
        range_size = max_ - min_
        mapped = (rnum % range_size) + min_
        return mapped

    def choices(self, lst:list, count:int=1) -> list | Any:
        values = []
        if count == 1:
            return lst[self.randint(0, len(lst) - 1)]
        for i in range(count):
            values.append(lst[self.randint(0, len(lst) - 1)])
        return values

    def shuffle(self, lst:list) -> list:
        for i in reversed(range(len(lst) - 1)):
            j = self.randint(0, len(lst) - 1)
            lst[i], lst[j] = lst[j], lst[i]
        return lst

    def random(self) -> float:
        return self.randfloat(0.0, 1.0)


prg = PseudoRandomGenerator()
