s=" hello world"
a=len(s)
len_word=0
while a>0:
    a -=1
    if s[a] != " ":
        len_word += 1
    elif len_word > 0:
         break
print(len_word)             