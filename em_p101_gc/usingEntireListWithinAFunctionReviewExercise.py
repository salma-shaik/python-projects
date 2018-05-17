intList=[2,234,1233,656]

def printElem(li):
    for elem in li:
        print(elem)

rangeList1=[0,1,2]
rangeList2=[2,3,4]
rangeList3=[2,7,12]

def sumOfThreeLists(li1,li2,li3):

    resList=[]
    newElem=0
    for elemIndex in range(3):
        newElem=li1[elemIndex]+li2[elemIndex]+li3[elemIndex]
        resList.append(newElem)
    return resList

print(sumOfThreeLists(rangeList1,rangeList2,rangeList3))


def printNestedLists(li):
    for eachList in li:
        for eachElem in eachList:
            print(eachElem)

printNestedLists([[1,2],[0,1],[3,4]])

printElem(intList)