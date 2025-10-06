#write and append data to a file

n = str(input('Enter text to write to the file: '))
file = open('output.txt', 'w')
writing_file = file.write(n)
print('Data successfully written to output.txt')
file.close()

y = str(input('\n'+'Enter additional text to append: '))
file = open('output.txt', 'a')
append_file = file.write('\n'+ y)
print('Data successfully append.')
file.close()

file = open('output.txt', 'r')
reading_file = file.read()
print('\n'+'Final content of output.txt: ','\n'+reading_file)
file.close()
