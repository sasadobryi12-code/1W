# bin1.exe
<img width="1101" height="683" alt="image" src="https://github.com/user-attachments/assets/29911c50-cd99-49f7-8285-b67a88d241fa" />


### -Открыл Ida, закинул туда bin1.exe. 
### -После декомпиляции получил код:
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char Str1[128]; // [rsp+20h] [rbp-80h] BYREF

  _main(argc, argv, envp);
  puts("Hello, enter password ");
  scanf("%s", Str1);
  if ( !strcmp(Str1, "arctf{z3r0_0r_no7_0}") )
    puts("Yes!");
  else
    puts("Wrong!");
  system("Pause");
  return 0;
}
```
### Сначала вписаваем строку

### -Потом видим, что наша строка сравнивается с arctf{z3r0_0r_no7_0}, если строки равны, он написат Yes!, а если не равны, то напишет Wrong!
```c
if ( !strcmp(Str1, "arctf{z3r0_0r_no7_0}") )
```

# bin2.exe
<img width="1097" height="685" alt="image" src="https://github.com/user-attachments/assets/de0e629e-a41b-4536-9eb7-76b65fe7f8bc" />



### -Открыл Ida, закинул туда bin2.exe.
### -После декомпиляции получил код:

```c
int sub_401000()
{
  char Str[256]; // [esp+0h] [ebp-100h] BYREF

  printf("Enter flag to check: ");
  scanf("%s", Str);
  if ( strlen(Str) == 12 )
  {
    if ( strcmp(Str, Str2) > 0 )
    {
      if ( strcmp(Str, aMiccheckH4y) < 0 )
        printf("Yes! Correct flag is %s\n", Str);
      else
        printf("Wrong check 2!\n");
      return 0;
    }
    else
    {
      printf("Wrong check 1!\n");
      return 0;
    }
  }
  else
  {
    printf("Wrong length!\n");
    return 0;
  }
}
```

### -Просмотрел код, увидел, что необходимо ввести какой-то пароль, который в длину должен быть 12 букв
```c
 if ( strlen(Str) == 12 )
