import re

toan_bo_van_ban = ""

while True:
    try:
        dong_moi = input()
        toan_bo_van_ban += dong_moi
    except EOFError:
        break


cac_cau = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|!|,|;|:|-|\))(\s+)', toan_bo_van_ban)

for i in range(0, len(cac_cau), 2):
    cau = cac_cau[i]
    if len(cau) == 0:
        continue

    cac_tu = cau.split()
    if len(cac_tu) == 0:
        continue
x
    if cac_tu[0][0].isalpha():
        cac_tu[0] = cac_tu[0][0].upper() + cac_tu[0][1:]

    cau_da_xu_ly = " ".join(cac_tu)


    if i + 1 < len(cac_cau):
        cau_da_xu_ly += cac_cau[i + 1]

    print(cau_da_xu_ly)