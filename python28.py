def insert_commas(N):

  s = str(N)[::-1]


  result = ""
  for i, char in enumerate(s):
      if i % 3 == 0 and i != 0:
          result += ","
      result += char


  return result[::-1]


try:
    N = int(input().replace('.', ''))
except EOFError:
    N = 123456789


result = insert_commas(N)
print(result)