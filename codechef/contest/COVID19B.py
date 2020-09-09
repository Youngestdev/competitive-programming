if __name__ == '__main__':
    try:
        T = int(input())
        for _ in range(T):
            n = int(input())
            athletes = [int(i) for i in input().split()]
            result = [0 for _ in range(n)]

            for i in range(n):
                x, y = 0, 0
                for j in range(i, -1, -1):
                    if athletes[j] > athletes[i]:
                        x += 1
                for k in range(i, n):
                    if athletes[k] < athletes[i]:
                        y += 1
                result[i] = x + y

            _min = result[0]
            _max = result[0]

            for l in range(n):
                if result[l] < _min:
                    _min = result[l]
                if result[l] > _max:
                    _max = result[l]
            _min += 1
            _max += 1
            print(_min, " ", _max)

    except Exception:
        pass