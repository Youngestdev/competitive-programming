if __name__ == '__main__':
    try:
        number_of_test_cases = int(input())
        for _ in range(number_of_test_cases):
            length = int(input())
            answer = set(map(int, input().split()))
            # answer = set(numbers)
            if 0 in answer:
                print(len(answer)-1)
            else:
                print(len(answer))
    except Exception:
        pass