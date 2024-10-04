input_string=input()

i =0
while i < len(input_string) and (input_string[i] == input_string[i].isdigit()) or input_string[i]=='.':
    i +=1

number_part = input_string[:i]
text_part = input_string[i:]

if '.' in number_part:
    integer_part,decimal_part = number_part.split('.')
else:
    integer_part,decimal_part = number_part,''

format_integer = f"{int(integer_part):,}"

if decimal_part:
    result = format_integer+'.'+decimal_part
else:
    result = format_integer

result += text_part

print(result)
