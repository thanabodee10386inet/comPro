filename = input('Enter a filename: ')
try:
    infile = open(filename, 'r')
    contents = infile.read()
    print(contents)
    infile.close()
except IOError:
    print('')
    print(', filename')

print("End of program")

#run > x.py