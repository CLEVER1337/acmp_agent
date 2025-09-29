
A, B, K = map(int, input().split())
result = str(A * (10 ** K) // B % 10)
print(result)
