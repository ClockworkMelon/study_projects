line = input().split()

while True:
    command = list(map(str, input().split()))

    if "3:1" in command:
        break

    com_one = command[0]

    if com_one == 'merge':
        start = int(command[1])
        stop = int(command[2])

        start = max(0, start)
        stop = min(len(line) - 1, stop)

        if start <= stop:
            merged = ''.join(line[start:stop + 1])
            line[start:stop + 1] = [merged]

    elif com_one == 'divide':
        ele = int(command[1])
        parts = int(command[2])

        element = line[ele]
        length = len(element)
        part_size = length // parts
        result = []
        start = 0

        for i in range(parts - 1):
            result.append(element[start:start + part_size])
            start += part_size

        result.append(element[start:])

        line[ele:ele + 1] = result

print(' '.join(line))
