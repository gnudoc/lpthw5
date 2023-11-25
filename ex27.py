# get byte-code for a snippet of python code
from dis import dis

dis('''
x = 10
y = 20
z = x + y
''')
