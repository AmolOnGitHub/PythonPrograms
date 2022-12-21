import string

ORDER = "()*/+- "

class node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

def leastpriority(st):
    char = ''
    strength = 0
    index = -1
    paran = False
    for i in range(len(st)):
        c = st[i]
        if c == ' ': continue
        if c == '(': paran = True
        if c == ')':
            paran = False
            continue
        if paran: continue

        if c in ORDER:
            if index == -1: 
                char = c
                strength = ORDER.index(str(c))
                index = i

            if ORDER.index(str(c)) > strength:
                char = c
                strength = ORDER.index(str(c))
                if strength % 2 == 1: strength -= 1
                index = i
        
    return(char, index)
   
ins = input()
evalexp = ""

# To check for validity of expression

#for item in ins.split(" "):
#    if len(item) > 1:
#        print("Seperate each term with a space")
#        quit()
       
for c in ins.lower():
    if c in list(string.ascii_lowercase):
        evalexp += str(1)
    elif c not in ORDER:
        print("Invalid symbol")
        quit()
    else: evalexp += c

try:
    i = eval(evalexp)
except SyntaxError:
    print("Syntax Error")
    quit()
except ZeroDivisionError:
    pass

# Code is valid if reached till here

exp = ins
lp = leastpriority(exp)
root = node(lp[0])
expl = exp[:lp[1]].strip()
expr = exp[lp[1]+1:].strip()

left = node(expl)
right = node(expr)
root.left = left
root.right = right
temp = root

while len(temp.left.data) > 1 and len(temp.right.data) > 1:
    lp = leastpriority(left.data)

print(expl)
print(expr)