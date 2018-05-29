import pickle
#pickle is an unreadable file so data is save untill it will not loaded using pickle.load

with open('mydata.pickle','wb') as mysavedata:
    pickle.dump([1,2,'three'], mysavedata)

with open('mydata.pickle','rb') as myrestoredata:
    list=pickle.load(myrestoredata)

print(list)
