def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    # Loop through each character in the text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt or decrypt uppercase characters
        if char.isupper():
            if mode == 'encrypt':
                result += chr((ord(char) + shift - 65) % 26 + 65)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift - 65) % 26 + 65)
        
        # Encrypt or decrypt lowercase characters
        elif char.islower():
            if mode == 'encrypt':
                result += chr((ord(char) + shift - 97) % 26 + 97)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift - 97) % 26 + 97)
        
        # Non-alphabet characters remain the same
        else:
            result += char
    
    return result

# User inputs
message = input("Enter your message: ")
shift_value = int(input("Enter the shift value: "))
mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ")

# Encrypt or Decrypt
result = caesar_cipher(message, shift_value, mode)
print("Output:", result)