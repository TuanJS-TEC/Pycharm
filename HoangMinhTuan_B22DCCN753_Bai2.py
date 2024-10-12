def tim_day_con_tang_dai_nhat(mang):

  n = len(mang)
  do_dai_day_con_tang = [1] * n
  phan_tu_truoc = [-1] * n
  cac_day_con_tang = [[] for _ in range(n)]
  do_dai_lon_nhat = 0


  for i in range(n):
    cac_day_con_tang[i] = [mang[i]]
    for j in range(i):

      if mang[j] < mang[i] and do_dai_day_con_tang[i] < do_dai_day_con_tang[j] + 1:
        do_dai_day_con_tang[i] = do_dai_day_con_tang[j] + 1
        cac_day_con_tang[i] = cac_day_con_tang[j] + [mang[i]]
    do_dai_lon_nhat = max(do_dai_lon_nhat, do_dai_day_con_tang[i])


  ket_qua = [day_con for day_con in cac_day_con_tang if len(day_con) == do_dai_lon_nhat]
  return do_dai_lon_nhat, ket_qua


def loai_bo(mang):
  do_dai_day_con_tang, cac_day_con_tang = tim_day_con_tang_dai_nhat(mang)
  k_toi_thieu = len(mang) - do_dai_day_con_tang
  return k_toi_thieu, cac_day_con_tang



N = int(input("Nhập số lượng phần tử: "))
mang = list(map(float, input("Nhập mảng, cách nhau bởi dấu phẩy: ").split(',')))


k_toi_thieu, ket_qua = loai_bo(mang)


ket_qua_chinh_sua = [[int(so) if so.is_integer() else so for so in day_con] for day_con in ket_qua]


print(f"K = {k_toi_thieu}")
for day_con in ket_qua_chinh_sua:
  print(day_con)