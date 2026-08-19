import string

def cipher_caesar(text: str, offset: int=3) -> str:
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase

    alphabet_offset_lower = alphabet_lower [offset:] + alphabet_lower [:offset]
    alphabet_offset_upper = alphabet_upper [offset:] + alphabet_upper [:offset]

    translation_table = str.maketrans(
            alphabet_lower + alphabet_upper, 
            alphabet_offset_lower + alphabet_offset_upper
            )
    return text.translate(translation_table)

#Custom offset in caesar cipher. To decrypt you can pass the negative value of 'offset' (knowing what the value is)
# The mathematical formula would be e(x) = (x + k). K is the shift (offset) applied to each letter. X is the character we are encrypting
# Basically : if the letter A = 1, A + k(3) = 4. The fourth letter of the alphabet is D.
# e(x) = (x - k) to decrypt.


if __name__ == "__main__" :
    


    print(cipher_caesar("CHICO", offset=1))
    print(cipher_caesar("chico", offset=5))
    print(cipher_caesar("CHICO", offset=10))
    print(cipher_caesar("chico", offset=25))
    print(cipher_caesar("dijdp", offset=-1))

