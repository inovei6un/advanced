rose_list = [letter for letter in "rose"]
tulip_list = [letter for letter in "tulip"]
lotus_list = [letter for letter in "lotus"]
daffodil_list = [letter for letter in "daffodil"]

vowels_collection = input().split(' ')
consonants_collection = input().split(' ')

while rose_list and tulip_list and lotus_list and daffodil_list:
    if len(vowels_collection) == 0 or len(consonants_collection) == 0:
        break
    vowel = vowels_collection.pop(0)
    consonant = consonants_collection.pop(-1)
    if vowel in rose_list:
        rose_list.remove(vowel)
    if vowel in tulip_list:
        tulip_list.remove(vowel)
    if vowel in lotus_list:
        lotus_list.remove(vowel)
    if vowel in daffodil_list:
        daffodil_list.remove(vowel)
    if consonant in rose_list:
        rose_list.remove(consonant)
    if consonant in tulip_list:
        tulip_list.remove(consonant)
    if consonant in lotus_list:
        lotus_list.remove(consonant)
    if consonant in daffodil_list:
        daffodil_list.remove(consonant)
        if consonant in daffodil_list:
            daffodil_list.remove(consonant)

if len(rose_list) == 0:
    print('Word found: rose')
elif len(tulip_list) == 0:
    print('Word found: tulip')
elif len(lotus_list) == 0:
    print('Word found: lotus')
elif len(daffodil_list) == 0:
    print('Word found: daffodil')
else:
    print('Cannot find any word!')

if vowels_collection:
    print(f"Vowels left: {' '.join(vowels_collection)}")
if consonants_collection:
    print(f"Consonants left: {' '.join(consonants_collection)}")

'''
o e a o e a i
p r s x r f


a a a
x r l t p p

u a o i u y o e
p m t l
'''
