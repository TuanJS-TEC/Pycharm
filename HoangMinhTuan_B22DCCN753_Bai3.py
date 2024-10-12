def count_strings(N):
  """
  Đếm số lượng chuỗi có độ dài N thỏa mãn các luật cho trước.

  Args:
    N: Độ dài của chuỗi.

  Returns:
    Số lượng chuỗi thỏa mãn.
  """

  if N <= 0:
    return 0
  elif N == 1:
    return 5  # 'a', 'e', 'i', 'o', 'u'

  # Khởi tạo mảng dp để lưu trữ số lượng chuỗi kết thúc bằng mỗi nguyên âm
  dp = [[0] * 5 for _ in range(N + 1)]
  vowels = ['a', 'e', 'i', 'o', 'u']

  # Khởi tạo giá trị cho các chuỗi có độ dài 1
  for i in range(5):
    dp[1][i] = 1

  # Duyệt qua các độ dài từ 2 đến N
  for i in range(2, N + 1):
    for j in range(5):
      # Xét các luật để tính số lượng chuỗi kết thúc bằng nguyên âm vowels[j]
      if vowels[j] == 'a':
        dp[i][j] = dp[i - 1][1]  # 'e' trước 'a'
      elif vowels[j] == 'e':
        dp[i][j] = dp[i - 1][0] + dp[i - 1][2]  # 'a' hoặc 'i' trước 'e'
      elif vowels[j] == 'i':
        for k in range(5):
          if k != 2:  # Bất kỳ nguyên âm nào trừ 'i' trước 'i'
            dp[i][j] += dp[i - 1][k]
      elif vowels[j] == 'o':
        dp[i][j] = dp[i - 1][3] + dp[i - 1][2]  # 'u' hoặc 'i' trước 'o'
      elif vowels[j] == 'u':
        dp[i][j] = dp[i - 1][0]  # 'a' trước 'u'

  # Tổng số lượng chuỗi có độ dài N là tổng số lượng chuỗi kết thúc bằng mỗi nguyên âm
  total_count = sum(dp[N])
  return total_count


# Nhập độ dài chuỗi từ người dùng
N = int(input("Nhập độ dài chuỗi N: "))

# Tính và in ra kết quả
result = count_strings(N)
print(f"Số lượng chuỗi có độ dài {N} thỏa mãn luật là: {result}")