import hashlib

input = 'bgvyzdsv'

key = 0
while 1:
    test_key = input + str(key)
    hash = hashlib.md5(test_key.encode()).hexdigest()

    if hash[:5] != '00000':
        key += 1
    else:
        break

print(f'Part 1 : {key}')

key = 0
while 1:
    test_key = input + str(key)
    hash = hashlib.md5(test_key.encode()).hexdigest()

    if hash[:6] != '000000':
        key += 1
    else:
        break

print(f'Part 2 : {key}')