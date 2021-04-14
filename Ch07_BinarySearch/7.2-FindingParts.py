# 7.2 부품 찾기
import sys

n = int(sys.stdin.readline().rstrip())
my_parts = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
order_parts = list(map(int, sys.stdin.readline().rstrip().split()))

my_parts.sort()

result = ["no"] * len(order_parts)
for order_part_idx, order_part in enumerate(order_parts):
    start = 0
    end = len(my_parts) - 1
    while start <= end:
        mid = (start + end) // 2
        if order_part < my_parts[mid]:
            end = mid - 1
        elif order_part > my_parts[mid]:
            start = mid + 1
        elif order_part == my_parts[mid]:
            result[order_part_idx] = "yes"
            break

print(" ".join(result))
