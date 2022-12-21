from datetime import datetime 

d1 = datetime.now()
d2 = datetime.strptime("24/01/2023", "%d/%m/%Y")
d3 = datetime.strptime("03/01/2023", "%d/%m/%Y")
d4 = datetime.strptime("01/02/2023", "%d/%m/%Y")

delta1 = d2 - d1
delta2 = d3 - d1
delta3 = d4 - d1

print(f"mains: {delta1.days} days left")
print(f"pre2: {delta2.days} days left")
print(f"board: {delta3.days} days left")