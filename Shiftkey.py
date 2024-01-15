# Define function to decrypt a ciphertext
def decrypt(ciphertext, shift):
    decrypted_text = "" # Initialize decrypted text as empty string
    for char in ciphertext: # Iterate through each character in the ciphertext
        if char.isalpha(): # Check if the character is a letter
            ascii_offset = ord('A') if char.isupper() else ord('a') # Calculate ASCII offset for uppercase or lowercase letters
            decrypted_text += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset) # Decrypt the character using Caesar cipher formula and ASCII offset
        else: # If the character is not a letter
            decrypted_text += char # Append the character to the decrypted text without decryption
    return decrypted_text # Return the decrypted text

def find_shift_key(ciphertext):
    for shift in range(26): # Iterate through each possible shift key (from 0 to 25)
        decrypted_text = decrypt(ciphertext, shift) # Decrypt the ciphertext using the current shift key
        print(f"Shift {shift}: {decrypted_text}") # Print the shift key and the decrypted text

# Example cryptogram
cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"

find_shift_key(cryptogram) # Call the function to find the shift key for the example cryptogram