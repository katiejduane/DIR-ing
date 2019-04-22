
alphabet = "abcdefghijklmnopqrstuvwxyz"

rotate_by = 13  # We're doing ROT 13

# Create a variable with an empty string that we'll add decoded letters to.
uncoded_message = "horse"
coded_message = ""
i = 0
while i < len(uncoded_message):
    letter = uncoded_message[i]
    i = i + 1
    if letter in alphabet:
        index_in_alphabet = alphabet.index(letter)
        new_index = index_in_alphabet + rotate_by
        if new_index >= len(alphabet):
            new_index = new_index - len(alphabet)
        coded_message = coded_message + alphabet[new_index]

print(coded_message)



# thePassword = str(1234)


# def crack_password(password):
#     passwd = list(thePassword)
#     for i in range(0, 10):
#         for j in range(0, 10):
#             for k in range(0, 10):
#                 for l in range(0, 10):
#                     if str(i) == passwd[0] and str(j) == passwd[1] and str(k) == passwd[2] and str(l) == passwd[3]:
#                         mylist = [str(i), str(j), str(k), str(l)]
#                         code = "".join(mylist)
#                         #print mylist
#                         #print code
#     print("Four Digit Password: {}".format(code))


# crack_password(1234)
