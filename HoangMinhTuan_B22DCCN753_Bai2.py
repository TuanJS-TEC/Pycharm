def LIQ(arr):
    n = len(arr)
    dp = [1] * n
    prev = [-1] * n
    a = [[] for _ in range(n)]
    max_length = 0

    # đây là đoạn truy vết
    for i in range(n):
        a[i] = [arr[i]]
        for j in range(i):
            if arr[j] < arr[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                a[i] = a[j] + [arr[i]]
        max_length = max(max_length, dp[i])

    result = [sub for sub in a if len(sub) == max_length]
    return max_length, result


def remove(arr):
    length_of_lis, lis_sequences = LIQ(arr)
    min_k = len(arr) - length_of_lis
    return min_k, lis_sequences


N = int(input())
arr = list(map(float, input().split(',')))

min_k, result = remove(arr)

res = [[int(num) if num.is_integer() else num for num in seq] for seq in result]

print(f"K = {min_k}")
for seq in res:
    print(seq)