import math


class PhaseFrequencyCriteria:
    @staticmethod
    def is_stochastic(data):
        delta = []
        for a, b in zip(data[0::2], data[1::2]):
            delta.append(b - a)
        #print(delta)

        phases = int()
        old_sign = delta[0] > 0
        for a in delta:
            new_sign = a>0
            if a == 0:
                pass
            elif not (new_sign == old_sign):
                phases += 1
                old_sign = a > 0
        #print(phases)

        n = len(data)
        _ = 0
        if n < 30:
            _ = 0.5
        z1 = (abs(phases - (2 * len(data) - 7) / 3) - _) / math.sqrt((16 * n - 29) / 90)

        return z1 <= 1.96
