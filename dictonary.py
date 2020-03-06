from collections import Counter

students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

a = Counter(students)
print(a)

# Module eksport

#2
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
print(max(set(students), key=lambda x: students.count(x)))

#3
#???

#4 и 5 не сообразил как сделать 
