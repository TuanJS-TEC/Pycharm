def is_prime(n):

  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def phi(n):
  #   Euler's Totient function
  result = n
  i = 2
  while i * i <= n:
    if n % i == 0:
      while n % i == 0:
        n //= i
      result -= result // i
    i += 1
  if n > 1:
    result -= result // n
  return result


T = int(input())

for _ in range(T):
  N = int(input())
  k = phi(N)  #
  if is_prime(k):
    print("YES")
  else:
    print("NO")