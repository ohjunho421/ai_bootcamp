str, n = input().strip().split(' ')
n = int(n)

if 1 <= len(str) <= 10 and 1 <= n <= 5:
    result = str * n
    print(result)
else:
    print("조건을 만족하지 않습니다.")
