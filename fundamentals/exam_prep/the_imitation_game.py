encrypted_message = input()

while True:
    command = input().split("|")

    if 'Decode' in command:
        print(f'The decrypted message is: {encrypted_message}')
        break

    action = command[0]
    if action == 'Insert':
        index = int(command[1])
        letter = command[2]
        message_list = [x for x in encrypted_message]
        message_list.insert(index, letter)
        encrypted_message = "".join(message_list)
    elif action == 'ChangeAll':
        replaced_letter = command[1]
        letter_replacement = command[2]
        new_message = encrypted_message.replace(replaced_letter, letter_replacement)
        encrypted_message = new_message
    elif action == "Move":
        index = int(command[1])
        message_list = [x for x in encrypted_message]
        left_message_list = message_list[:index]
        right_message_list = message_list[index:]
        new_message_list = right_message_list + left_message_list
        encrypted_message = "".join(new_message_list)


