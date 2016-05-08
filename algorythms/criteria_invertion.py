class CriteriaInversion:
    @staticmethod
    def is_stochastic(data):

        inversions = 0
        index = 0
        for i in data:
            index += 1
            for j in data[index::1]:
                if i > j:
                    inversions += 1
        print('Number of inversions: ' + str(inversions))

        n = len(data)
        z2 = (inversions - n * (n - 1) / 4) * 6 / pow(n, 3/2)
        return z2 <= 1.96
