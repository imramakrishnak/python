# Defining a String Variable

message1 = 'Hello World'
print(message1)

message2 = "Ramki's World"
print(message2)

message3 = 'Ramki\'s World'
print(message3)

paragraph = '''
This is a multiline
string example.
'''
print(paragraph)

# String Functions
print(len(message1))

print(message1[0])
print(message1[0:5])
print(message1[:5])
print(message1[6:])

print(message1.lower())
print(message1.upper())

print(message1.count('l'))

print(message1.find('l'))

print(message1.replace('l', '1'))
