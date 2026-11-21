file = open("sample.txt",'r')
file.seek(7)
print(file.tell())
print(file.read(7))


a = [1,2,3]
type(a)