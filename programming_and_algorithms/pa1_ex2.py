# Encryption assignment tips & tricks
# ord('Q')        # returns 81
# ord('Q') + 12   # returns 93
# chr(93)         # returns ']'
# chr.__doc__

plain_txt = input("Enter the text to be encrypted: ")
shift = 5000
encrypted_txt = ''

for c in plain_txt:
    encrypted_txt += chr(ord(c) + shift)

print(f"Encrypted text: {encrypted_txt}")
