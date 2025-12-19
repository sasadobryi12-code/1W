
# Задание 1 -----------

ids = {'user1': [213, 213, 213, 15, 213], 
       'user2': [54, 54, 119, 119, 119], 
       'user3': [213, 98, 98, 35]}

idsValue = ids.values()
idsList = list(idsValue)
znap = []

for i in range(len(idsList)):
    for j in range(len(idsList[i])):
        if idsList[i][j] not in znap:
            znap.append(idsList[i][j])


print(znap)

# Задание 2 -----------

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

number = {}

for i in queries:
    word = len(i.split())
    if word in number:
        number[word] += 1
    else:
        number[word] = 1

number_len = len(queries)

for num_word in sorted(number):
    percent = round(number[num_word] / number_len * 100, 2)
    print(f"Поисковых запросов, содержащих {num_word} слов(а): {percent}%")

# Задание 3 -----------

results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}

for key, values in results.items():
    r = (values['revenue'] / values['cost'] -1) * 100
    results[key]['roy'] = round(r,2)


print("{")
for key in sorted(results.keys()):
    print(f"'{key}': {results[key]},")
print("}")

# Задание 4 -----------

stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}

i = 0

for key, value in stats.items():
    if value > i:
        i = value

for key, value in stats.items():
    if value == i:
        print("Максимальный объем продаж на рекламном канале:", key)


