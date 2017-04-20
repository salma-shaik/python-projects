emptyDict={}
emptyDict[34]=324.3432
emptyDict[32.23]="test"
emptyDict["test"]=23
print(emptyDict)
print(len(emptyDict))
print(emptyDict["test"])
emptyDict[32.23]=100
print(emptyDict[32.23])
del emptyDict[34]
print(emptyDict)
