so_xau_thoa_man = 0


def thu_xay_dung_xau(xau_hien_tai):

    global so_xau_thoa_man

    if len(xau_hien_tai) == n:
        so_xau_thoa_man += 1
        return

    ky_tu_cuoi = xau_hien_tai[-1]


    if ky_tu_cuoi == 'a':
        thu_xay_dung_xau(xau_hien_tai + 'e')
    elif ky_tu_cuoi == 'e':
        thu_xay_dung_xau(xau_hien_tai + 'a')
        thu_xay_dung_xau(xau_hien_tai + 'i')
    elif ky_tu_cuoi == 'i':
        for nguyen_am in 'aeou':
            thu_xay_dung_xau(xau_hien_tai + nguyen_am)
    elif ky_tu_cuoi == 'o':
        thu_xay_dung_xau(xau_hien_tai + 'u')
        thu_xay_dung_xau(xau_hien_tai + 'i')
    elif ky_tu_cuoi == 'u':
        thu_xay_dung_xau(xau_hien_tai + 'a')


n = int(input("Nhập độ dài của xâu: "))


for nguyen_am in 'aeiou':
    thu_xay_dung_xau(nguyen_am)

print("Số lượng xâu thỏa mãn:", so_xau_thoa_man)