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
    

    

if __name__ == "__main__":
    print(cipher_atbash("ABC"))




