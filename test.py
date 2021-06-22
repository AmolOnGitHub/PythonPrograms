f = open("pylintDisable.txt", "r")
text = f.read().strip()
first = text[0]
last = text[-1]
print(f"{first} {last}")