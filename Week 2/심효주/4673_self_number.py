# self_num = [1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97]

def d(n):
    dn = n
    for value in list(str(n)):
        dn += int(value)
    return dn

excep = []
for i in range(10001):
    excep.append(d(i))

excep.sort()

for i in range(1, 10000):
    if i in excep:
        continue
    else:
        print(i)

