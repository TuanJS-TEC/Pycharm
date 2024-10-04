# Input: Nhập chuỗi số thập phân hoặc số kèm chữ
input_string = input()

# Bước 1: Tìm vị trí phần chữ (nếu có)
i = 0
while i < len(input_string) and (input_string[i].isdigit() or input_string[i] == '.'):
    i += 1

# Chia chuỗi thành phần số và phần chữ
number_part = input_string[:i]
text_part = input_string[i:]

# Bước 2: Tìm phần nguyên và phần thập phân
if '.' in number_part:
    integer_part, decimal_part = number_part.split('.')
else:
    integer_part, decimal_part = number_part, ''

# Bước 3: Định dạng phần nguyên với dấu phẩy
formatted_integer = f"{int(integer_part):,}"

# Bước 4: Ghép lại các phần
if decimal_part:
    result = formatted_integer + '.' + decimal_part
else:
    result = formatted_integer

result += text_part

# Output: In ra kết quả
print(result)
