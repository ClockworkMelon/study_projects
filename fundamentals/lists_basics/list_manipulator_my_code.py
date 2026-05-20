nums = list(map(int, input().split(' ')))

while True:
    command = input().split()

    if command[0] == 'end':
        print(nums)
        break

    action = command[0]
    action_two = command[1]
    if len(command) == 3:
        action_three = command[2]

    odd_nums = [x for x in nums if x % 2 != 0]
    even_nums = [x for x in nums if x % 2 == 0]

    if action == 'exchange':
        if int(command[1]) < 0 or int(command[1]) > len(nums):
            print('Invalid index')
        else:
            left = nums[:int(command[1]) + 1]
            right = nums[int(command[1]) + 1:]
            nums = right + left

    elif action == 'max' and action_two == 'odd':
        if not odd_nums:
            print(f'No matches')
        else:
            max_index_odd = nums.index(max(odd_nums))
            print(f'{max_index_odd}')
    elif action == 'max'and action_two == 'even':
        if not even_nums:
            print(f'No matches')
        else:
            max_index_even = nums.index(max(even_nums))
            print(f'{max_index_even}')

    elif action == 'min' and action_two == 'odd':
        if not odd_nums:
            print(f'No matches')
        else:
            min_index_odd = nums.index(min(odd_nums))
            print(f'{min_index_odd}')
    elif action == 'min' and action_two == 'even':
        if not even_nums:
            print(f'No matches')
        else:
            min_index_even = nums.index(min(even_nums))
            print(f'{min_index_even}')

    elif action == 'first' and action_three == 'odd':
        if len(nums) < int(action_two):
            print(f'Invalid count')
        elif len(odd_nums) < int(action_two):
            print(f'{odd_nums}')
        elif not odd_nums:
            print(f'[]')
        else:
            print(f'{odd_nums[:int(action_two)]}')

    elif action == 'first' and action_three == 'even':
        if len(nums) < int(action_two):
            print(f'Invalid count')
        elif len(even_nums) < int(action_two):
            print(f'{even_nums}')
        elif not even_nums:
            print(f'[]')
        else:
            print(f'{even_nums[:int(action_two)]}')

    elif action == 'last' and action_three == 'odd':
        n = int(action_two)
        if len(nums) < n:
            print(f'Invalid count')
        elif len(odd_nums) < n:
            print(f'{odd_nums}')
        elif not odd_nums:
            print(f'[]')
        else:
            print(f'{odd_nums[-n:]}')

    elif action == 'last' and action_three == 'even':
        n = int(action_two)
        if len(nums) < n:
            print(f'Invalid count')
        elif len(even_nums) < n:
            print(f'{even_nums}')
        elif not even_nums:
            print(f'[]')
        else:
            print(f'{even_nums[-n:]}')



