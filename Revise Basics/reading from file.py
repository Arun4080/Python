myfile=open('example.txt') # Read file bt it should be in same directory

for each_line in myfile:
    print(each_line,end='') # print one line

myfile.seek(0) # return to the start of the file

print(myfile.readline(), end='')

myfile.close()
