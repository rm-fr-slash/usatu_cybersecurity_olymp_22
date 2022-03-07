new_msg = ''
with open('послание.txt', 'r') as f:
    msg = f.read()
    for symb in msg:
        new_msg += (str((ord(symb) + 13371337) * 13371337) + ' ')
with open('послание.txt', 'w') as f:
    f.write(new_msg)