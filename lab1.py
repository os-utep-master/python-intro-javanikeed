import sys


inputf = open(sys.argv[1], 'r')
outputf = open(sys.argv[2], 'w')


print("Writing to new file...")
for line in inputf:
    outputf.write(line)

inputf.close()


