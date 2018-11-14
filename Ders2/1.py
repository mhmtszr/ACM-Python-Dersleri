"""
a=5
b=3
if(a>b):
    print("a bden büyüktür")
"""
"""
 \n -->alt satıra inmemizi sağlar
"""
"""
print("ACM\nHacettepe")
"""
"""
a=3**(2+1)
print(a)
"""
"""
    while-->-ken döngüsü
"""
"""
i=0
a="ACM"
while(i<5):     
    print(a)
    i=i+1
"""
"""
a=[1,2,3,4,5]
b="ACMHACETTEPE"
print(a[0])
print(b[1])
"""
"""
a="ACMHACETTEPE"
print(a[2:5])
"""
"""
a=[1,2,3,4,5]
print(a[::2])
"""

"""
    break -->beni gördüğünde döngüyü bitir
    continue -->beni gördüğünde döngüyü başa al
    
"""
"""
i=0
while(i<5):
    if(i==3):
        i=i+1
        break
    i=i+1
    print(i)
"""
"""
kullaniciadi="acmhacettepe"
sifre="12345"
while(True):
    print("Instagram'a hoşgeldiniz")
    a=input("Kullanici adinizi giriniz:")
    b=input("Şifrenizi giriniz")
    if(a==kullaniciadi and sifre==b):
        print("hoşgeldiniz "+kullaniciadi)
        break
    else:
        print("yanlış giriş yaptınız")
        continue
"""
"""
bakiyem=200
while(True):
    print("Bankamıza hoşgeldiniz")
    print("İşlemler:\n1:Para çekme\n2:Para yatırma\n3:Çıkış")
    islem=int(input("Lütfen bir işlem seçiniz:"))
    if(islem==1):
        paramiktarı=int(input("Ne kadar para çekmek istiyorsunuz:"))
        bakiyem=bakiyem-paramiktarı
        print("Güncel bakiyeniz "+str(bakiyem))
        continue
    elif(islem==2):
        yatırılanpara=int(input("Ne kadar para yatırmak istiyorsunuz:"))
        bakiyem=bakiyem+yatırılanpara
        print("Güncel bakiyeniz "+str(bakiyem))
        continue
    elif(islem==3):
        print("Görüşmek üzere")
        break
"""
"""
a="ACM"
print(len(a))
"""
"""
a=[1,2,3,4,5,6]
print(a[len(a)-1])
print(a[-1])
"""
"""
a="ACM"
for ahmet in a:
    print(ahmet)
"""
"""
liste=[5,1,2,3,-1]
for i in liste:
    print(i)
"""
"""
    range -->array üretici
"""
"""
print(*range(0,10))
for i in range(0,10):
    print(i)
"""
"""
for i in range(0,10):
    print(i*"ACM")
"""
