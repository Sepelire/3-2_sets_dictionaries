semolina_count = int(input())
oat_count = int(input())

names_set = {}

total_count = semolina_count + oat_count
for _ in range(total_count):
    name = input().strip()
    names_set[name] = names_set.get(name, 0) + 1

single_porridge_lovers = sum(1 for count in names_set.values() if count == 1)

if single_porridge_lovers:
    print(single_porridge_lovers)
else:
    print('Таких нет')