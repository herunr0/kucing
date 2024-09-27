import random

print("=================================")
print("=================================")
print ("selamat datang di game menggembul")
print("=================================")
print("=================================")



nama_user = "tata"
nama_user=input("siapakah nama kamu?")

print(f"halo selamat datang {nama_user}!!!")

nomorkucing = random.randint(1,5)
kucing = "(^v^)"
semua_kucing = [kucing] * 5
kucing_benar = semua_kucing.copy()


kucing_benar[nomorkucing - 1] = "0v0"

print(f'''selamat datang {nama_user} coba perhatikan gambar kucing dibawah ini? 
      {semua_kucing}''')

jawaban= int(input("dari kucing diatas, kucing mana yang paling gembul[1/2/3/4/5]?"))


konfirmasi = input(f"apakah kamu yakin jawabannya {jawaban} ?[y/n]")


if konfirmasi == "n":
    print("program dihentikan")
    exit
elif konfirmasi == "y":
    if jawaban == nomorkucing:
        print(f'''selamat anda benar, kegembulan ada di kucing nomor {nomorkucing}
              {kucing_benar}''')
    else :
        print(f'''yah salah, ternyata kucing yg gembul adalah kucing nomor {nomorkucing}
              {kucing_benar} sedangkan jawaban kamu adalah kucing nomor {jawaban}''')
else:
    print("silahkan ulangi")