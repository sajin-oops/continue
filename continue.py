str1 = "a,b,c,d"
str2 = " "
for i in str1:
    if i == ",":
        continue
    str2 = str2 + i
print(str2)

# abcd