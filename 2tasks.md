# bin1.exe
<img width="1101" height="736" alt="image" src="https://github.com/user-attachments/assets/a36b7521-b940-42be-a368-56861d678a22" />

### -Открыл ida, закинул файл
### -После декомпиляции получил код:
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char Str2[14]; // [esp+3h] [ebp-10Dh] BYREF
  char Str1[255]; // [esp+11h] [ebp-FFh] BYREF

  strcpy(Str2, "VaL1DP@$$w0rD");
  ((void (__cdecl *)(char *))((char *)&etext + 1))(aThisIsSecureAp);
  scanf("%s", Str1);
  if ( !strcmp(Str1, Str2) )
    ((void (__cdecl *)(char *))((char *)&etext + 1))(aYouAreWelcomeN);
  else
    ((void (__cdecl *)(char *))((char *)&etext + 1))(aGoOutOfHere);
  return 0;
}
```
### -Просмотрев код, увидел, что он сравнивает две строки(Первую вводим сами, вторая нам дается "VaL1DP@$$w0rD" )
```c
  if ( !strcmp(Str1, Str2) )
    ((void (__cdecl *)(char *))((char *)&etext + 1))(aYouAreWelcomeN);
  else
    ((void (__cdecl *)(char *))((char *)&etext + 1))(aGoOutOfHere);
  return 0;
```
### -Вписал "VaL1DP@$$w0rD" и получил "You are welcome! Now you can use this app."

# bin2.exe
<img width="1106" height="681" alt="image" src="https://github.com/user-attachments/assets/46cb95e7-70c5-456e-a845-aebf8d3cb080" />

### -Открыл ida, закинул файл
### -После декомпиляции получил код:

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char Str[255]; // [esp+5h] [ebp-FFh] BYREF

  ((void (__cdecl *)(char *))((char *)&etext + 1))(aThisIsSecureAp);
  scanf("%s", Str);
  if ( strlen(Str) == 6
    && Str[0] == 113
    && Str[1] == 119
    && Str[2] == 101
    && Str[3] == 114
    && Str[4] == 116
    && Str[5] == 121 )
  {
    ((void (__cdecl *)(char *))((char *)&etext + 1))(aYouAreWelcomeN);
    return 1;
  }
  else
  {
    ((void (__cdecl *)(char *))((char *)&etext + 1))(aGoOutOfHere);
    return 0;
  }
}
```
### - В коде видим, что длина строки 6 и идет проервка на айди символов

```c
  if ( strlen(Str) == 6
    && Str[0] == 113
    && Str[1] == 119
    && Str[2] == 101
    && Str[3] == 114
    && Str[4] == 116
    && Str[5] == 121 )
```
### -Открываем таблицу айди символов и подбираем нужный.
### -Итоговый результат: "qwerty"

# bin3.exe
<img width="1100" height="685" alt="image" src="https://github.com/user-attachments/assets/cee73cc4-932f-4e72-a859-bf893add8f3d" />


### -Открыл ida, закинул файл
### -После декомпиляции получил код:

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char Destination[32]; // [rsp+20h] [rbp-70h] BYREF
  char Str1[32]; // [rsp+40h] [rbp-50h] BYREF
  char Source[40]; // [rsp+60h] [rbp-30h] BYREF
  char v7[8]; // [rsp+88h] [rbp-8h] BYREF

  _main();
  strcpy(v7, "0xjfkD2");
  puts("Enter Username: ");
  scanf("%30s", Source);
  puts("Enter Password: ");
  scanf("%30s", Str1);
  strcpy(Destination, Source);
  strcat(Destination, v7);
  if ( !strcmp(Str1, Destination) )
    puts("Password is correct. Good job");
  else
    puts("No, thats not it. Try again\n");
  return 0;
}
```

### -Видим, что нам надо вписать логин и пароль
### -После чего он копирует наш логин в "Destination" и добавляет в конец строку, в которой написано "0xjfkD2"
```c
strcpy(Destination, Source);
strcat(Destination, v7);
```
### -И делает проверку на одинаковые строки
```c
if ( !strcmp(Str1, Destination) )
    puts("Password is correct. Good job");
  else
    puts("No, thats not it. Try again\n");
  return 0;
