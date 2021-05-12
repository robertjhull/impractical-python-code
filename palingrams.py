"""Find all word-pair palingrams in dictionary file."""

import load_dictionary

word_list = load_dictionary.load('dictionary.txt')

def find_palingrams():
    pali_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    pali_list.append((word, rev_word[end-i:]))
                    print('Found a palingram')
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    pali_list.append((rev_word[:end-i], word))
                    print('Found a palingram')
    return pali_list

palingrams = find_palingrams()
palingrams_sorted = sorted(palingrams)

print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))