#read a file and handle errors

try:
    file = open('sample.txt', 'r+')
    writing_file = file.write('Line 1: This is a sample text file.\nLine 2: It contains multiple lines.')
    print('Reading file content:')
    file.close()

    file = open('sample.txt', 'r+')
    reading_file = file.read()
    print(reading_file)
    file.close()

except FileNotFoundError:
    print(f'Error: The file {'sample.txt'} was not found.')

