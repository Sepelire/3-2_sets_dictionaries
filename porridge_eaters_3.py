simolina_count = int(input())
oat_count = int(input())

names_set = {}

total_count = simolina_count + oat_count
for _ in range(total_count):
    name = input().strip()
    names_set[name] = names_set.get(name, 0) + 1

single_porridge_lovers = [name for name, count in names_set.items() if count == 1]

single_porridge_lovers.sort()

if single_porridge_lovers:
    for name in single_porridge_lovers:
        print(name)
else:
    print('Таких нет')