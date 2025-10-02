s = str(input())
if len(s)%2==0:
    i= int(len(s)/2)
    print(s[i-1:i+1])
else:
    print(s[(len(s)%2)+1])
