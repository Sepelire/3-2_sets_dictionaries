word = input()
new_word = ''
for letter in set(word):
    new_word += letter
print(new_word)