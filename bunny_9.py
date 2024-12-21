seen_dict = {}
while True:
    string = input().split()

    if string:
        for word in string:
            seen_dict[word] = seen_dict.get(word, 0) + 1
    else:
        break

for word, count in seen_dict.items():
    print(f'{word} {count}')