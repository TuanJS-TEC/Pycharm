def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

while True:
    try:

        N, M = map(int, input("Nhap N M: ").split())


        if N <= 0 or M <= 0:
            print("So Khong Hop Le")
            continue

        matrix = []
        for _ in range(N):
            row = list(map(int, input().split()))

            for value in row:
                if value < -10**18 or value > 10**18:
                    raise ValueError("Tran So")
            matrix.append(row)

        for i in range(N):
            for j in range(M):
                if is_prime(matrix[i][j]):
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = 0


        for row in matrix:
            print(*row)


        break

    except ValueError as e:
        if str(e) == "Tran So":
            print("Tran So")
        else:
            print("So Khong Hop Le")
