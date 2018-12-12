"""
sayi=int(input("Bir sayi giriniz:"))
cevap=0
for i in range(1,sayi):
    if(sayi%i==0):
        cevap+=i
if(cevap==sayi):
    print(sayi,"bir mükemmel sayidir")  
else:
    print(sayi,"bir mükemmel sayi degildir.")      
"""
"""
a=input("bir sayi giriniz:")
basamaksayim=len(a)
a=int(a)
sayi=a
cevap=0
while(sayi>0):
    i=sayi%10  #4
    cevap+=i**basamaksayim
    sayi=sayi//10
if(cevap==a):
    print(a,"bir armstrong sayısıdır")
else:
    print(a,"bir armstrong sayısı değildir.")
"""
"""
EBOB
"""
"""
a=int(input("Sayi1:")) #4
b=int(input("Sayi2:")) #6
c=a
d=b

ebob=1
i=2
while(c>=i or d>=i): 
    if(c%i==0 and d%i==0):
        c=c//i
        d=d//i
        ebob*=i
    else:
        i+=1
print(ebob)
ekok=(a*b)/ebob
print(int(ekok))
"""
"""
a=["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
b=["","bir","iki","üç","dört","beş","altı","yedi","sekis","dokuz"]

sayi=int(input("bir sayi giriniz:"))
birlerbasamagi=sayi%10
onlarbasamagi=(sayi//10)
print(a[onlarbasamagi]+b[birlerbasamagi])
"""
"""
a=["ACM",5,8,11,"Python","Java",7]
print(a)
for i in range(len(a)):
    try:
        a[i]+=1
    except TypeError:
        print("String geldi")
        continue
print("Güncellenen arrayimiz: ",a)
"""
"""
a=[]
a.append(ACM)
"""
"""
def acmkayitolustur(isim,soyisim,okulnumarasi):
    print("Aramıza hoşgeldin\n")
    print(isim,soyisim,okulnumarasi)

isim=input("isminiz nedir")
soyisim=input("soyisminiz nedir")
okulnumarasi=int(input("okul numranız nedir"))
acmkayitolustur(isim,soyisim,okulnumarasi)
"""
"""
def karesinial(a):
    a=a**2
    return a
a=int(input("bir sayi giriniz:"))
a=karesinial(a)

"""
"""
a=[1,2,3,4,5]
b=list(a)
b.append(50)
print(a)
"""

