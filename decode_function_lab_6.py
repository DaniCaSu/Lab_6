def main():
    user_input = 0
    while user_input != 3:
        print(f'Menu\n  '
             f'-------------\n'
             f'1. Encode\n'
             f'2. Decode\n'
             f'3. Quit\n')
        encoded_password = ''
        password = ''
        user_input = int(input('Please enter an option: '))
        if user_input == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!')
        elif user_input == 2:
            encoded_password = input('Please enter your password to decode: ')
            password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {password}')


def encode(password):
       #Takes in a string password (int only) and shifts each integer up by 3
    encoded = []
    for char in password:
        encoded.append(str((int(char)+3)%10))
    return ''.join(encoded)


def decode(encoded_password):

    decoded_password = ""
    for digit in encoded_password:
        # Cast digit to an int and add 3. % 10 to get the first digit after adding.
        digit = (int(digit) - 3) % 10
        # Add each digit to a new string
        decoded_password += str(digit)
    return decoded_password


if __name__ == '__main__':
    main()