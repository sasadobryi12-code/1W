### Bin3.exe
<img width="1096" height="685" alt="image" src="https://github.com/user-attachments/assets/99f88906-ada4-4db5-8291-d497550cc29e" />

<img width="1181" height="712" alt="image" src="https://github.com/user-attachments/assets/6cd7ed6a-17c1-44fc-86a3-3b21ff571108" />

Программа принимает строку из аргументов командной строки, проверяет что её длина не превышает 128 символов, затем многократно переставляет символы строки с помощью функции swaper и выводит изменённую строку.
```c#
if ( (unsigned int)((int (__cdecl *)(const char *))((char *)&etext + 1))(argv[1]) <= 0x80 )
```
0x80 = 128

```c#
if ( strlen(argv[1]) <= 128 )
```

Функция swaper:
#### -получает длину строки
#### -разбивает строку на блоки размера a2
#### -в каждом блоке меняет местами первый и последний символ

<img width="1034" height="438" alt="image" src="https://github.com/user-attachments/assets/513c5153-9a07-45ca-b728-35aa06454850" />


### Bin4.exe
<img width="1088" height="675" alt="image" src="https://github.com/user-attachments/assets/3ecf01af-18cb-4996-98e2-abc541f051ec" />
 Программа принимает два числа a и b, расшифровывает встроенную строку с помощью аффинного шифра Цезаря, затем использует полученную строку как ключ для XOR-дешифрования массива байтов и выводит флаг.
Значения a = 21 и b = 15 получены перебором допустимых a (взаимно простых с 26) и b (0–25) до появления осмысленного текста после дешифрования, который затем корректно раскрывает флаг.  arctf{1t_wa5_v3ry_9los3}
<img width="1422" height="907" alt="image" src="https://github.com/user-attachments/assets/b24d3b85-976b-4956-b26e-13f426940dc1" />


### Bin5.exe
<img width="1098" height="684" alt="image" src="https://github.com/user-attachments/assets/6f023640-812a-4221-8643-908f109d5e6c" />

#### Открыл IDA, закинул bin5.exe и увидел код, где 5 проверок, которые не сильно спрятаны, все в коде на видном месте, надо просто писать в cmd 2500, 1828, 360, 9 и CaptureTheFlag, если все 5 проверок пройти он напишет флаг arctf{a_l0t_o7_q4est1ons}

```c#
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char q5[100]; // [rsp+20h] [rbp-80h] BYREF
  int q4; // [rsp+8Ch] [rbp-14h] BYREF
  int q3; // [rsp+90h] [rbp-10h] BYREF
  int q2; // [rsp+94h] [rbp-Ch] BYREF
  int q1; // [rsp+98h] [rbp-8h] BYREF
  int cnt; // [rsp+9Ch] [rbp-4h]

  _main(argc, argv, envp);
  setlocale(0, "Rus");
  puts(&Buffer);
  scanf("%d", &q1);
  if ( q1 == 2500 )
  {
    ++cnt;
    puts(&byte_404032);
  }
  else
  {
    puts(&byte_404039);
  }
  puts(&byte_404048);
  scanf("%d", &q2);
  if ( q2 == 1828 )
  {
    ++cnt;
    puts(&byte_404032);
  }
  else
  {
    puts(&byte_404039);
  }
  puts(&byte_404088);
  scanf("%d", &q3);
  if ( q3 == 360 )
  {
    ++cnt;
    puts(&byte_404032);
  }
  else
  {
    puts(&byte_404039);
  }
  puts(&byte_4040B8);
  scanf("%d", &q4);
  if ( q4 == 9 )
  {
    ++cnt;
    puts(&byte_404032);
  }
  else
  {
    puts(&byte_404039);
  }
  puts(&byte_404100);
  scanf("%s", q5);
  if ( !strcmp(q5, "CaptureTheFlag") )
  {
    ++cnt;
    puts(&byte_404032);
  }
  else
  {
    puts(&byte_404039);
  }
  if ( cnt == 5 )
    puts("arctf{a_l0t_o7_q4est1ons}");
  else
    puts(&byte_404170);
  system("Pause");
  return 0;
}
```
