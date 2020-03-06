names = ['Оля', 'Петя', 'Вася', 'Маша']
for i in names:
    print(i)

names = ['Оля', 'Петя', 'Вася', 'Маша']
for i in names:
    print(f'{i} {len(i)}')

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    if name in is_male.keys():
        if is_male[name]:
            print(f'{name} мужской пол')
        else:
            print(f'{name} женский пол')

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
print(f'Всего {len(groups)} групп')
for i in groups:
    print(f'В группе {len(i)} учеников')

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
counter = 0
for group in groups: 
    counter = counter + 1
    print("Группа {}: {}".format(counter, ', '.join(group)))

#все было легко сделать, просто правильно загуглив, даже не знаю насколько это честно