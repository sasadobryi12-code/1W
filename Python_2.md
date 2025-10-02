# Задачи для занятия 2

### Задание 1
```python
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
```

### Задание 2

```python
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

s3 = 0
s2 = 0

for i in range(len(queries)):
    if len(queries[i].split(' ')) == 3:
        s3+=1
    else:
        s2+=1

print("Поисковых запросов, содержащих 2 слов(а):", round(s2/len(queries)* 100, 2), "%") 
print("Поисковых запросов, содержащих 3 слов(а):",  round(s3/len(queries) * 100, 2), "%" )
```

### Задание 3

```python
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

```

### Задание 4

```python
stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}

i = 0

for key, value in stats.items():
    if value > i:
        i = value

for key, value in stats.items():
    if value == i:
        print("Максимальный объем продаж на рекламном канале:", key)

```
