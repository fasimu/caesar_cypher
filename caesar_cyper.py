"""
The Caesar cipher (or Caesar code ) is a monoalphabetic substitution cipher,
where each letter is replaced by another letter located a little further in the alphabet
(it shifted but always the same for given cipher message). 
"""

# decoding caesar cyper
def caesar_decode(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoded_message = ""
    for letter in message:
        if letter in alphabet:
            new_index = (alphabet.find(letter) + offset) % len(alphabet)
            new_letter = alphabet[new_index]
            decoded_message += new_letter
        else:
            decoded_message += letter
    return decoded_message

# encoding caesar cyper
def caesar_encode(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded_message = ""
    for letter in message:
        if letter in alphabet:
            new_index = (alphabet.find(letter) - offset) % len(alphabet)
            new_letter = alphabet[new_index]
            encoded_message += new_letter
        else:
            encoded_message += letter
    return encoded_message

""" example 

message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
print(caesar_decode(message, 10))
message_1 = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
print(caesar_decode(message_1, 10))
message_2 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
print(caesar_decode(message_2, 14))

message_3 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
for i in range(7,8):
  print(caesar_decode(message_3, i))

msg = caesar_decode(message, 10)
print(caesar_encode(msg, 10))
"""
