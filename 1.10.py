
def isDup(strs):
    i = 0
    while i < len(strs):
        j = i + 1
        while j < len(strs):
            if list(strs)[j] == list(strs)[i]:
                return True
            j += 1
        i += 1
    return False

S = str(input())
res = isDup(S)
print(res)
