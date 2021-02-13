# 1이 될 떄까지

n, k = map(int, input().split())
result = 0
while True:
    if n % k == 0:
        n //= k
        result += 1
    else:
        # 앞 전에는 일일이 한개씩 빼서 k가 커지면 속도가 느려짐 #
        n, count = divmod(n,k)
        result += count

    if n == 1:
        break

print(result)

