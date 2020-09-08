if __name__ == '__main__':
    try:
        T = int(input())
        for _ in range(T):
            N = int(input())
            values = list(map(int, input().split()))
            store = {}
            for value in values:
                if value not in store:
                    store[value] = 0
                store[value] += 1
            if 0 in values:
                print(store, len(store)-1)
            else:
                print(store, len(store))
    except Exception:
        pass