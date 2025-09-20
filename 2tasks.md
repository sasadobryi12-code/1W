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
<img width="1100" height="681" alt="image" src="https://github.com/user-attachments/assets/f2104b37-025e-4f0f-8e25-4eff475b5456" />

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
