from collections import deque

substrings = deque(input().split())

main_colors = {"red", "yellow", "blue"}
secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}
}

found_colors = []

while substrings:
    if len(substrings) == 1:
        first = substrings.pop()
        last = ""
    else:
        first = substrings.popleft()
        last = substrings.pop()

    combined = first + last
    reversed_combined = last + first

    color = None

    if combined in main_colors or combined in secondary_colors:
        color = combined
    elif reversed_combined in main_colors or reversed_combined in secondary_colors:
        color = reversed_combined

    if color:
        found_colors.append(color)
    else:
        first = first[:-1]
        last = last[:-1]

        middle_index = len(substrings) // 2

        if first:
            substrings.insert(middle_index, first)
        if last:
            substrings.insert(middle_index, last)

final_colors = []

for color in found_colors:
    if color in main_colors:
        final_colors.append(color)
    else:
        needed = secondary_colors[color]
        if needed.issubset(found_colors):
            final_colors.append(color)

print(final_colors)
