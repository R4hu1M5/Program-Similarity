import sys

filename1 = sys.argv[1]
filename2 = sys.argv[2]

file1 = open(filename1, "r")
dotfile1 = open("pycallgraph1", "w")

found = 0
for line in file1:
    if (line[:11] == "digraph G {"):
        found += 1
    if(found > 0):
        dotfile1.write(line)

file2 = open(filename2, "r")
dotfile2 = open("pycallgraph2", "w")

found = 0
for line in file2:
    if (line[:11] == "digraph G {"):
        found += 1
    if(found > 0):
        dotfile2.write(line)
