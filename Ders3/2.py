türkcekarakter="şÇİÜĞğıÖö"
parola=input("Parolanızı giriniz:")
sayi=0
for harf in parola:
    if harf in türkcekarakter:
        sayi+=1 #sayi=sayi+1
        continue
print("Şifrenizde",sayi,"kadar türkçe karakter var")