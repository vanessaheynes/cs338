# Vanessa Heynes 

# ---- Diffie Hellman ----

# find values for x and y 
# for x in range(61):
#     if ((7**x) % 61) == 30:
#         print("x = " , x)
#     if ((7**x) % 61) == 17:
#         print("y = " , x)

# # find secret message 
# print("The secret message is", 7**(23*41)%61, "\n")

# ---- RSA -----

n = 170171
e = 17

# find values for p and q (p = 449, q = 379)
for i in range(412, n):
    if (n % i == 0):
        p = i
        # print(p)
q = n / p
# print(q)

# find value for d (d = 119537)
for x in range(n):
    if ((e*x) % ((p-1)*(q-1))) == 1:
        d = x
        # print(d)

# decode the message 
cipherText = [65426, 79042, 53889, 42039, 49636, 66493, 41225, 58964,
126715, 67136, 146654, 30668, 159166, 75253, 123703, 138090,
118085, 120912, 117757, 145306, 10450, 135932, 152073, 141695,
42039, 137851, 44057, 16497, 100682, 12397, 92727, 127363,
146760, 5303, 98195, 26070, 110936, 115638, 105827, 152109,
79912, 74036, 26139, 64501, 71977, 128923, 106333, 126715,
111017, 165562, 157545, 149327, 60143, 117253, 21997, 135322,
19408, 36348, 103851, 139973, 35671, 93761, 11423, 41336,
36348, 41336, 156366, 140818, 156366, 93166, 128570, 19681,
26139, 39292, 114290, 19681, 149668, 70117, 163780, 73933,
154421, 156366, 126548, 87726, 41418, 87726, 3486, 151413,
26421, 99611, 157545, 101582, 100345, 60758, 92790, 13012,
100704, 107995]

decryptedBlocks = []
for c in cipherText:
    x = (c**d) % n
    decryptedBlocks.append(x)

# sources
# https://www.datacamp.com/tutorial/python-data-type-conversion
# https://www.geeksforgeeks.org/python-program-to-convert-binary-to-ascii/

secretMessage = ""
for m in decryptedBlocks:
    bin_m = bin(m)
    binary_int = int(bin_m, 2)
    byte_number = binary_int.bit_length() + 7
    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii = binary_array.decode()
    secretMessage = secretMessage + ascii

print(secretMessage)