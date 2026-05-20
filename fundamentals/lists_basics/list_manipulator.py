nums = list(map(int, input().split()))

while True:
    command = input().split()

    if command[0] == "end":
        print(nums)
        break

    action = command[0]

    if action == "exchange":
        index = int(command[1])
        if index < 0 or index >= len(nums):
            print("Invalid index")
        else:
            nums = nums[index+1:] + nums[:index+1]

    elif action == "max" or action == "min":
        parity = command[1]

        filtered = []
        for x in nums:
            if parity == "odd" and x % 2 != 0:
                filtered.append(x)
            elif parity == "even" and x % 2 == 0:
                filtered.append(x)

        if len(filtered) == 0:
            print("No matches")
        else:
            if action == "max":
                target = max(filtered)
            else:
                target = min(filtered)

            rev_index = nums[::-1].index(target)
            last_index = len(nums) - 1 - rev_index
            print(last_index)

    elif action == "first":
        count = int(command[1])
        parity = command[2]

        if count > len(nums):
            print("Invalid count")
        else:
            filtered = []
            for x in nums:
                if parity == "odd" and x % 2 != 0:
                    filtered.append(x)
                elif parity == "even" and x % 2 == 0:
                    filtered.append(x)
            print(filtered[:count])

    elif action == "last":
        count = int(command[1])
        parity = command[2]

        if count > len(nums):
            print("Invalid count")
        else:
            filtered = []
            for x in nums:
                if parity == "odd" and x % 2 != 0:
                    filtered.append(x)
                elif parity == "even" and x % 2 == 0:
                    filtered.append(x)
            print(filtered[-count:])