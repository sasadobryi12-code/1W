
# Объяснения, как пользоваться IDA
### Сначала необходимо скачать саму IDA
### Ссылка на скачивание:
https://drive.google.com/drive/folders/1sp8iqJOhqLapV2TIpWlY9ORJG347ITuq?usp=sharing
### (Также у вас должен быть скачан Python)
### После того, как скачали, надо разорхивировать и убрать аккуратно в папку
### Дальше скачиваем папку с заданием(Посмотреть в ТГ канале) и скачать(Внимательно смотрите срок сдачи заданий)
### Дальше открываем саму IDA (иногда для бинарника нужно открыть не ida.exe, а ida64.exe)
<img width="932" height="954" alt="image" src="https://github.com/user-attachments/assets/4b83f4c8-2cae-4de7-9501-d36d9bf17cab" />

### Нажимаем ,,Ок"
<img width="495" height="325" alt="image" src="https://github.com/user-attachments/assets/b806e116-6f29-4775-9c7a-0553f009a2b7" />

### Дальше нажимаем ,,New"
<img width="387" height="350" alt="image" src="https://github.com/user-attachments/assets/c8239011-ca53-4f13-9dae-b9ae9c6e0841" />

### И выбираем нужный бинарный файл
<img width="1181" height="711" alt="image" src="https://github.com/user-attachments/assets/c42f4d5a-e20c-4ef8-adda-e984eb98136b" />

### Нажимаем много раз ,,Окей"
<img width="744" height="510" alt="image" src="https://github.com/user-attachments/assets/f9cd650e-a430-46b6-b4f4-2ce0a29d1561" />

### Получаем наш код в виде таблицы и странные символы
<img width="3439" height="1389" alt="image" src="https://github.com/user-attachments/assets/d1019495-f8a0-404a-a460-6116bafc572c" />

### Нажимаем левой кнопкой мыши на нашу таблицу справа и нажимаем ,,Tab" и получаем наш код:
<img width="3439" height="1387" alt="image" src="https://github.com/user-attachments/assets/68bd2185-cc17-4b05-ab14-4b8a8d47a04b" />

### Здесь мы внимательно смотрим и пытаемся понять, что делает данный код.
### Объясню на примере первого задания. 
```c
puts("Hello, enter password ");
```
### Этот код говорит о том, что нам выводят ,,Hello, enter password", смотрим дальше
```c
  scanf("%s", Str1);
```
### Код, чтобы мы могли что-то написать и он это проверил 
```c
  if ( !strcmp(Str1, "arctf{z3r0_0r_no7_0}") )
    puts("Yes!");
  else
    puts("Wrong!");
  system("Pause");
  return 0;
```
### Дальше код проверка. Смотрим, что он хочет проверить. !strcmp - проверяет на одинаковые строки, тоесть, если вы напишете то же самое, с чем он проверяет, вы молодцы, он напишеь YES!
### !strcmp(str1, str2), проверят str1 такая же, как и str2 или нет
### Мы сразу видим, что он проверяет нашу строку со срокой ,,arctf{z3r0_0r_no7_0}"
### Открываем cmd(открываем папку, где наш файл bin1.exe)

<img width="1864" height="145" alt="image" src="https://github.com/user-attachments/assets/97baf375-1e11-4a18-be13-da857604d2a3" />

### Дальше нажимаем на поисковую строку сверху 

<img width="1934" height="155" alt="image" src="https://github.com/user-attachments/assets/bfd67007-79ca-4567-b638-e3c27d9c6898" />

### И пишем cmd и нажимаем ,,ENTER"

<img width="1926" height="189" alt="image" src="https://github.com/user-attachments/assets/80dedc1f-3653-46a1-9ffe-a2a784b3ffef" />

### Открывается наша командная строка

<img width="1099" height="630" alt="image" src="https://github.com/user-attachments/assets/41df6d07-373a-4823-8e3f-bd48e3505282" />

### Вписываем сюда название нашего файла(В нашем случае это bin1.exe)

<img width="1098" height="634" alt="image" src="https://github.com/user-attachments/assets/407ebd23-1c64-45ae-bfa0-7f2f269d2f01" />

### И нажимаем ,,ENTER"
### Дальше вводим наш пароль и также нажимаем ,,ENTER" и видим, что все подошло и мы молодцы
### Дальше пишем команду  whoami (Это надо, чтобы преподаватель понимал, что вы пишите со своего компа, а не скопировали фотку откуда-то)

<img width="1092" height="633" alt="image" src="https://github.com/user-attachments/assets/6ac9e8ef-75d0-4c60-bb34-1507663053cb" />

### Дальше делаем скриншот выполненой задачи И НЕ ЗАБУДЬТЕ ЗАСКРИНИТЬ ВРЕМЯ
### Пример правильного скриншота

<img width="1104" height="676" alt="image" src="https://github.com/user-attachments/assets/76649763-9699-4e28-bd29-b10d21be17ca" />

### Дальше описываем, как мы выполнили работу и прикрепляем скриншот
### **Формат сдачи отчетов:**
### 1. Использовать аналоги на подобие Notion, Affine, Yonote ...
### 2. В решение необходимо описывать логику работы бинарника, с приложением соответствующих скриншотов, на которых должно обязательно быть следующие - Время и вывод работы утилиты `whoami`
### Используем для записи выполненой работы одну из этих сайтов(Либо гит хаб(как я))
### И СКИДЫВАЕМ ЕМУ ССЫЛКУ НА ФАЙЛ, НЕ СТОИТ СКИДЫВАТЬ ЕМУ В ЛС ФАЙЛ, ОН НЕ ПРИМЕТ
### Отчёт о выполненой работы делайте также, как и я сейчас все написал со скриншотами
### Удачи в работе :)
### И помните - если будете списывать - ничего не поймете - разбирайтесь сами :)
