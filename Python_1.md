# Задания для занятия 1

### Задание 1
```python
s = str(input())
if len(s)%2==0:
    i= int(len(s)/2)
    print(s[i-1:i+1])
else:
    print(s[(len(s)%2)+1])

```

### Задание 2
```python
a = 1
b = 0
for i in range(10000):
    if a == 0:
        print(b)
        break          
    else:
        print('Введите число:')
        a = int(input())
        b+=a

```

### Задание 3

```python
boy = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girl = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boy) == len(girl):
    boy.sort()
    girl.sort()
    print('Идеальные пары: ')
    for i in range(len(boy)):
        print(boy[i], ' и ', girl[i])
else:
    print('Количетва парней и девушек неравны')

```


### Задание 4
```python
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius

countries_temperature = [
    ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Germany', [57.2, 55.4, 59, 59, 53.6]],
    ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

z = []

for country, temperatures in countries_temperature:
    celsius_temperatures = [fahrenheit_to_celsius(temp) for temp in temperatures]
    aver = sum(celsius_temperatures) / len(celsius_temperatures)
    z.append([country, round(aver, 1)])

print(z)
```

