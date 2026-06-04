#Reverse String
#Slicing Method
word="QA Automation"
print(word[::-1])

#Loop Method
a="Automation"
rev=""
for char in a:
    rev=char+rev
print("loop method :", rev)

#Reversed Method
b="automation"
print("".join(reversed(b)))

#Using Def
word2="illuminati"
print("".join(reversed(word2)))

def text(word: str) -> str:
    rever=""
    for i in word:
        rever=i+rever
    return rever
print(text("kettle"))