
p = int(input("Enter p"))
k = int(input("Enter k"))

a = int(input("Enter a"))
b = int(input("Enter b"))

c = (k**a)%p 
d = (k**b)%p

ssk1 = (d**a)%p
ssk2 = (c**b)%p

print(ssk1,ssk2,c,d)