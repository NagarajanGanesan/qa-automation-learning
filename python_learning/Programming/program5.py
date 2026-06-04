#Sort by values
data = {"a": 50, "b": 20, "c": 30}

result = dict(sorted(data.items(), key=lambda x: x[1]))
#For descending order
result1 = dict(sorted(data.items(),key=lambda x: x[1],reverse=True))
print("Ascending order: ", result)
print("Descending Order: ", result1)

