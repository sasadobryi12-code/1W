# bin1.exe
<img width="1101" height="736" alt="image" src="https://github.com/user-attachments/assets/a36b7521-b940-42be-a368-56861d678a22" />

### -Открыл ida, закинул файл
### 
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
