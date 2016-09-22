'''
The function takes a 16 byte input and gives a 16 byte output. It uses
multiplication (*), bit-wise exclusive OR (XOR) and modulo (%) to
calculate an element of the digest based on elements of the input
message:

digest [i] = ( (129 * message[i]) XOR message[i-1]) % 256
For the first element, the value of message[-1] is 0.

(typo? should say message[0] = 1, not message[0]-1)

For example, if message[0] = 1 and message[1] = 129, then:
For digest[0]:
129*message[0] = 129
129 XOR message[-1] = 129
129 % 256 = 129
Thus digest[0] = 129.

For digest[1]:
129*message[1] = 16641
16641 XOR  message[0] = 16640
16640 % 256 = 0
Thus digest[1] = 0.

Write a function answer(digest) that takes an array of 16 integers and returns another array of 16 that correspond to the unique message that created this digest. Since each value is a single byte, the values are 0 to 255 for both message and digest.
'''
 # digest [i] = ( (129 * message[i]) XOR message[i-1]) % 256

test = [0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165]




def answer(digest):
    # create 256x256 matrix testing all possible pairings of integers, i and j, from 0 to 255
    # each digest is stored at matrix[i][j]
    matrix = [[(129 * i ^ j) % 256 for i in range(256)] for j in range(256)]
    # initate message; first element uses 0 as j by default
    message = [matrix[0].index(digest[0])]
    # iterate through digest; find list in matrix at index of previous message; index of digest[i] is next message element
    for i in range(1,len(digest)):
        message.append( matrix[message[i-1]].index(digest[i]) )
    return message

print(answer(test))


# print(matrix)
