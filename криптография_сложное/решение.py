a = bytes.fromhex('7771637677597d7a4d507d7a4d707d5f')
b = bytes.fromhex('22222222222222222222222222222222')
c = ''
for i in range(len(a)):
    c += chr(a[i] ^ b[i])
print(c)