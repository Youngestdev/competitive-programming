if __name__ == '__main__':
    try:
        words = []
        T = int(input())
        for i in range(T):
            words.append(str(input()))

        def idk(words):
            result = []
            for i in range(len(words)):
                word = words[i]
                if len(word) % 2 == 0:
                    mid = len(word) // 2
                    if sorted(word[:mid]) == sorted(word[mid:]):
                        result.append("YES")
                    else:
                        result.append("NO")
                if len(word) % 2 == 1:
                    mid = len(word) // 2
                    if sorted(word[:mid - 1] == sorted(word[mid + 1:])):
                        result.append('YES')
                    else:
                        result.append("NO")
            return result
        print(idk(words))
    except Exception:
        pass