```
### -Вписывает свой любой логин, а в пороль без пробелов пишем свой же логин и добавляем "0xjfkD2"

# bin4.exe

<img width="1095" height="675" alt="image" src="https://github.com/user-attachments/assets/4c6f62f5-9b54-460b-b4e9-c677f60b3ef6" />



### -Открыл ida, закинул файл
### -После декомпиляции получил код:
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char v4[256]; // [esp+0h] [ebp-204h] BYREF
  char Buffer[256]; // [esp+100h] [ebp-104h] BYREF
  FILE *Stream; // [esp+200h] [ebp-4h]

  Stream = fopen(FileName, Mode);
  if ( Stream )
  {
    fgets(Buffer, 255, Stream);
    fclose(Stream);
    Stream = fopen(aHello2, aR_0);
    if ( Stream )
    {
      fgets(v4, 255, Stream);
      fclose(Stream);
      if ( check(Buffer, v4) )
      {
        puts(aNope);
        return 1;
      }
      else
      {
        if ( !check2(Buffer) )
          printf("Flag{%s}\n", Buffer);
        return 0;
      }
    }
    else
    {
      puts(aNotAgain);
      return 3;
    }
  }
  else
  {
    puts(::Buffer);
    return 5;
  }
}
```
### -Видим, что он открывает два файла по отдельности
```c
Stream = fopen(FileName, Mode);

Stream = fopen(aHello2, aR_0);
```
### -В коде находим их названия: "Hello1" и "Hello2"
### -Создаем в папке с бинарников 2 текстовых файла и убираем расширение, чтобы он стал просто файлом
### -Дальше у нас проверка на символы:
```c
int __cdecl check(int a1, int a2)
{
  int i; // [esp+0h] [ebp-Ch]
  int v4; // [esp+4h] [ebp-8h]
  int v5; // [esp+8h] [ebp-4h]

  v5 = ((int (__cdecl *)(int))((char *)&etext + 1))(a1);
  v4 = ((int (__cdecl *)(int))((char *)&etext + 1))(a2);
  if ( v5 != v4 )
    return -1;
  for ( i = 0; i < v5; ++i )
  {
    if ( *(char *)(i + a1) != *(char *)(v4 - 1 - i + a2) )
      return -1;
  }
  return 0;
}

```
### - и
```c
int __cdecl check2(char *a1)
{
  if ( ((int (__cdecl *)(char *))((char *)&etext + 1))(a1) != 8 )
    return -1;
  if ( *a1 != a1[6] )
    return -1;
  if ( a1[2] != a1[3] )
    return -1;
  if ( a1[3] != a1[7] )
    return -1;
  if ( a1[1] != 102 )
    return -1;
  if ( a1[7] != 115 )
    return -1;
  if ( *a1 != 122 )
    return -1;
  if ( a1[5] - a1[4] != 8 )
    return -1;
  if ( a1[5] == 105 )
    return 0;
  return -1;
}
```
### -Понимаем, что длина строки 8 символов
### - a1[1] должен быть равен 102, это буква "f"
### - a1[7] должен быть равен 115, это буква "s"
### - a1 должен быть равен 122, это буква "z"
### - a1[5] должна быть равна 105, это буква "i"
### - a1[3] должен быть равен a1[7]
### - a1[2] должен быть равен a1[3]
### - a1[5] - a1[4] равен 8, тоесть a1[4] это "a"
### - a1[6] должен быть равен a1
### - Получаем "zfssaizs", вписываем его в "Hello1", открываем "Hello2" и записываем туда отзеркаленую строку "sziassfz"


# bin5.exe

<img width="1100" height="683" alt="image" src="https://github.com/user-attachments/assets/9bd4473e-be7c-475f-a4e7-893360da7644" />

### -Открыл ida, закинул файл
### -После декомпиляции получил код:
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  ((void (__cdecl *)(char *))((char *)&etext + 1))(aEnterSerialNum);
  scanf("%s", &Buf);
  if ( Check() )
    PrintOK();
  else
    PrintError();
  return 0;
}
```
### И
```c
int Check()
{
  size_t v0; // eax
  int i; // [esp+0h] [ebp-8h]

  v0 = strlen(&Buf);
  if ( v0 != 7 )
    return 0;
  if ( Buf != 97 )
    return 0;
  for ( i = 1; i < (int)(v0 - 1); ++i )
  {
    if ( *(&Buf + i) != i + *(&Buf + i - 1) )
      return 0;
  }
  return 1;
}
```

### -Длина строки должна быть 7
### -Первая буква в строке "a"
### -Дальше циклом проходит по строке и сравнивает
### -Сравнение происходит с арифметической прогрессией
```c
  for ( i = 1; i < (int)(v0 - 1); ++i )
  {
    if ( *(&Buf + i) != i + *(&Buf + i - 1) )
      return 0;
  }
```
### Для i=1 buf[1] = 1 + 97 = 98, а это "b"
### Для i=2 buf[2] = 2 + 98 = 100, а это "d"
### Для i=3 buf[3] = 3 + 100 = 103, а это "g"
### Для i=4 buf[4] = 4 + 103 = 107, а это "k"
### Для i=5 buf[5] = 5 + 107 = 112, а это "p"
### Для i=6 buf[6] = 6 + 112 = 118, а это "v"
### Получаем строку: "abdgkpv"
