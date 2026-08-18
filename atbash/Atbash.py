import string
from utils.text_utils import reversed_string

def cipher_atbash(text: str) -> str:
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    
    translation_table = str.maketrans(
        alphabet_lower + alphabet_upper, 
        reversed_string(alphabet_lower) + reversed_string(alphabet_upper)
     )

    return text.translate(translation_table)     

    #Atbash is self-inverse, the encryption and decryption methods are the same operation because the mapping is simmetrycal.  A - Z, B - Y, C - X, ...
    #If your input has the value CHICO, calling cipher_atbash will translate to XSRXL.
    #If your input has the value XSRXL, calling cipher_atbash will translate to CHICO

if __name__ == "__main__":
    print(cipher_atbash("CHICO"))
    print(cipher_atbash("chico"))
    print(cipher_atbash("XSRXL"))
    print(cipher_atbash("xsrxl"))




