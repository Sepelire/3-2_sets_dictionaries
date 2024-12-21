simolina_count = int(input())
oat_count = int(input())
semolina_lovers = set()
oat_lovers = set()

for _ in range(simolina_count):
    semolina_lovers.add(input()) 
for _ in range(oat_count):
    oat_lovers.add(input())
# semolina_lovers = {input().strip() for _ in range(..._count)}

common_lovers = semolina_lovers & oat_lovers

if len(common_lovers):
    print(len(common_lovers))
else:
    print('Таких нет')