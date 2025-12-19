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
