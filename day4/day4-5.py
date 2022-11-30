

try:
    with open('/Users/vbm/tunnel.sh', 'r') as f:
        print(f.read())
        f.write('ererer')
        print('test!')
except FileNotFoundError:
    print("File not found!")
except IOError:
    print('File cannot be written!')
finally:
    print("finaly!")

print('I am alive!!!!')
print('lalala!!!!!!')
print('))))))')
    