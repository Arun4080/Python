try:
    a=[1,2,3,4,5,6] #data to store in file
    newFile= open("self_Created_file.txt",'w') #open file in write mode if it exist then it will be open if not it will be created
    print(a,file=newFile) #Saving data using print command
    
except:
    print('File error')

finally:
    newFile.close() #must close even crash occur in after opening file
