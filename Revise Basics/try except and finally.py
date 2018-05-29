try:
    myfile= open("notAvelable.txt")
    for i in myfile:
        print(i, end="")
    myfile.close()   
# try to execute this program

except:
    print("file not found") #if try fails do this

finally: print("exiting now") #must happen either try works or not
