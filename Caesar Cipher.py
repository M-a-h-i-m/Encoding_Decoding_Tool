import art
art.banner()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(text, shift):
    result = []

    for letter in text:
        if letter not in alphabet:
            result.append(letter)
        else:
            new_index = (alphabet.index(letter) + shift) % len(alphabet)
            result.append(alphabet[new_index])

    return "".join(result)


# 🔁 Loop to continue program
while True:
    encode_decode = input("\nType 'encode' to encrypt, 'decode' to decrypt:\n").lower()
    message = input("Type your message:\n").lower()
    shift_number = int(input("Type the Shift Number:\n"))

    if encode_decode == "encode":
        print("Encoded message:", caesar(message, shift_number))

    elif encode_decode == "decode":
        print("Decoded message:", caesar(message, -shift_number))

    else:
        print("Invalid option! Please type 'encode' or 'decode'.")

    # Ask to continue
    again = input("\nDo you want to continue? (yes/no): ").lower()

    if again != "yes":
        print("Goodbye 👋")
        break
