from collections import defaultdict

# The user gives the set of variables, the first one is S
variables = []
for x in range(int(input("Enter number of variables: "))):
    variables.append(input("Var[" + str(x) + "] in UPPERCASE: ")[0])

# The user gives the set of rules
# The terminals are all the characters that are not variables
rules = defaultdict(list)
for x in (variables):
    rules_var = []
    for y in range(int(input("Number of rules for " + x + ": "))):
        rules_var.append(input(x + " = "))
    rules[x] = rules_var

# We start at S and with an empty word
# word = cfg('S', rules, variables, '')


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


# Check availability
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
