# __Author__ __Lencof__
# README.py

README = '''
The project was made with the need to upload files to the Could.
'''

f = open('README.txt', 'w') 
f.write(README)
f.close()

# if no mode is specified,
# 'r'ead mode is assumed by default
f = open('README.txt') # name file
while True: 
    line = f.readline()
    # Zero length indicates EOF
    if len(line) == 0:
        break
    # The `line` already has a newline
    # at the end of each line
    # since it is reading from a file.
    print(line, end='')
f.close()
