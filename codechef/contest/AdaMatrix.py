if __name__ == '__main__':
    try:
        T = int(input())
        for _ in range(T):
            matrix = []
            n = int(input())
            for _ in range(n):
                submatrix = list(map(int, input().split()))
                matrix.append(submatrix)
            number_of_ways = 0
            for i in range(n-1, 0, -1):
                print(i, matrix[i][i], matrix[i])
                if matrix[i][i] != matrix[i][i-1]+1:
                    number_of_ways += 1
                    next = i + 1
                    for j in range(next):
                        for k in range(j, next):
                            print("Value of j and k: ", j, k)
                            matrix[j][k], matrix[k][j] = matrix[k][j], matrix[j][k]
                            print(matrix)
                else:
                    continue
                print(matrix)

            print(number_of_ways)
    except Exception:
        pass