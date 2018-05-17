strList=["test1","abc","end"]

def oneInput(li):
    print(li[1]) #abc
    print(li[2]+"frog") #endfrog
    li.remove(li[0]) # removes test1
    print(li)   # abc,end

oneInput(strList)