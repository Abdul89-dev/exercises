word = 'Архангельск'
print(word[-1]) 

word = 'Архангельск'
print(word.count('a'))

word = 'Архангельск'
vowels = set("аеиоуэ")
word_set = set(word.lower())
 
print('Гласных {}, согласных {}'.format(len(word_set.intersection(vowels)),
                                        len(word_set.difference(vowels))))

sentence = 'Мы приехали в гости'
max_len = max(len(word) for word in sentence.split())

#Вывести первую букву каждого слова на отдельной строке не понял как сделать

sentence = 'Мы приехали в гости'
sentence_len = [len(x) for x in sentence.split()]
a = max(sentence_len) / min(sentence_len)
print(a)

