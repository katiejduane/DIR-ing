# secret_message = "ubefr"

def de_cipher(coded_message):
    i = 0
    decoded_message = ""
    rotate_by = 13  
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while i < len(coded_message):
        letter = coded_message[i]
        i = i + 1
        if letter in alphabet:
            index_in_alphabet = alphabet.index(letter)
            new_index = index_in_alphabet + rotate_by
            if new_index >= len(alphabet):
                new_index = new_index - len(alphabet)
            decoded_message = decoded_message + alphabet[new_index]
    return decoded_message

# print(de_cipher(de_cipher(secret_message)))


thePassword = de_cipher('ubefr')

def crack_password(password):
    password_guess = input('guess my password: ')
    i = 0
    for char in password_guess:
        coded = de_cipher(char)
        if coded == password[i]:
            print(f"you guessed {char} correctly!")
            i += 1
        else: 
            print("try again!")
            i += 1


crack_password(thePassword)

# assignment: it takes a string (user input, letters only), we're going to have a hash
# that reps the caesar cipher. for every char in the string, run a caeser cipher
# function to see if that matches the hashed password
