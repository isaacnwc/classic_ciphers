import string

def cipher_rot13(text: str) -> str:
    alphabet= string.ascii_letters
    alphabet_13offset_lower= alphabet[13:26] + alphabet [:13]
    alphabet_13offset_upper = alphabet[39:] + alphabet [26:39]

    translation_table = str.maketrans(
            
            alphabet, alphabet_13offset_lower + alphabet_13offset_upper
            )
    return text.translate(translation_table)

#Rot13 is basically caesar cipher with an offset of 13.



if __name__ == "__main__" :
    print(cipher_rot13("CHICO"))
    print(cipher_rot13("chico"))
    print(cipher_rot13("PUVPB"))
    print(cipher_rot13("puvpb"))



    
    



