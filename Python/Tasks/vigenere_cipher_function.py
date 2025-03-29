def vigenere_cipher_func(text, key):
    key_result = ''

    for x in range(len(message)):
        if x >= len(key):
            x %= len(key)
        key_result += key[x]

    step = 0
    tabula_recta = []
    for i in range(65, 91):
        curr_row = []
        for j in range(65, 91):
            if (j + step) > 90:
                j -= 26
            curr_row.append(chr(j + step))

        tabula_recta.append(curr_row)
        step += 1

    key_rows = [chr(x) for x in range(65, 91)]
    message_cols = [chr(x) for x in range(65, 91)]

    result = ''
    idx = 0
    for row in range(len(message)):
        idx_key = key_rows.index(key_result[idx])         # row = key
        idx_msg = message_cols.index(message[idx])        # col = message
        result += tabula_recta[idx_key][idx_msg]
        idx += 1

    return result


message = input()
key = input()

print(vigenere_cipher_func(message, key))


# message = ATTACKATDAWN
# key = LEMON
# Expected output: LXFOPVEFRNHR
