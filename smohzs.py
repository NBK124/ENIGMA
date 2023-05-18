import string

alphabet = list(string.ascii_uppercase)
mapping = {k: alphabet[i] for i, k in enumerate(string.ascii_uppercase)}

def enigma(text, rotor1=0, rotor2=0, rotor3=0):
    r1 = alphabet[rotor1:] + alphabet[:rotor1]
    r2 = alphabet[rotor2:] + alphabet[:rotor2]
    r3 = alphabet[rotor3:] + alphabet[:rotor3]

    encrypted_text = []
    for letter in text.upper():
        if letter in alphabet:
            index = alphabet.index(letter)
            index = alphabet.index(r1[index])
            index = alphabet.index(r2[index])
            index = alphabet.index(r3[index])
            encrypted_text.append(mapping[alphabet[index]])
        else:
            encrypted_text.append(letter)

        r1 = r1[1:] + r1[:1]
        if alphabet.index(r1[0]) == rotor1:
            r2 = r2[1:] + r2[:1]
        if alphabet.index(r2[0]) == rotor2:
            r3 = r3[1:] + r3[:1]

    return ''.join(encrypted_text)


def decrypt_enigma(text, rotor1=0, rotor2=0, rotor3=0):
    r1 = alphabet[rotor1:] + alphabet[:rotor1]
    r2 = alphabet[rotor2:] + alphabet[:rotor2]
    r3 = alphabet[rotor3:] + alphabet[:rotor3]

    decrypted_text = []
    for letter in text.upper():
        if letter in alphabet:
            index = alphabet.index(letter)
            index = r3.index(alphabet[index])
            index = r2.index(alphabet[index])
            index = r1.index(alphabet[index])
            decrypted_text.append(mapping[alphabet[index]])
        else:
            decrypted_text.append(letter)

        r1 = r1[1:] + r1[:1]
        if alphabet.index(r1[0]) == rotor1:
            r2 = r2[1:] + r2[:1]
        if alphabet.index(r2[0]) == rotor2:
            r3 = r3[1:] + r3[:1]

    return ''.join(decrypted_text)

if (select := input('en/de? ')) == 'en':
    firsts = int(input(' 1: '))
    seconds = int(input(' 2: '))
    thirds = int(input(' 3: '))
    enigma_text = enigma(input('text... '), rotor1=firsts, rotor2=seconds, rotor3=thirds)
    print('  ' + enigma_text)
elif select == 'de':
    firsts = int(input('1: '))
    seconds = int(input('2: '))
    thirds = int(input('3: '))
    decrypted_text = decrypt_enigma(input('code... '), rotor1=firsts, rotor2=seconds, rotor3=thirds)
    print('  ' + decrypted_text.lower())
else:
    print('nothing.')
