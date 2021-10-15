tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Андрей', 'Влад'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

tutor_gen = ((tutors[n], klasses[n]) if len(klasses) > n else (tutors[n], None) for n in range(len(tutors)))


print(type(tutor_gen), *tutor_gen, sep='\n')
print(next(tutor_gen))