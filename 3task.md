### Открыл IDA, закинул бинарник и получил код:
```c
__int64 start()
{
  __int64 v0; // rcx
  __int64 i; // rdx
  __int16 v2; // ax
  __int64 v3; // rcx
  __int64 j; // r10
  __int64 v5; // rax
  __int16 v6; // t2
  __int64 result; // rax
  char v8[16]; // [rsp+0h] [rbp-10h]

  v0 = 0i64;
  for ( i = 0i64; ; ++i )
  {
    v2 = *(_WORD *)((char *)&unk_140003000 + v0);
    v0 += 2i64;
    if ( !v2 )
      break;
  }
  v3 = 0i64;
  for ( j = 0i64; ; ++j )
  {
    v5 = *(_WORD *)((char *)&unk_140003000 + v3) >> 1;
    v6 = (unsigned __int16)v5 % 6u;
    LOBYTE(v5) = (unsigned __int16)v5 / 6u;
    BYTE1(v5) = v6;
    result = v5 - 1;
    v8[j] = result;
    if ( i == j )
      break;
    v3 += 2i64;
  }
  v8[j] = 0;
  return result;
}
```
