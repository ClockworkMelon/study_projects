string = list(input().split())
nums = []
letters = []

for x in string:
    num =''
    let = ''
    for y in x:
        if y.isdigit():
            num += y
        else:
            let += y

    let = list(let)
    let[0], let[-1] = let[-1], let[0]
    let = "".join(let)

    nums.append(num)
    letters.append(let)

chars = [chr(int(ch)) for ch in nums]
new_str = [x + y for x, y in zip(chars, letters)]
print(" ".join(new_str))



