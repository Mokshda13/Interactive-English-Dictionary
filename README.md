# Interactive-English-Dictionary
This is an interactive dictionary built using python.Here the user enters the word whose meaning is to be searched.The program is made user friendly so that even if there is some spelling error,it detects the actual word and outputs its meaning.

## Here is the explanation to the code:
Import the libraries

```python
import json
from difflib import get_close_matches
```

Load the input data fron .json file:
```python
data=json.load(open(r"C:\Users\hp\Downloads\data.json"))
```
Define a function that outputs the meaning of the input word:
```python
def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
```        
For the condition when there is some spelling error use the function get_close_matches form the difflib library which gives the most probable correct word as output.If the user agrees on that word then give its meaning as output otherwise output the string "We didn't understand your entry".Here is the code to this:
```python
elif len(get_close_matches(w,data.keys()))>0 :
    yn=input("did you mean %s instead?"%get_close_matches(w,data.keys())[0])
    if yn=="Y":
        return data[get_close_matches(w,data.keys())[0]]
    elif yn=="N":
        return"the word doesn't exist.Please double check it"
    else:
        return"We didn't understand your entry"
  ```
  If the input word does't satisfy any of these conditions then print then:
  ```python
  else:
        return"the word doesn't exist.Please double check it"
  ```
  now print the output:
  ```python
  word=input("enter word:")
output=(translate(word))

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
```    
    
  
