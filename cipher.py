"""
Decrypt a path through a Union Route Cipher.

Designed for whole-word transposition ciphers with variable rows and columns. 
Assumes encryption began at either top or bottom of a column. 
Key indicates the order to read columns and teh direction to traverse.
Negative column numbers mean start at bottom and read up.
Positive column numbers mean start at top & read down.

Example below is for 4x4 matrix with key -1 2 -3 4.
Note "0" is not allowed.
Arrows show encryption route; for negative key values read UP.

    1   2   3   4
"""
import sys

#==========================================================================================================================
# USER INPUT

# the string to be decrypted: = 
# ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
# ciphertext ="REST TRANSPORT YOU GODWIN VILLAGE ROANOKE WITH ARE YOUR IS JUST SUPPLIES FREE SNOW HEADING TO GONE TO SOUTH FILLER"
ciphertext = "THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDENTS OF AT WHY AND IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEM CAN UP"

#initialize variables
COLS = 4
ROWS = 6
key = '-1 2 -3 4' #neg number means read UP column

# END OF USER INPUT - DO NOT EDIT BELOW!
#==========================================================================================================================

def main():
    """Run program and print decrypted plaintext."""
    print("\nCiphertext = {}".format(ciphertext))
    print("Trying {} columns".format(COLS))
    print("Trying {} rows".format(ROWS))
    print("Trying key = {}".format(key))
    # split elements into words, not letters
    cipherlist = list(ciphertext.split())
    validate_col_row(cipherlist)
    key_int = key_to_int(key)
    translation_matrix = build_matrix(key_int,cipherlist)
    plaintext = decrypt(translation_matrix)

    print("Plaintext = {}".format(plaintext))

def validate_col_row(cipherlist):
    """Check that input columns & rows are valid vs. message length."""
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher): #range excludes 1-column ciphers
        if len_cipher % i == 0:
            factors.append(i)
    print("\nLength of cipher = {}".format(factors))
    print("Acceptable column/row values include {}".format(factors))
    print()
    if ROWS * COLS != len_cipher:
        print("\nError - Input columns & rows not factors of length "
        "of cipher. Terminating program.", file=sys.stderr)
        sys.exit(1)

def key_to_int(key):
    """Turn key into list of integers & check availability"""
    key_int = [int(i) for i in key.split()]
    key_int_lo = min(key_int)
    key_int_hi = max(key_int)
    if len(key_int) != COLS or key_int_lo < -COLS or key_int_hi > COLS \
        or 0 in key_int:
        print("\nError - Problem with key. Terminating program.", file=sys.stderr)
        sys.exit(1)
    else:
        return key_int

def build_matrix(key_int, cipherlist):
    """Turn every n items in a list into a new item in a list of lists"""
    translation_matrix = [None] * COLS
    start = 0
    stop = ROWS
    for k in key_int:
        if k < 0: # read bottom to top of column
            col_items = cipherlist[start:stop]
        elif k > 0: # top-to-bottom
            col_items = list((reversed(cipherlist[start:stop])))
        translation_matrix[abs(k) - 1] = col_items
        start += ROWS
        stop += ROWS
    return translation_matrix

def decrypt(translation_matrix):
    """Loop through nested lists popping off last item into string"""
    plaintext = ""
    for i in range(ROWS):
        for matrix_col in translation_matrix:
            word = str(matrix_col.pop())
            plaintext += word + " "
    return plaintext

if __name__ == '__main__':
    main()