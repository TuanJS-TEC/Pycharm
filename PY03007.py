import re

toan_bo_van_ban = ""


while True:
    try:
        dong_moi = input()
        toan_bo_van_ban += dong_moi
    except EOFError:
        break


cac_cau = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|!)\s', toan_bo_van_ban)

for cau in cac_cau:
    if len(cau) == 0:
        continue

    cac_tu = cau.lower().split()

    cac_tu[0] = cac_tu[0][0].upper() + cac_tu[0][1:]

    cau_da_xu_ly = " ".join(cac_tu)
    print(cau_da_xu_ly)
