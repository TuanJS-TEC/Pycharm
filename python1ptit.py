def is_prime(num):
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

N, M = map(int, input().split())

matrix = []
for _ in range(N):
  row = list(map(int, input().split()))
  matrix.append(row)

for i in range(N):
  for j in range(M):
    if is_prime(matrix[i][j]):
      matrix[i][j] = 1
    else:
      matrix[i][j] = 0

for row in matrix:
  print(*row)