```
### -Начал искать дальше, увидел 2 пароля, которые сравнивают с нашей вписаной строкой(MicCheck_h4w и MicCheck_h4y)
```c
    if ( strcmp(Str, Str2) > 0 )
    {
      if ( strcmp(Str, aMiccheckH4y) < 0 )
```
### -Сравнивает по айди символа, значит нужно посмотреть в таблицу и увидеть, что между w и y находится x
### -Написал, проверил, все работает.

# bin3.exe
<img width="1101" height="681" alt="image" src="https://github.com/user-attachments/assets/c91987dc-95f5-49e5-b404-f33aff192757" />


### -Открыл Ida, закинул туда bin2.exe.
### -После декомпиляции получил код:
```c
int sub_40101D()
{
  int v1; // [esp+0h] [ebp-124h]
  int v2; // [esp+4h] [ebp-120h]
  int v3; // [esp+8h] [ebp-11Ch]
  int v4; // [esp+Ch] [ebp-118h]
  int v5; // [esp+10h] [ebp-114h]
  int v6; // [esp+14h] [ebp-110h]
  int v7; // [esp+18h] [ebp-10Ch]
  int v8; // [esp+1Ch] [ebp-108h]
  int v9; // [esp+20h] [ebp-104h]
  char Str[256]; // [esp+24h] [ebp-100h] BYREF

  printf("Enter flag to check: ");
  scanf("%s", Str);
  if ( strlen(Str) == 17 )
  {
    if ( atoi(Str) == 333 )
    {
      if ( sub_401000((int)Str, 5) == 111 )
      {
        if ( sub_401000((int)Str, 7) == 111 )
        {
          if ( sub_401000((int)Str, 11) == 111 )
          {
            v9 = sub_401000((int)Str, 9);
            if ( v9 == sub_401000((int)Str, 13) )
            {
              v8 = sub_401000((int)Str, 13);
              if ( v8 == sub_401000((int)Str, 15) )
              {
                v7 = sub_401000((int)Str, 17);
                if ( v7 == sub_401000((int)Str, 9) )
                {
                  v6 = sub_401000((int)Str, 4);
                  if ( v6 == sub_401000((int)Str, 6) )
                  {
                    v5 = sub_401000((int)Str, 4);
                    if ( v5 == sub_401000((int)Str, 8) )
                    {
                      v4 = sub_401000((int)Str, 4);
                      if ( v4 == sub_401000((int)Str, 10) )
                      {
                        v3 = sub_401000((int)Str, 4);
                        if ( v3 == sub_401000((int)Str, 12) )
                        {
                          v2 = sub_401000((int)Str, 4);
                          if ( v2 == sub_401000((int)Str, 14) )
                          {
                            v1 = sub_401000((int)Str, 4);
                            if ( v1 == sub_401000((int)Str, 16) )
                            {
                              if ( sub_401000((int)Str, 16) == 103 )
                              {
                                if ( sub_401000((int)Str, 9) == 48 )
                                  printf("Yes! Correct flag is %s\n", Str);
                                else
                                  printf("No zero!\n");
                                return 0;
                              }
                              else
                              {
                                printf("No \"g\"!\n");
                                return 0;
                              }
                            }
                            else
                            {
                              printf("Wrong check 10!\n");
                              return 0;
                            }
                          }
                          else
                          {
                            printf("Wrong check 9!\n");
                            return 0;
                          }
                        }
                        else
                        {
                          printf("Wrong check 8!\n");
                          return 0;
                        }
                      }
                      else
                      {
                        printf("Wrong check 7!\n");
                        return 0;
                      }
                    }
                    else
                    {
                      printf("Wrong check 6!\n");
                      return 0;
                    }
                  }
                  else
                  {
                    printf("Wrong check 5!\n");
                    return 0;
                  }
                }
                else
                {
                  printf("Wrong check 4!\n");
                  return 0;
                }
              }
              else
              {
                printf("Wrong check 3!\n");
                return 0;
              }
            }
            else
            {
              printf("Wrong check 2!\n");
              return 0;
            }
          }
          else
          {
            printf("No \"o3\"!\n");
            return 0;
          }
        }
        else
        {
          printf("No \"o2\"!\n");
          return 0;
        }
      }
      else
      {
        printf("No \"o1\"!\n");
        return 0;
      }
    }
    else
    {
      printf("Wrong check 1!\n");
      return 0;
    }
  }
  else
  {
    printf("Wrong length!\n");
    return 0;
  }
}
```
### И небольшая функция:
```c
int __cdecl sub_401000(int a1, int a2)
{
  return *(char *)(a2 - 1 + a1);
}
```
### -Длина строки 17, первые 3 цифры это 333
```c
  if ( strlen(Str) == 17 )
  {
    if ( atoi(Str) == 333 )
```
### -Дальше программа проверяет по функции и проверяет какие буквы стоят
### -На 5 и 7 и 11 должна находится буква o
```c
      if ( sub_401000((int)Str, 5) == 111 )
      {
        if ( sub_401000((int)Str, 7) == 111 )
        {
          if ( sub_401000((int)Str, 11) == 111 )
          {
```

### -Дальше на 9 должна быть цифра 0
```c
                                if ( sub_401000((int)Str, 9) == 48 )
```

### -Дальше на 16 должна быть буква g
```c
                              if ( sub_401000((int)Str, 16) == 103 )
```

### -Потом 13, 15 и 17 должен быть такой же символ, как у 9, тоесть 0
```c
            v9 = sub_401000((int)Str, 9);
            if ( v9 == sub_401000((int)Str, 13) )
            {
              v8 = sub_401000((int)Str, 13);
              if ( v8 == sub_401000((int)Str, 15) )
              {
                v7 = sub_401000((int)Str, 17);
                if ( v7 == sub_401000((int)Str, 9) )
```
### -На 6,8,10,12,14,16 должен быть такой же символ, как у 4, тоесть g
```c
                {
                  v6 = sub_401000((int)Str, 4);
                  if ( v6 == sub_401000((int)Str, 6) )
                  {
                    v5 = sub_401000((int)Str, 4);
                    if ( v5 == sub_401000((int)Str, 8) )
                    {
                      v4 = sub_401000((int)Str, 4);
                      if ( v4 == sub_401000((int)Str, 10) )
                      {
                        v3 = sub_401000((int)Str, 4);
                        if ( v3 == sub_401000((int)Str, 12) )
                        {
                          v2 = sub_401000((int)Str, 4);
                          if ( v2 == sub_401000((int)Str, 14) )
                          {
                            v1 = sub_401000((int)Str, 4);
                            if ( v1 == sub_401000((int)Str, 16) )
                            {
```
### Получаем такую комбинацию:
### 333gogog0gog0g0g0

# bin4.exe
<img width="1099" height="682" alt="image" src="https://github.com/user-attachments/assets/4745232a-d8aa-4b84-a8e1-e5ca71c319d3" />


### -Открыл Ida, закинул туда bin2.exe.

### -После декомпиляции получил код:
```c
int sub_40101D()
{
  size_t v1; // [esp+0h] [ebp-104h]
  char Str[8]; // [esp+4h] [ebp-100h] BYREF
  char Str1[248]; // [esp+Ch] [ebp-F8h] BYREF

  printf("Enter flag to check: ");
  scanf("%s", Str);
  v1 = 4 * strlen(Str);
  if ( v1 == sub_401000((int)Str, 1) )
  {
    if ( !strncmp(Str, Str2, 8u) )
    {
      if ( !strcmp(Str1, aKomne) )
        printf("Yes! Correct flag is %s\n", Str);
      else
        printf("Wrong check 2!\n");
      return 0;
    }
    else
    {
      printf("Wrong check 1!\n");
      return 0;
    }
  }
  else
  {
    printf("Wrong length!\n");
    return 0;
  }
}
```
### -Заметил, что первая проверка означает, что берется длина строки, умножается на 4 и сравнивается с айди первого символа, если первая буква H, то всего длина должна быть 18
### -Дальше функция проверяет на одинаковые символы
### !strncmp(Str, Str2, 8u)
### В нашем случае надо, чтобы 8 первых символов совпадали с str2
### Нашел саму строку str2: 4_points.
### Первый символ говорит о том, что в строке должно быть 52/4, тоесть 13 символов
### Дальше идет вторая проверка
### !strcmp(Str1, aKomne)
### Она проверяет нашу строку с еще одной строкой(komne), попробовал сделать следующим образом: посчитал количество символов в 4_points и komne и пришел к выводу, что надо просто соединить 2 строки и напить ее

# bin5.exe
<img width="1096" height="649" alt="image" src="https://github.com/user-attachments/assets/c5cf9149-3285-4fe5-a9b2-f6f09a3ada70" />

### -Открыл Ida, закинул туда bin5.exe.
### -Заметил, что идет проверка в цикле и проверяется схожесть айди символов.
### -Изучив подробнее код стало ясно, что str это f2hwldozg|:wbq, дальше в цикле можно увидеть i + v3[i] != Str[i], что означает, что правильные символы можно найти следующим образом:
### -Надо сначала заменить ! на =  i + v3[i] == Str[i], поменять местами: v3[i] == Str[i] – i, открыв айди символов, перебираем каждый:
### f-0 = f
### 2-1=1 и так далее берем айди и вычитаем саму i, получая нужные буквы

