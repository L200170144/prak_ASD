Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Aiza Fravy Qanza
>>> #L200170144
>>> #D
>>> #Modul 04
>>> 
>>> #Nomer 1
>>> class mhsTIF():
    def __init__(self, nama, asal, saku):
        self.nama = nama
        self.asal = asal
        self.saku = saku

        
>>> def cari(n):
	baru = []
	for i in range(len(n)):
		if(n[i].asal.lower() == 'samarinda'):
			baru.append(i)
	return baru

>>> c0 = mhsTIF('Aiza','Samarinda',240000)
>>> c1 = mhsTIF('Bella','Jakarta',290000)
>>> c2 = mhsTIF('Chiara','Balikpapan',250000)
>>> c3 = mhsTIF('Devia','Bandung',230000)
>>> c4 = mhsTIF('Elvira','Surabaya',235000)
>>> c5 = mhsTIF('Farah','Bandung',220000)
>>> c6 = mhsTIF('Gege','Tarakan',260000)
>>> daftar = [c0,c1,c2,c3,c4,c5,c6]
>>> cari(daftar)
[0]
>>> 
>>> #Nomer 2
>>> def sakuTerkecil(n):
	baru = n[0].saku
	for i in range(len(n)):
		if(n[i].saku<baru):
			baru = n[i].saku
	return baru

>>> sakuTerkecil(daftar)
220000
    #Nomer 3
>>>def sakuTerkecil2(n):
	baru = n[0].saku
	list = []
	for i in range(len(n)):
		if(n[i].saku==baru):
			list.append(n[i].nama)
		elif(n[i].saku<baru):
			baru = n[i].saku
			list = []
			list.append(n[i].nama)
	return list

>>> sakuTerkecil2(daftar)
['Farah']
>>> 
>>> #Nomer 4
>>> def sakuKurang(n):
	batas = 250000
	list = []
	for i in range(len(n)):
		if(n[i].saku < batas):
			list.append(n[i].nama)
	return list

>>> sakuKurang(daftar)
['Aiza', 'Devia', 'Elvira', 'Farah']
>>> 
>>> #Nomer 5
>>> class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

		
>>> class LinkedList:
	def __init__(self):
		self.head = None
	def pushAw(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
		return self.head
	def search(self, x):
		current = self.head
		while current != None:
			if current.data == x:
				return "True"
			current = current.next
		return "False"
	def display(self):
		current = self.head
		while current is not None:
			print(current.data, end = ' ')
			current = current.next

			
>>> k=LinkedList()
>>> k.pushAw(12)
<__main__.Node object at 0x00000176071279B0>
>>> k.pushAw(23)
<__main__.Node object at 0x000001760729BA90>
>>> k.pushAw(10)
<__main__.Node object at 0x000001760729BCF8>
>>> k.pushAw(19)
<__main__.Node object at 0x00000176072ABBE0>
>>> k.pushAw(12)
<__main__.Node object at 0x00000176072ABC18>
>>> k.pushAw(34)
<__main__.Node object at 0x00000176072ABC50>
>>> k.search(23)
'True'
>>> k.search(8)
'False'
>>> 
>>> #Nomer 6
>>> def binSe(list, target):
	low = 0
	high = len(list) - 1
	while(low<=high):
		mid = (low+high)//2
		if(list[mid] == target):
			return "Target di index "+str(mid)
		elif(target<list[mid]):
			high = mid - 1
		else:
			low = mid +1
	return "Target tidak ditemukan"

>>> l=[1,2,3,4,5,6,7,8,9]
>>> target=10
>>> binSe(l, target)
'Target tidak ditemukan'
>>> target=22
>>> binSe(l, target)
'Target tidak ditemukan'
>>> target=1
>>> binSe(l, target)
'Target di index 0'
>>> 
>>> #Nomer 7
>>> def binSe(kumpulan, target):
	temp = []
	low = 0
	high = len(kumpulan)-1
	while low <= high :
		mid = (high+low)//2
		if kumpulan[mid] == target:
			midKiri = mid-1
			while kumpulan[midKiri] == target:
				temp.append(midKiri)
				midKiri = midKiri-1
			temp.append(mid)
			midKanan = mid+1
			while kumpulan[midKanan] == target:
				temp.append(midKanan)
				midKanan = midKanan+1
			return temp
		elif target < kumpulan[mid]:
			high = mid-1
		else:
			low = mid+1
	return False

>>> kumpulan=[1,3,5,7,9,11,13,15]
>>> target = 1
>>> binSe(kumpulan,target)
[0]
>>> target = 5
>>> binSe(kumpulan,target)
[2]
>>> target = 10
>>> binSe(kumpulan,target)
False
>>> 
