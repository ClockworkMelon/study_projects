kids = [x for x in input().split()]
trows = int(input())

removed_kid_index = 0
while len(kids) > 1:
    removed_kid_index = (removed_kid_index + trows - 1) % len(kids)
    removed_kid = kids.pop(removed_kid_index)
    print(f'Removed {removed_kid}')

print(f'Last is {kids[0]}')
