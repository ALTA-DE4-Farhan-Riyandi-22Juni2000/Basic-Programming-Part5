def muncul_sekali(angka):
  unik = []
  for karakter in angka:
    if angka.count(karakter) == 1:
      unik.append(karakter)

  unik = list(map(int, unik))
  return unik

if __name__ == '__main__':
    print(muncul_sekali("1234123")) # [4]
    print(muncul_sekali("76523752")) # [6, 3]
    print(muncul_sekali("12345")) # [1, 2, 3, 4, 5]
    print(muncul_sekali("1122334455")) # []
    print(muncul_sekali("0872504")) # [8, 7, 2, 5, 4]