str=input("string1:")
str1=[]
for i in str:
    if i.isalpha():
        if i not in str1:
            str1.append(i.lower())
element=','.join(str1)
print("uniqueLetters=",element)

    