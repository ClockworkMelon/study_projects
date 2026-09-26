collection = [element.split() for element in input().split("|")][::-1]
[print(*row, end=" ") for row in collection if row]

# new_collection = []

# for idx in range(len(collection)):
#     row = collection[idx].split()
#     if row:
#         new_collection.append(row)
#
# for row in new_collection:
#     print(*row, end=" ")