program_name = "Shift Cipher"
program_version = '0.2.0'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def print_version():
    print(program_name + ' version ' + program_version)

def print_operation_prompt():
    print("Input 'e' to start encoding")
    print("Input 'd' to start decoding")
    print("Input 'q' to quit")
    print('\nThis program only encodes and decodes lower-case characters in the English alphabet.\n')

def get_rotation():
    while True:
        try:
            rotation = int(input('Rotation integer: '))
            if 1 <= rotation <= 25:
                return rotation
        except ValueError:
            pass

        print('\nInvalid input: Must be an integer in the range 1-25\n')

def find_possible_rotations(encoded, known):
    return [i for i in range(1, 26) if encode(known, i) in encoded]

def do_encode_operation():
    to_encode = input('Text to encode: ')
    rotation = get_rotation()
    encoded = encode(to_encode, rotation)
    print('\nEncoded text: ' + encoded)

def print_decrypt_method_prompt():
    print("Input 'k' to decrypt based on a known key")
    print("Input 'm' to decrypt based on a known part of the decrypted message")
    print("Input 'q' to quit\n")

def decrypt_from_key():
    to_decode = input('Text to decode: ')
    rotation = get_rotation()
    decoded = decode(to_decode, rotation)
    print('\nDecoded text: ' + decoded)

def decrypt_from_msg():
    to_decode = input('Text to decode: ')
    known_part = input('Known part: ')
    possible_rotations = find_possible_rotations(to_decode, known_part)
    print()
    for rotation in possible_rotations:
        decoded = decode(to_decode, rotation)
        print('Text decoded with rotation ' + str(rotation) + ': ' + decoded)

def decode(input, rotation):
    return encode(input, -rotation)

def encode(input, rotation):
    encoded = ''.join([(alphabet[(alphabet.index(c) + rotation) % 26] if c in alphabet else c) for c in input])
    return encoded

if __name__ == '__main__':
    print_version()
    print()
    while True:
        print_operation_prompt()
        
        operation = input('Operation: ')

        print()

        if operation == 'e':
            do_encode_operation()
        elif operation == 'd':
            print_decrypt_method_prompt()
            decrypt_method = input('Method of decryption: ')
            if decrypt_method == 'k':
                decrypt_from_key()
            elif decrypt_method == 'm':
                decrypt_from_msg()
            elif decrypt_method == 'q':
                quit()
            else:
                print("Invalid input: Enter 'k', 'm', or 'q'")
        elif operation == 'q':
            quit()
        else:
            print("Invalid input: Enter 'e', 'd', or 'q'")

        print()