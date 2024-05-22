
# KONUSU: PYTHON'DA YERLEŞİK (BUILT-IN) VERİ YAPILARI
# PYTHON'DA 4 TANE VERİ YAPISI VARDIR
#Veri yapıları aynı ya da farklı tipte verileri bir arada tutmamıza,
#saklamamıza ve onların üzerinde işlem yapmamıza yarar
# 1-LİSTELER (LIST)
# 2-SÖZLÜKLER (DICTIONARY)
# 3-DEMET (TUPLE)
# 4-KÜMELER (SET)

#1-LİSTELER
#Python'daki en kapsamlı veri yapısıdır

#listeler aşağıdaki gibi tanımlanır
# liste tanımlama 1. yol
my_list = []
print(type(my_list))

# liste tanımlama 2.yol
my_list2 = list()
print(type(my_list2))

#listeye eleman ekleme
my_list.append("ilk eleman")
print(my_list)
print(f"listenin ilk elemanı: {my_list[0]}")

my_list.append("ybs")
my_list.append("bst")
my_list.append("muhasabe")

print("-"*50)
print(my_list)

# listelerde elemanların index numarasını öğrenme

print(my_list.index("ybs"))

#append fonksiyonu sıralı bir şekilde eleman ekler
# sıfırıncı indexten başlar -1'e yani son indexe kadar gider

# istediğimiz index numarasına göre eleman ekleme

print(my_list.index("ybs"))

my_list.insert(1,"yeni")
print(my_list)
print(my_list[1])

print(f"dizinin değer uzunluğu: {len(my_list)}")

my_list.insert(10,"son")

print("-"*50)
print(my_list)
print(my_list.index("son"))
print(len(my_list))

# farklı veri tiplerini bir arada bulunduran liste tanımlama

print("-"*20)
my_list3 = ["ztyo ybs",10,bool(1),True,155.86]
print(my_list3)

# listenin tipi ve içerisindeki verilerin tipini öğrenme

print("-"*50)
print(f"listenin tipi =  {type(my_list3)}")
print(f"listenin 1. elemanının tipi = {type(my_list3[0])}")
print(f"listenin 2. elemanının tipi = {type(my_list3[1])}")
print(f"listenin 3. elemanının tipi = {type(my_list3[2])}")
print(f"listenin 4. elemanının tipi = {type(my_list3[3])}")
print(f"listenin 4. elemanının tipi = {type(my_list3[4])}")

#print(my_list3.clear())
#print(my_list3)

# del anahtar kelimesi (delete) kelimesinin kısaltmasıdır

#del my_list3
#print(my_list3)

# del ve list.clear() arasındaki fark:
# list.clear() fonksiyonu, listenin içindeki tüm değerleri siler
# del list ise listenin doğrudan kendisini siler !!!

print("-"*50)
my_list3.append("ybs")
my_list3.append("ybs")
print(my_list3)
print(my_list3.count("ybs"))
print(my_list3[5])
print(my_list3.count(my_list3[5]))
print("-"*50)

print(my_list3)

# Python'da tip kontrolü
if type(my_list3[-1]) == str:
    print(my_list3[-1])

elif type(my_list3[-1]) == int:
    print(f"my_list3[-1]'in tipi int'tir")
else:
    print("hiçbiri")

print("-"*50)

# list.extend() kullanımı:
# içerisine eklenilecek liste.extend(ekleyeceğimiz liste)

my_list4 = ["gümrük bölümü","uluslar arası ticaret"]

my_list3.extend(my_list4)
print(my_list3)
print("*"*50)

print(my_list3)

# sonuncu elemanı silmeye yarar list.pop()
my_list3.pop()
print(my_list3)

#list.remove() index sayısına göre o indexteki elemanı siler
# list.remove(4) 4.indexteki yani 5. değeri siler
my_list3.remove(my_list3[4])
print(my_list3)

print("-"*50)

# Python'da liste içerisindeki verileri sıralama (a'dan z'ye)
deneme1 = ["c","s","z","a","f","d"]
print(f"listenin orijinal hali = {deneme1}")

deneme1.sort()
print(f"listenin a'dan z'ye sıralanışı = {deneme1}")

# Python'da tersten sıralama (büyükten küçüğe, z'den a'ya)
deneme1.reverse()
print(f"listenin tersten (z'den a'ya) sıralnışı = {deneme1}")

# listeyi kopyalama (değer kopyalama yani içindeki değerleri kopyalama)
print(""*50)
deneme3 = ["makü","ybs","orta düzey", "programlama"]

deneme4 = deneme3.copy()
print(deneme3)
print(deneme4)

print("-"*50)
deneme3.pop()
print(deneme3)
print(deneme4)

# Değer tip ve Referans tip karşılaştırması

# Değer tip ataması
a = 10
b = 5

print(a)
print(b)
print("-"*50)

a = b
print(a)
print(b)

# Referans tip ataması
print("-"*50)
liste1 = ["burdur","mehmet","akif","ersoy","üniversitesi"]
liste2 = liste1

print(liste1)
print(liste2)

liste1.pop()

print("-"*10)
print(liste1)
print(liste2)

# list.copy() => listenin içindeki değerleri kopyalar
# list1 = list2 ise list2'nin bellekteki (RAM'deki) referans adresini
# list2'nin içindeki değerlerle kopyalar

# for döngüsü
# 1. Kullanım:
# for anahtar_kelime in range(başlangıç değeri,bitiş değeri,artış değeri)
# for döngüsünde range içerisine hiçbir değer verilmezse
# başlangıç sıfır kabul edilir ve range içerisindeki değere kadar
# yazdırılır (ama o değer yazdırılmaz => range(değer-1) mantığıyla çalışır)
# artış miktarı verilmezse 1 kabul edilir
for anahtar_kelime in range(5,11,2):
    print(anahtar_kelime)

print("-"*10)

# Veri yapıları içerisinde for kullanımı
# 1. yol: doğrudan listenin içindeyken çalışma
print(f"mylist3 = {my_list3}")

for i in my_list3:
    print(i)

print("-"*50)

# 2. yol: veri yapısının uzunluğunu range değeri olarak belirleyip
# buna göre döngünün artışını sağları

for i in range(len(my_list3)):
    print(my_list3[i])

print("-"*50)

# Listelere sıralı ve artan şekilde sayı ekleme

# 1. Yol
dizi = []

for i in range(1,11):
    dizi.append(i)

print(dizi)

# 2. Yol: 1'den 11'e kadar eleman ekleme (11 dahil değil)

dizi2 = list(range(1,11))
print(dizi2)

# 3. Yol

dizi3 = [x for x in range(1,11)]
print(dizi3)

# 3. Yol'un bir ayrıcalığı var. Sıralı bir şekilde yazdırabildiğimiz gibi
# elemanlara müdahale de edebiliyoruz (4. Yol da gösterilmiştir)

# 4. Yol: her bir elemanın karesini alarak eklemek
# list compherensions

diziek = [x for x in range(1,11)]
print(diziek)
dizi4 = [x%2==0 for x in range(1,11)]
print(dizi4)