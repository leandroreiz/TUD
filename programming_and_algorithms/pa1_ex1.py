# get user input
incoming_int_as_string = input("Enter an integer to convert: ")

# validate information entered by user
if incoming_int_as_string.isnumeric():
    incoming_int = int(incoming_int_as_string)
else:
    print(f"{incoming_int_as_string} is not a number, quitting...")
    quit(1)

if incoming_int < 0:
    print(f"Value {incoming_int} cannot be processed, so I'm quitting...")
    quit(1)
else:
    print(f"{incoming_int} is a valid number, proceeding to conversion...")

binary_string = ''

while incoming_int > 0:
    remainder = incoming_int % 2                    # '%' is 'modulus', returns the remainder of a division
    incoming_int = incoming_int // 2                # '//' is 'integer' division, i.e. yields a whole number only
    binary_string = str(remainder) + binary_string  # convert and add the remainder at the beginning of the string

print(f"Result: {binary_string}")
