raws_count = int(input())
strings_arr = []

for raw in range(raws_count):
    strings_arr.append(input())

unique_words = set(' '.join(strings_arr).split())
for word in unique_words:
    print(word)