import string

letters_dict = {}

for x in range(0, 30):
    file_name = 'word_{}.txt'.format(x)

    my_file = open(file_name)
    word = my_file.read()

    for letter in word:
        lower_letter = letter.lower()
        if lower_letter not in letters_dict:
            letters_dict[lower_letter] = 1
        else:
            letters_dict[lower_letter] += 1

    my_file.close()

alphabet = list(string.ascii_lowercase)

for letter in letters_dict:
    if letter not in alphabet:
        print('error: ', letter)

results = ''

for letter in alphabet:
    letter_count = letter + str(letters_dict[letter])
    results = results + letter_count

print(results)