word="madam"
if word == word[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#Method - 2 Using 2 point
s="palindrome"
left=0
right=len(s)-1
flag=True
while left < right:
    if s[left] != s[right]:
        flag=False
        break
    left+=1
    right-=1
print(flag)
