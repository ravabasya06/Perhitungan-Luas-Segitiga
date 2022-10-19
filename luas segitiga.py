def ulang():
    
    alas = float(input("Masukkan alas segitiga : "))
    tinggi = float(input("Masukkan tinggi segitiga : "))
    
    print("Luas : "+str(float(1/2*alas*tinggi)))
    
    pengulangan = input("Lakukan perhitungan lagi? ya / tidak : ")
    if pengulangan == "ya":
        ulang()
    elif pengulangan == "tidak":
        print("Ok")
    else:
        print("Saya tidak mengerti perintah anda, saya akan menganggap anda menjawab tidak.")
ulang()
