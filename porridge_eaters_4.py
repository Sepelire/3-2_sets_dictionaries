children_count = int(input())
porridge_lovers = {}

for _ in range(children_count):
    data = input().split()
    surname = data[0]
    porridges = data[1:]
    porridge_lovers[surname] = porridges
print(porridge_lovers)

needed_porridge = input().strip()

lovers = []
for surname, porridge in porridge_lovers.items():
    if needed_porridge in porridge:
        lovers.append(surname)

lovers.sort()

if lovers:
    for lover in lovers:
        print(lover)
else:
    print('Таких нет')