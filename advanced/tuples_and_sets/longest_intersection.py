number_of_intersections = int(input())

longest_intersection = []

for _ in range(number_of_intersections):
    intersections = input().split('-')

    start_inter_one, end_inter_one = intersections[0].split(",")
    start_inter_two, end_inter_two = intersections[1].split(",")

    first_intersection = [x for x in range(int(start_inter_one), int(end_inter_one) + 1)]
    second_intersection = [y for y in range(int(start_inter_two), int(end_inter_two) + 1)]

    current_check = first_intersection + second_intersection
    current_longest_intersection = set()

    for element in current_check:
        if current_check.count(element) > 1:
            current_longest_intersection.add(element)

    if len(longest_intersection) < len(current_longest_intersection):
        longest_intersection = list(current_longest_intersection)
        longest_intersection.sort()

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")





