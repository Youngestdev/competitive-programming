if __name__ == '__main__':
    try:
        normal = []
        reversed_arr = []
        T = int(input())
        for _ in range(T):
            normal.append(str(input()))

        reversed_arr = [int(i[::-1]) for i in normal]
        for i in range(len(reversed_arr)):
            print(reversed_arr[i])
    except Exception:
        pass