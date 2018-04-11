from random import randint

output_file = open('more_random_chars.txt', 'w')
for i in range(50000):
    p = randint(0,99)
    if p >= 25:
        r = randint(75, 100) 
    else:
        r = randint(33, 127)
    s = '{}\n'.format(chr(r))
    output_file.write(s)

output_file.close()