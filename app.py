#
# Created By Hamed Sadeghzadeh
# 1401/10/06
# 27-12-2022
#
# This App Is For Calculating CYK Algorithm
# In This App We Are Using `collections` Library To Make Lists Or Sets Collection
# Steps:
# 1. Make Grammar:
#   1.1. Get Variables From User
#   1.2. Get Rules Of Each Variable
# 2. Define CYN Function:
#   2.1. Make CYK Table
#   2.2. Return CYK Table
# 3. Get String From User To Check If It Can Be Created Using This Algorithm
# 4. Search For String's Value To Be 'S' In CYK Table
#
# Libraries
from collections import defaultdict

# The User Gives The Set Of Variables, The First One Is 'S'
variables = []
for x in range(int(input("Enter number of variables: "))):
    variables.append(input("Var[" + str(x) + "] in UPPERCASE: ")[0])

# The Terminals Are All The Characters That Are Not Variables
rules = defaultdict(list)
for x in (variables):
    rules_var = []
    for y in range(int(input("Number of rules for " + x + ": "))):
        rules_var.append(input(x + " = "))
    rules[x] = rules_var


def cykFun(substr, rules, cyk, x):
    res = set()
    for z in range(x-1):
        var1 = cyk[substr[:z+1]]
        var2 = cyk[substr[z+1:]]
        for var in [x+y for x in var1 for y in var2]:
            for key in rules:
                if var in rules[key]:
                    res.add(key)
    cyk[substr] = res
    return cyk


cyk = defaultdict(set)
string = input("Enter a string: ")
for x in range(1, len(string)+1):
    for y in range(len(string)+1-x):
        substr = (string[y:y+x])
        if x == 1:
            for key in rules:
                if substr in rules[key]:
                    cyk[substr].add(key)
        else:
            cyk = cykFun(substr, rules, cyk, x)


# Check Availability
def checkAvailable():
    if cyk[string]:
        for ob in cyk[string]:
            if ob == variables[0]:
                return True
    return False


if checkAvailable():
    print("String Can Be Created With This Grammar. :)")
else:
    print("String Can Not Be Created With This Grammar. :(")
