
def caesarCipher(s, k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotate = k%len(alphabet)

    new_alphabet = alphabet[rotate:] + alphabet[:rotate]
    alphabet_dic = {}

    for old, new in zip(alphabet, new_alphabet) : 
        alphabet_dic[old] = new

    final = []
    for letter in s:
        if letter.isupper() :
            final.append( alphabet_dic[letter.lower()].upper()  )
            
        elif letter not in alphabet_dic.keys():
            print(letter)
            final.append(letter)
        else :
            final.append(alphabet_dic[letter])

    return ''.join(final) 



        