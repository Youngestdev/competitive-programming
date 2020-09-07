if __name__ == '__main__':
    try:
        values = [int(i) for i in input().strip().split()]
        for v in range(len(values)):
            if values[v] == 42:
                break
            print(values[v])
    except Exception:
        pass