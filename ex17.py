from sys import argv
from os.path import exists

from_file = 'test.txt'
to_file = 'new_test.txt'

print(f'Copying from {from_file} to {to_file}')

indata = open(from_file).read()
#could be done in two steps - in_file = open(from_file); indata = in_file.read()

print(f'The input file is {len(indata)} bytes long')

print(f'Does the output file exist? {exists(to_file)}')
print('Ok, hit RET to continue, Ctrl-C to abort.')
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print('Alright, all done.')

out_file.close()
#in_file.close()
