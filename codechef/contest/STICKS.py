def answer(array):
    print(array)
    n = len(array)
    H = max(array) - 1
    i, count = 0, 0

    if all(values == array[0] for values in array):
        return 1

    while i < n:
        if array[i] - H <= 0:
            array.pop(i)
            n -= 1
        else:
            array[i] = array[i] - H
            i += 1
        count += 1
    if all(values == array[0] for values in array):
        return count
    return 0

    # return array

if __name__ == '__main__':
    try:
        values = []
        T = int(input())
        for _ in range(T):
            N = int(input())
            values.append(list(map(int, input().split())))
        for value in values:
            print(answer(value))
    except Exception:
        pass