def sequence(a):
    seq_row = []
    for x in range(a):
        if len(seq_row) == 0:
            seq_row.append(1)
        elif len(seq_row) < 4:
            seq_row.append(sum(seq_row))
        else:
            seq_row.append(seq_row[x-3] + seq_row[x - 2] + seq_row[x -1])

    return f'{" ".join(str(x) for x in seq_row)}'

num = int(input())

print(sequence(num))