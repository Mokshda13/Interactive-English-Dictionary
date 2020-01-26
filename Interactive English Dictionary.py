import json
from difflib import get_close_matches
data=json.load(open(r"C:\Users\hp\Downloads\data.json"))
def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0 :
        yn=input("did you mean %s instead?"%get_close_matches(w,data.keys())[0])
        if yn=="Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="N":
            return"the word doesn't exist.Please double check it"
        else:
            return"We didn't understand your entry"
    
             
             
    else:
        return"the word doesn't exist.Please double check it"
    
word=input("enter word:")
output=(translate(word))

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
        
