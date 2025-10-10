# bin1.exe

<img width="1095" height="605" alt="image" src="https://github.com/user-attachments/assets/3f4ebce6-41cd-4dd9-ab86-4a7c94bc6adf" />

### Открыл ida, закинул код и получил:

<img width="918" height="647" alt="image" src="https://github.com/user-attachments/assets/9d4d59c6-3b5c-45e0-95c4-8bc6567fc93f" />

### Просмотрел

<img width="288" height="65" alt="image" src="https://github.com/user-attachments/assets/0c1e4dce-0d01-45c3-92d3-570a1f06c407" />

### Выписывает нам ,,Input password:", потом берет нашу вписанную строку и кидает ее в Destination

<img width="586" height="407" alt="image" src="https://github.com/user-attachments/assets/bc05f5e4-36d5-42f2-a959-98075917bb91" />

### Дальше у нас идёт проверка сначала на длину строки, она должна быть 15
### После заходим в цикл и посимвольно проверяем каждый элемент 
### После у нас идёт функция shl, которая преобразовывает наш символ, сдвигаем первый бит на 7 влево, убираем спарва лишний и добавляем ноль в начало

<img width="360" height="169" alt="image" src="https://github.com/user-attachments/assets/56fe3dad-bacb-477b-9123-36a1362a0622" />

### дальше заходим в to_sets и видим следующую картинку

<img width="664" height="601" alt="image" src="https://github.com/user-attachments/assets/47e4426d-661a-4083-ab78-21d53811ce7b" />

### Видим справа числа, которые записаны в 16-ричной системе и к какому set_x оно прикрепленно
### делаем небольшие мохинации в питоне и получаем код, где применяем ROR для восстановления исходных значений, сначала создаем список, где будут хранится наши буквы и мы юудем применять к ниф функцию ROR, чтобы найти нужные символы

```python
def ror(b):
    return ((b >> 1) | (b << 7)) & 0xFF

bytes_after_rol = [0xC2, 0xE4, 0xC6, 0xE8, 0xCC, 0xF6, 0xE0, 0x60,
                   0xD2, 0xDC, 0xE8, 0xCA, 0xE4, 0xE6, 0xFA]

original_bytes = [ror(b) for b in bytes_after_rol]
original_chars = [chr(b) for b in original_bytes]
password = ''.join(original_chars)

print(f"{password}")
```

### Получаем на выходе наш флаг arctf{p0inters}
### Вписываем его и получаем верный результат
