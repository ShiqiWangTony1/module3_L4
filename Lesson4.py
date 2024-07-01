import re

def check_names(names):
    pattern = re.compile(r'^[A-Z][a-z]*([ ][A-Z][a-z]*)*$')
    
    for name in names:
        if pattern.match(name):
            print(name)
        else:
            print("Invalid name")

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", 
         "Connor Milliken", "Jordan Alexander Williams", "Madonna", 
         "programming is cool"]
check_names(names)
