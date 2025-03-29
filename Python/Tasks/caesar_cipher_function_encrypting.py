def caesar_cipher(text, shift):
    result = ''
    for letter in text:
        result += chr(ord(letter) + shift)

    return result


text = input()
shift = int(input())

print(caesar_cipher(text, shift))


# text = ATTACKATDAWN
# shift = 3   to the right
# Expected output: DWWDFNDWGDZQ
