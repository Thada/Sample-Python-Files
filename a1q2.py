#!/usr/bin/python
#Thomas Hada, ID 107758936

#This program decodes a given encrypted English text, using given hints:
# Letter 'k' is encrypted to 'n', letter 'r' is encrypted to 'u', and letter
#  'x' is encrypted to 'a'.
# Punctuation marks are not encrypted.

#Initialize variables:
message = "fjxdfkb qebob'p kl zlrkqofbp fq fpk'q exoa ql al klqefkd ql hfii lo afb clo xka kl obifdflk qll fjxdfkb xii qeb mblmib ifsfkd ifcb fk mbxzb vlr jxv pxv qexq F'j x aobxjbo yrq F'j klq qeb lkiv lkb f elmb pljbaxv vlr'ii glfk rp xka qeb tloia tfii yb xp lkb"
list(message)
trans  = []
final = ""

#A loop that will convert all elements in 'message' to ASCII values, then adds
# +3 to all letter ASCII values. Includes special cases x > a, y > b, z > c.
for letter in message:
    if ord(letter) > 96 and ord(letter) < 123:
        trans.append(ord(letter) + 3)
        if trans[len(trans) - 1] == 123:
            trans.pop()
            trans.append(97)
        elif trans[len(trans) - 1] == 124:
            trans.pop()
            trans.append(98)
        elif trans[len(trans) - 1] == 125:
            trans.pop()
            trans.append(99)
    elif ord(letter) > 64 and ord(letter) < 91:
        trans.append(ord(letter) + 3)
    else:
        trans.append(ord(letter))

#Puts each value in 'trans' into a new, string variable:
for letter in trans:
    final = final + chr(letter)

#Prints out the decrypted message:
print final
