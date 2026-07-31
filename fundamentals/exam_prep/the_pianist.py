number_of_pieces = int(input())
pieces_list = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    pieces_list[piece] = {"composer": composer, "key": key}

commands = input()

while commands != "Stop":
    commands = commands.split("|")
    action = commands[0]
    piece = commands[1]

    if action == "Add":
        composer = commands[2]
        key = commands[3]
        if piece not in pieces_list.keys():
            pieces_list[piece] = {"composer": composer, "key": key}
            print(f'{piece} by {composer} in {key} added to the collection!')
        else:
            print(f'{piece} is already in the collection!')
    elif action == "Remove":
        if piece in pieces_list.keys():
            del pieces_list[piece]
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
    elif action == "ChangeKey":
        key = commands[2]
        if piece in pieces_list.keys():
            pieces_list[piece]["key"] = key
            print(f'Changed the key of {piece} to {key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
    commands = input()

for piece, piece_info in pieces_list.items():
    composer = piece_info["composer"]
    key = piece_info["key"]
    print(f'{piece} -> Composer: {composer}, Key: {key}')
