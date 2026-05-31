def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char  # spaces and symbols stay same
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# ---- Main Program ----
print("=== Caesar Cipher Tool ===")
print("(DecodeLabs - Cyber Security Project 2)")
print("-" * 40)

message = input("\nEnter your message: ")
shift = int(input("Enter shift number (example: 3): "))

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print("\n--- RESULTS ---")
print(f"Original Message:  {message}")
print(f"Encrypted Message: {encrypted}")
print(f"Decrypted Message: {decrypted}")

if message == decrypted:
    print("\n Encryption and Decryption working perfectly!")
else:
    print("\n Something went wrong!")