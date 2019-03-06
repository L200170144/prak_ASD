Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Nomer 1
>>> def cetakSiku(x):
	for i in range (1, x+1):
		print ("*"*i)

		
>>> cetakSiku(5)
*
**
***
****
*****
>>> #Nomer 2
>>> def gambarlahPersegiEmpat(a,b):
	i = 1
	print("@"*b)
	while (i<a):
		print ("@"+" "*(b-2)+"@")
		i+=1
	print ("@"*b)

	
>>> gambarlahPersegiEmpat (4,5)
@@@@@
@   @
@   @
@   @
@@@@@
>>> #Nomer 3(a)
>>> def jumlahHurufVokal (s):
	vok = "aiueo"
	jumlah = 0
	for i in s :
		if i.lower() in vok:
			jumlah += 1
	return (len(s), jumlah)

>>> jumlahHurufVokal("surakarta")
(9, 4)
>>> #Nomer 3(b)
>>> def jumlahHurufKonsonan (s):
	vok = "aiueo"
	jumlah = 0
	for i in s :
		if i.lower() not in vok:
			jumlah += 1
	return (len(s), jumlah)

>>> jumlahHurufKonsonan("surakarta")
(9, 5)
>>> #Nomer 4
>>> def rerata (b):
	jumlah = 0
	for i in b:
		jumlah += i
	return jumlah/len(b)

>>> print (rerata ([1,2,3,4,5]))
3.0
>>> g = [3,4,5,4,3,4,5,2,2,10,11,23]
>>> rerata(g)
6.333333333333333
>>> #Nomer 5
>>> from math import sqrt as sq
>>> def apakahPrima(n):
    n=int(n)
    assert n>=0
    primakecil=[2, 3, 5, 7, 11]
    bukanprima=[0, 1, 4, 6, 8, 9, 10]
    if n in primakecil:
        return True
    elif n in bukanprima:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if(n%i==0):
                return False
    return True

>>> print(apakahPrima(17))
True
>>> print(apakahPrima(123))
False
>>> #Nomer 6
>>> def cetakbilanganprima():
    prima=list()
    for i in range(2,1000):
        a = True
        for iter in prima:
            if(i%iter==0):
                a=False
                break
        if(a):
            print(i)
            prima.append(i)

            
>>> cetakbilanganprima()
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113
127
131
137
139
149
151
157
163
167
173
179
181
191
193
197
199
211
223
227
229
233
239
241
251
257
263
269
271
277
281
283
293
307
311
313
317
331
337
347
349
353
359
367
373
379
383
389
397
401
409
419
421
431
433
439
443
449
457
461
463
467
479
487
491
499
503
509
521
523
541
547
557
563
569
571
577
587
593
599
601
607
613
617
619
631
641
643
647
653
659
661
673
677
683
691
701
709
719
727
733
739
743
751
757
761
769
773
787
797
809
811
821
823
827
829
839
853
857
859
863
877
881
883
887
907
911
919
929
937
941
947
953
967
971
977
983
991
997
>>> #Nomer 7
>>> def faktorprima(n):
    prima=list()
    for i in range(2,n):
        a = True
        for iter in prima:
            if(i%iter==0):
                a=False
                break
        if a and n%i==0:
            prima.append(i)
    return prima

>>> faktorprima(10)
[2, 5]
>>> #Nomer 8
>>> def apakahTerkandung(a,b):
	return a.lower() in b.lower()

>>> h = "do"
>>> k = " Indonesia tanah air beta "
>>> apakahTerkandung(h,k)
True
>>> apakahTerkandung("pusaka",k)
False
>>> #Nomer 9
>>> def iterasi():
    for i in range(1,100):
        if (i%3)!=0 and (i%5)!=0:
            print(i)
        else:
            if (i%15)==0:
                print("pyton UMS")
            elif (i%3)==0:
                print("python")
            elif (i%5)==0:
                print("UMS")

                
>>> iterasi()
1
2
python
4
UMS
python
7
8
python
UMS
11
python
13
14
pyton UMS
16
17
python
19
UMS
python
22
23
python
UMS
26
python
28
29
pyton UMS
31
32
python
34
UMS
python
37
38
python
UMS
41
python
43
44
pyton UMS
46
47
python
49
UMS
python
52
53
python
UMS
56
python
58
59
pyton UMS
61
62
python
64
UMS
python
67
68
python
UMS
71
python
73
74
pyton UMS
76
77
python
79
UMS
python
82
83
python
UMS
86
python
88
89
pyton UMS
91
92
python
94
UMS
python
97
98
python
>>> #Nomer 10
>>> from math import sqrt as akar
>>> def selesaikanABC(a,b,c):
	a=float(a)
	b=float(b)
	c=float(c)
	D=(b**2)-(4*a*c)
	if D<0:
		return "Determinan negatif. Persamaan tidak mempunyai akar real"
	else:
		x1 = (-b+akar(D))/(2*a)
		x2 = (-b-akar(D))/(2*a)
		hasil = (x1,x2)
		return hasil

	
>>> selesaikanABC(1,2,3)
'Determinan negatif. Persamaan tidak mempunyai akar real'
>>> selesaikanABC(1,-5,6)
(3.0, 2.0)
>>> #Nomer 11
>>> def apakahKabisat(a):
	if(a%400==0):
		return True
	if(a%100==0):
		return False
	if(a%4==0):
		return True
	return False

>>> apakahKabisat(2000)
True
>>> apakahKabisat(1900)
False
>>> #Nomer 12
>>> import random
>>> def permainan():
	a=random.randrange(0, 100)
	while(True):
		b=int(input("Masukan tebakan: "))
		if(b>a):
			print("Itu terlalu besar, coba lagi")
		elif(b<a):
			print("Itu terlalu kecil, coba lagi")
		else:
			print("Ya, Anda benar")
			break

		
>>> permainan()
Masukan tebakan: 28
Itu terlalu besar, coba lagi
Masukan tebakan: 12
Itu terlalu kecil, coba lagi
Masukan tebakan: 16
Itu terlalu kecil, coba lagi
Masukan tebakan: 18
Itu terlalu besar, coba lagi
Masukan tebakan: 17
Ya, Anda benar
>>> #Nomer 13
>>> def katakan(a):
    x={"0":"","1":"Se","2":"Dua ","3":"Tiga ","4":"Empat ","5":"Lima ","6":"Enam ","7":"Tujuh ","8":"Delapan ","9":"Sembilan "}
    y={-1:"",-2:"Puluh ",-3:"Ratus ",-4:"Ribu ",-5:"Puluh ",6:"Ratus ",7:"Juta ",8:"Puluhjuta "}
    b=str(a)
    f=""
    i=-1
    while i>= -len(b):
        f=x[b[i]]+y[i]+f
        i-=1
    return f

>>> katakan (1999)
'SeRibu Sembilan Ratus Sembilan Puluh Sembilan '
>>> #Nomer 14
>>> def formatRupiah(a):
    b=str(a)
    c=""
    i = -1
    while i>= -len(b):
        if((i+1)%3==0 and (i+1)!=0):
            c="."+c
        c=b[i]+c
        i-=1
    return "Rp "+c

>>> formatRupiah(150000)
'Rp 150.000'
>>> 
>>> #Nama : Aiza Fravy Qanza
>>> #NIM : L200170144
>>> #Kelas D
