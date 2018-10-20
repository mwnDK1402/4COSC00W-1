program_name = "Shift Cipher"
program_version = '0.1.0'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def print_version():
    print(program_name + ' version ' + program_version)

def print_operation_prompt():
    print("Input 'e' to start encoding")
    print("Press 'd' to start decoding")
    print("Press 'q' to quit\n")

def get_rotation():
    while True:
        try:
            rotation = int(input('Rotation integer: '))
            if 1 <= rotation <= 25:
                return rotation
        except ValueError:
            pass

        print('\nInvalid input: Must be an integer in the range 1-25\n')

def do_encode_operation():
    to_encode = input('Text to encode: ')
    rotation = get_rotation()
    encoded = encode(to_encode, rotation)
    print('\nEncoded text: ' + encoded)

def do_decode_operation():
    to_decode = input('Text to decode: ')
    rotation = get_rotation()
    decoded = decode(to_decode, rotation)
    print('\nDecoded text: ' + decoded)

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
            do_decode_operation()
        elif operation == 'q':
            quit()
        else:
            print('Invalid input')

        print()