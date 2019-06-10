#Example 3: How iter() works for callable objects with sentinel?


def processLine(line) :
    print (line)


filename = 'mydata.txt'

with open(filename) as fp:
    for line in iter(fp.readline, sentinel=''):
        processLine(line)

#When you run the program, it will open mydata.txt in read mode.

#Then, the iter(fp.readline, '') in the for loop calls readline (which reads each line in the text file)
# until the sentinel character '' (empty string) is reached.

