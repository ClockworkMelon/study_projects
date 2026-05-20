
def rounding(el):
    for x in range(len(el)):
        el[x] = round(el[x])
    return el

string = list(map(float, input().split(' ')))

print(rounding(string))