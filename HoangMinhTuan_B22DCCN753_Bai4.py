import matplotlib.pyplot as plt


def tan_suat_tu(van_ban):

  cac_tu = van_ban.lower().split()


  tan_suat = {}
  for tu in cac_tu:
    tan_suat[tu] = tan_suat.get(tu, 0) + 1


  tu_sap_xep = sorted(tan_suat.items(), key=lambda item: item[1], reverse=True)
  return tan_suat, tu_sap_xep


def ve_bieu_do(tu_sap_xep):

  top_tu = dict(tu_sap_xep[:10])


  plt.bar(top_tu.keys(), top_tu.values())
  plt.title("10 từ xuất hiện nhiều nhất")
  plt.xlabel("Từ")
  plt.ylabel("Tần suất")
  plt.show()



van_ban = input("Nhập một đoạn văn bản: ")


tan_suat, tu_sap_xep = tan_suat_tu(van_ban)


ve_bieu_do(tu_sap_xep)
