d = eval(input())
target = int(input())
result = []
for key in d:
    if d[key] == target:
        result.append(key)
print(result)
