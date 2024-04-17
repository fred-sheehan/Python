Exceptions and Errors handling

try:
    file = open('file.txt') # doesn't exist
    a_dictionary = {'key': 'value'}
    print(a_dictionary['mumbo_jumbo'])
except FileNotFoundError:
    file = open('file.txt', 'w') # will create it
    file.write('Hello World')
except KeyError as error_message:
    print(f'The Key {error_message} not found')
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print('File was closed')
    raise TypeError('This is an error that I made up') # will raise an error

height = float(input('Height: '))
weight = int(input('Weight: '))

if height > 3:
    raise ValueError('Height should be less than 3 meters')

bmi = weight / height ** 2
print(bmi)
