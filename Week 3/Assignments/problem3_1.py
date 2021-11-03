
def problem3_1(txtfilename):
    f = open(txtfilename)
    count = 0
    for line in f:
        count += len(line)
        print(line, end='')

    print(f'\n\nThere are {sum} letters in the file')
