class Stack(object):
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self)==0

    def __len__(self):
        return len(self.items)

    def peek(self):
        assert not self.isEmpty()
        return self.items[-1]

    def pop(self):
        assert not self.isEmpty()
        return self.items.pop()

    def push(self,data):
        self.items.append(data)

'''a=Stack()
a.push(2)
a.push(8)
a.push(3)
a.push(19)
a.push(99)
print(a.items)
print(a.pop())'''

#nomer 1
def cetakHexa(data):
    a = Stack()
    hxlist = "0123456789ABCDEF"
    while data != 0:
        sisa = data%16
        data = data//16
        a.push(hxlist[sisa])
    st=""
    for i in range(len(a)):
        st = st + str(a.pop())
    return st

print(cetakHexa(12))
print(cetakHexa(31))
print(cetakHexa(229))
print(cetakHexa(255))
print(cetakHexa(31519))

#nomer 2
nilai = Stack()
for i in range(16):
    if i%3 == 0:
        nilai.push(i)
        print(nilai.items)

#nomer 3
nilai = Stack()
for i in range(16):
    if i%3 == 0:
        nilai.push(i)
    elif i%4 == 0:
        nilai.pop()
print(nilai.items)
