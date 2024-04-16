# Caesar Cipher
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result += shifted_char
        else:
            result += char
    return result

# Playfair Cipher
def create_playfair_matrix(key):
    # Create a 5x5 matrix from the key (excluding 'J')
    # Fill in the rest of the alphabet
    pass

def playfair_encrypt(plaintext, key_matrix):
    # Implement the encryption logic
    pass

# Morse Code
def text_to_morse(text):
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.',  # ... (complete dictionary)
    }
    morse_text = ""
    for char in text.upper():
        if char in morse_dict:
            morse_text += morse_dict[char] + " "
        else:
            morse_text += char + " "
    return morse_text.strip()

# Hill Cipher
import numpy as np

def generate_key_matrix(key):
    # Create a key matrix (3x3 or 2x2)
    pass

def hill_encrypt(plaintext, key_matrix):
    # Implement the encryption logic
    pass

# Example usage
if __name__ == "__main__":
    plaintext = "HELLO"
    shift_value = 3
    caesar_ciphertext = caesar_cipher(plaintext, shift_value)
    print(f"Caesar Ciphertext: {caesar_ciphertext}")

    key = "KEYWORD"
    key_matrix = create_playfair_matrix(key)
    playfair_ciphertext = playfair_encrypt(plaintext, key_matrix)
    print(f"Playfair Ciphertext: {playfair_ciphertext}")

    morse_message = text_to_morse(plaintext)
    print(f"Morse Code: {morse_message}")

    key = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
    hill_ciphertext = hill_encrypt(plaintext, key)
    print(f"Hill Ciphertext: {hill_ciphertext}")

def vigenere_encrypt(plaintext, keyword):
    result = ""
    keyword = keyword.upper()
    for i, char in enumerate(plaintext):
        if char.isalpha():
            base = ord('A')
            shift = ord(keyword[i % len(keyword)]) - base
            shifted_char = chr((ord(char.upper()) - base + shift) % 26 + base)
            result += shifted_char
        else:
            result += char
    return result

plaintext = "HELLO"
keyword = "KEYWORD"
vigenere_ciphertext = vigenere_encrypt(plaintext, keyword)
print(f"Vigenère Ciphertext: {vigenere_ciphertext}")


def rail_fence_encrypt(plaintext, num_rails):
    rails = [[] for _ in range(num_rails)]
    direction = 1
    rail_idx = 0
    for char in plaintext:
        rails[rail_idx].append(char)
        rail_idx += direction
        if rail_idx == num_rails or rail_idx == -1:
            direction *= -1
            rail_idx += 2 * direction
    ciphertext = "".join("".join(rail) for rail in rails)
    return ciphertext

plaintext = "HELLO"
num_rails = 3
rail_fence_ciphertext = rail_fence_encrypt(plaintext, num_rails)
print(f"Rail Fence Ciphertext: {rail_fence_ciphertext}")

def vernam_encrypt(plaintext, key):
    if len(plaintext) != len(key):
        raise ValueError("Plaintext and key must be of equal length")
    ciphertext = "".join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, key))
    return ciphertext

plaintext = "HELLO"
key = "RANDOMKEY"  # Must be truly random and as long as the plaintext
vernam_ciphertext = vernam_encrypt(plaintext, key)
print(f"Vernam Ciphertext: {vernam_ciphertext}")

# Install the 'blowfish' package (if not already installed)
# pip install blowfish

import blowfish

def encrypt_blowfish(plaintext, key):
    cipher = blowfish.Cipher(key.encode())
    ciphertext = cipher.encrypt(plaintext.encode())
    return ciphertext.hex()

def decrypt_blowfish(ciphertext, key):
    cipher = blowfish.Cipher(key.encode())
    plaintext = cipher.decrypt(bytes.fromhex(ciphertext)).decode()
    return plaintext

# Example usage
plaintext = "HELLO"
key = "SECRETKEY"

blowfish_ciphertext = encrypt_blowfish(plaintext, key)
print(f"Blowfish Ciphertext: {blowfish_ciphertext}")

blowfish_decrypted = decrypt_blowfish(blowfish_ciphertext, key)
print(f"Decrypted Text: {blowfish_decrypted}")

def create_polybius_square():
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # No 'J' in the square
    polybius_square = [list(alphabet[i:i + 5]) for i in range(0, 25, 5)]
    return polybius_square

def polybius_cipher(plaintext):
    polybius_square = create_polybius_square()
    ciphertext = ""
    for char in plaintext.upper():
        if char == "J":
            char = "I"
        for row, row_letters in enumerate(polybius_square):
            if char in row_letters:
                col = row_letters.index(char)
                ciphertext += f"{row + 1}{col + 1}"
                break
    return ciphertext

# Example usage
plaintext = "GEEKSFORGEEKS"
polybius_ciphertext = polybius_cipher(plaintext)
print(f"Polybius Ciphertext: {polybius_ciphertext}")
