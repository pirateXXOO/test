# Author:Jack
# Date:2018/5/19

# a='123'
# b="123"
#
#
# print(type(a))

a="Let's go"
print(a)


b=a*2
print(b)

print('helloworld'[2:])

print("el" in "helloworld")


print('123' in '1234')


print('%s is a good teacher'%a)

a='123'
b='abc'
print(a+b)

c=a.join(b)
print(c)

print(''.join([a,b]))

print('***'.join([a,b]))

# String 的内置方法

st='hello kitty!'
print(st.count('l'))
print(st.capitalize())
print(st.center(30,'#'))
print(st.endswith('!'))
print(st.startswith('h'))
st='string\tshell 123 {name}is {age}'
print(st.expandtabs(tabsize=10))
print(st.find('t'))
print(st.format(name='alex',age=37))
print(st.format_map({'name':'alex','age':33}))
print(st.index('t'))
print(st.find('qqq'))
print(st.isalnum())
print('shelll'.isalnum())
print('124'.isalnum())
print('123'.isalpha())
print('0102'.isdecimal())
print('3993'.isdigit())
print('skldjf'.isdigit())
print('234.323'.isdigit())
print('slkdjfi'.islower())
print('123'.isnumeric())
print('23.skdjf'.isidentifier())
print('lskdjfi'.islower())
print('LKSDJ'.isupper())
print('  '.isspace())
print('My Title To You'.istitle())
print('IOKJIksdjifj'.lower())
print('lkjsidf'.upper())
print('ksjdifIIJIJ'.swapcase())
print('lskdjfi'.ljust(10,'*'))
print('lskdjfi'.rjust(10,'*'))
print('   shell Coonfig    '.strip())
print('lskdjfie'.strip())
print('lksdjif \n '.strip())
print('config .ssoiejf'.upper())
print(' lskdjfie'.lstrip())
print('  lskdjfij    '.rstrip())
print('lskdjfiej'.replace('ej','shell'))
print('My title title '.replace('title','find'))
print('My title title'.rfind('l'))
print('My title title '.split('i'))
print('which lskdjfie'.rsplit('i',2))
print('sldkfjie'.title())

# importment
print(st.count())
st.startswith()
st.find()
st.format()
st.center()
st.upper()
st.lower()
st.strip()
st.split()
t.replace()
