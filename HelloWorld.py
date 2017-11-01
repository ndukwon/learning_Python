# Python3

print("hello world!")

age = 36
name = 'Duk'
fullName = '''
Duk
won
Nam
"hello~"
'''

print('\n##### printing arguments #####')
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('{} was {} years old when he wrote this book'.format(name, age))
print('was {} years old when he wrote this book'.format(name, age))
# print('{} was {} years old when he wrote this book'.format(name))     IndexError: tuple index out of range
print('fullName={0}'.format(fullName))

print('\n##### printing format #####')
print('{0}'.format(1.0/3))
print('{0:.3f}'.format(1.0/3))

print('[{}]'.format("Hello!"))
print('[{0:_^15}]'.format("Hello!"))
print('[{0:^15}]'.format("Hello!"))
print('[{0:#^15}]'.format("Hello!"))
print('[{0:\'^15}]'.format("Hello!"))
print('[{0:\\^15}]'.format("Hello!"))
# print('{0:_15}'.format("Hello!"))     ValueError: Invalid format specifier

print('{name} wrote {book}'.format(name='Duk', book='note'))

print('\n##### printing escape characters #####')
# r means raw.
print('\' << This is a single quotation mark')
print(r'\' << This is a single quotation mark')
print('\\ << This is a back slash mark')
print(r'\\ << This is a back slash mark')
print('This \n is Enter')
print(r'This \n is Enter')
print('This \t is Tab')
print(r'This \t is Tab')
print('This \
is attached')
print(r'This \
is attached')

# p.42

some_list = [1, 3, 4, 5, None, 3]


for element in some_list:
    if not element:
        pass
    print("print after pass") # will print after pass

for element in some_list:
    if not element:
       continue
    print("not print after continue") # will not print after continue
