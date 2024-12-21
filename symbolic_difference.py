word_1 = input()
word_2 = input()
result = ''

common_letters = set(word_1) & set(word_2)

for letter in common_letters:
    result += letter
print(result)