#Duplicate Characters
# word="programming"
# dup=[]

# for char in word:
#     if word.count(char) > 1 and char not in dup:
#         dup.append(char)
# print(dup)

#Method 2 - Using seen
# a="Dummy"
# seen=[]
# dup=[]
# for char in a:
#     if char in seen:
#         if char not in dup:
#             dup.append(char)
#     else:
#         seen.append(char)
# print(dup)

#Method - 3 Using Dictionary
# s="programming"
# f={}
# for char in s:
#     f[char] = f.get(char, 0)+1

# for k,v in f.items():
#     if v > 1:
#         print("method 2:", k)

#Method - 4 Using def
# def find_dup(text: str) -> list[str]:
#     seen=set()
#     dup=set()

#     for char in text:
#         if char in seen:
#             dup.add(char)
#         else:
#             seen.add(char)
#     return list(dup)

# print(find_dup("programming"))

#Method 5 - Using Collection
from collections import Counter
def finding_dup(text:str) -> list[str]:
    counts=Counter(text)
    return[char for char, count in counts.items() if count > 1]
print(finding_dup("programming"))