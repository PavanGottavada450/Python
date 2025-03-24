n1 = int(input())
n2 = int(input())

prime = []

for i in range(n1,n2):
    count = 0
    if i<2 :
        continue

    if i == 2:
        prime.append(2)
        continue

    for j in range(2,i):
        if(i%j == 0):
            count = 1
            break
        
    if count == 0:
        prime.append(i)

print(prime)
    