"""
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
text="The Lord Chamberlain walked busily among the courtiers assembled in the main hall, fussing about the arrangements, making sure that everyone was in his or her place.";
chars=[char for char in text]

rules=[{"offset":3,"length":10,"style":'RED'},3-10
       {"offset":5 ,"length":2,"style":'GREEN'} 5-7
       ]



print(rules)

result=[
    {"chars":"The","styles":[]},
    # {"chars":" Lord Cham","styles":['RED']} incorrect
    {"chars": " L", "styles": ['RED']},
    {"chars": "or", "styles": ['RED',"GREEN"]},  ## IMPORTANT!!!!
    {"chars": "d Cham", "styles": ['RED']},
    {"chars": "dberlain walked busily among the courtiers assembled in the main hall, fussing about the arrangements, making sure that everyone was in his or her place.", "styles": []},
]
"""
def numberBack (element):
    return element["numbers"]



def generalStyle(*color):
# def generalStyle(color1,color2):
    result = x.intersection(*color)
    generalStyle = [value for value in color[0] if value in color[1]]
    return generalStyle

text="The Lord Chamberlain walked busily among the courtiers"
# chars=[char for char in text]
chars=[i for i in range(1,len(text))]
print(chars)
CharsProperties=[
    {"offset":2,"length":8,"style":'GREEN'},
    {"offset":3,"length":4,"style":'RED'},
    {"offset":1,"length":4,"style":'BLUE'}
]

rulesList=[]
for rule in CharsProperties:
    baseArray=[i for i in range(rule['offset'],rule['offset']+rule["length"])]
    rule["numbers"]=set(baseArray)



# allRules
for idx, chr in enumerate(CharsProperties):
    nextIter=CharsProperties.copy()
    for i in range(0,idx):
        nextIter.pop()
    _rule=list(map(lambda x: x['style'],nextIter))
    allRules=list(map(lambda x: x["numbers"],nextIter))
    finalResult=set.intersection(*allRules)
    dif = set.difference(*allRules)
    print(_rule,finalResult,dif)



# for i in allRules:
#     print(i)
# # # print(allRules)
# finalResult=set.intersection(*allRules)
# print(finalResult)
# for rule in CharsProperties:
    # print(rule["numbers"])
    # set.intersection(*rule)


# for rule in CharsProperties:



exit(1)


greenChars=(chars[(CharsProperties[0].get("offset")):((CharsProperties[0].get("offset"))+((CharsProperties[1].get("length"))))])
redChars=(chars[(CharsProperties[3].get("offset")):((CharsProperties[3].get("offset"))+((CharsProperties[4].get("length"))))])
result={"characters":(chars)}
print(redChars)
print(greenChars)
print(generalStyle(greenChars,redChars))
# generalStyle=(stylesSeparator(redChars,greenChars))
greenChars="".join(greenChars)
redChars="".join(redChars)
startChars="".join(chars[0:CharsProperties[0].get("offset")])
unityStyle="".join(generalStyle(greenChars,redChars))

result=[{"chars":startChars,"from":3,"to":10,"style":"None"},
        {"chars":greenChars,"style":CharsProperties[2].get("style")},
        {"chars":redChars,"style":CharsProperties[5].get("style")},
        # {"chars":chars[((CharsProperties[3].get("offset"))+((CharsProperties[4].get("length")))):-1:1],"style":"None"}
        ]
print(result)
