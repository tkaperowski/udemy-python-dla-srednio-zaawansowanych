listA = list(range(6))
listB = list(range(6))

print(listA, listB)

product = []

for a in listA:
    for b in listB:
        product.append((a,b))

print(product)
print(id(product))

product =[(a,b) for a in listA for b in listB] #list comprehension
print(product)
print(id(product))

product =[(a,b) for a in listA for b in listB if a % 2 == 1 if b % 2 == 0]
print(product)
print(id(product))