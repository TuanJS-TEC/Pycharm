def tim_hinh_vuong_va_chu_nhat_lon_nhat(ma_tran):
  dien_tich_hinh_vuong_lon_nhat = -1
  dien_tich_hinh_chu_nhat_lon_nhat = -1
  cac_hinh_vuong = []
  cac_hinh_chu_nhat = []

  so_dong = len(ma_tran)
  so_cot = len(ma_tran[0])

  # Tiền xử lý ma trận để tính chiều cao của các cột '1' liên tiếp
  for j in range(so_cot):
    for i in range(1, so_dong):
      if ma_tran[i - 1][j] != 0 and ma_tran[i][j] == 1:
        ma_tran[i][j] = ma_tran[i - 1][j] + 1

  def tinh_dien_tich(dong, chieu_cao):
    """
    Tính toán diện tích của hình chữ nhật lớn nhất kết thúc tại mỗi cột trong một hàng.
    """
    nonlocal dien_tich_hinh_vuong_lon_nhat, dien_tich_hinh_chu_nhat_lon_nhat, cac_hinh_vuong, cac_hinh_chu_nhat
    ngan_xep = []
    n = len(chieu_cao)
    i = 0
    while i < n:
      if not ngan_xep or chieu_cao[i] > chieu_cao[ngan_xep[-1]]:
        ngan_xep.append(i)
        i += 1
      else:
        chi_so = ngan_xep.pop()
        chieu_cao_hien_tai = chieu_cao[chi_so]
        chieu_rong = i if not ngan_xep else i - ngan_xep[-1] - 1
        dien_tich = chieu_cao_hien_tai * chieu_rong

        # Cập nhật hình vuông lớn nhất
        if chieu_cao_hien_tai <= chieu_rong:
          dien_tich_hinh_vuong = chieu_cao_hien_tai * chieu_cao_hien_tai
          if dien_tich_hinh_vuong > dien_tich_hinh_vuong_lon_nhat:
            dien_tich_hinh_vuong_lon_nhat = dien_tich_hinh_vuong
            cac_hinh_vuong = [((dong - chieu_cao_hien_tai + 1, chi_so - chieu_cao_hien_tai + 1), (dong, chi_so))]
          elif dien_tich_hinh_vuong == dien_tich_hinh_vuong_lon_nhat:
            cac_hinh_vuong.append(((dong - chieu_cao_hien_tai + 1, chi_so - chieu_cao_hien_tai + 1), (dong, chi_so)))

        # Cập nhật hình chữ nhật lớn nhất
        if dien_tich > dien_tich_hinh_chu_nhat_lon_nhat:
          dien_tich_hinh_chu_nhat_lon_nhat = dien_tich
          cac_hinh_chu_nhat = [((dong - chieu_cao_hien_tai + 1, chi_so - chieu_rong + 1), (dong, chi_so))]
        elif dien_tich == dien_tich_hinh_chu_nhat_lon_nhat:
          cac_hinh_chu_nhat.append(((dong - chieu_cao_hien_tai + 1, chi_so - chieu_rong + 1), (dong, chi_so)))

    while ngan_xep:
      chi_so = ngan_xep.pop()
      chieu_cao_hien_tai = chieu_cao[chi_so]
      chieu_rong = i if not ngan_xep else i - ngan_xep[-1] - 1
      dien_tich = chieu_cao_hien_tai * chieu_rong

      # Cập nhật hình vuông lớn nhất
      if chieu_cao_hien_tai <= chieu_rong:
        dien_tich_hinh_vuong = chieu_cao_hien_tai * chieu_cao_hien_tai
        if dien_tich_hinh_vuong > dien_tich_hinh_vuong_lon_nhat:
          dien_tich_hinh_vuong_lon_nhat = dien_tich_hinh_vuong
          cac_hinh_vuong = [((dong - chieu_cao_hien_tai + 1, chi_so - chieu_cao_hien_tai + 1), (dong, chi_so))]
        elif dien_tich_hinh_vuong == dien_tich_hinh_vuong_lon_nhat:
          cac_hinh_vuong.append(((dong - chieu_cao_hien_tai + 1, chi_so - chieu_cao_hien_tai + 1), (dong, chi_so)))

      # Cập nhật hình chữ nhật lớn nhất
      if dien_tich > dien_tich_hinh_chu_nhat_lon_nhat:
        dien_tich_hinh_chu_nhat_lon_nhat = dien_tich
        cac_hinh_chu_nhat = [((dong - chieu_cao_hien_tai + 1, chi_so - chieu_rong + 1), (dong, chi_so))]
      elif dien_tich == dien_tich_hinh_chu_nhat_lon_nhat:
        cac_hinh_chu_nhat.append(((dong - chieu_cao_hien_tai + 1, chi_so - chieu_rong + 1), (dong, chi_so)))

  # Xử lý từng hàng của ma trận
  for i, dong in enumerate(ma_tran):
    tinh_dien_tich(i, dong)

  return dien_tich_hinh_vuong_lon_nhat, cac_hinh_vuong, dien_tich_hinh_chu_nhat_lon_nhat, cac_hinh_chu_nhat


# Nhập ma trận từ người dùng
ma_tran = []
while True:
  try:
    ma_tran.append(list(map(int, input().split())))
  except EOFError:
    break  # Nhập ^D (Ctrl + D) để dừng input

# Tìm hình vuông và hình chữ nhật lớn nhất
dien_tich_hinh_vuong_lon_nhat, cac_hinh_vuong, dien_tich_hinh_chu_nhat_lon_nhat, cac_hinh_chu_nhat = tim_hinh_vuong_va_chu_nhat_lon_nhat(ma_tran)

# In kết quả
print("Output 1 =", dien_tich_hinh_vuong_lon_nhat)
for top_left, bot_right in cac_hinh_vuong:
  print(f"[{top_left[1] + 1}, {top_left[0] + 1}], [{bot_right[1] + 1}, {bot_right[0] + 1}]")

print("Output 2 =", dien_tich_hinh_chu_nhat_lon_nhat)
for top_left, bot_right in cac_hinh_chu_nhat:
  print(f"[{top_left[1] + 1}, {top_left[0] + 1}], [{bot_right[1] + 1}, {bot_right[0] + 1}]")