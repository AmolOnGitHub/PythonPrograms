import math
    
students = [
"HAFIZAA ALVEENAA B - G",
"MARY ANNE AMITHA - G",
"SUBALAKSHMI B - G",
"ANTON BENY M S - B",
"SANJIT CHOUDHARY - B",
"VEER DARSHAK KOTHARI - B",
"GRACE JACINTHA MERCY - G",
"SANGAMITHRA K S - G",
"PRANAV KARTHIK - B",
"TAMANNA KAUR - G",
"VAIBHAV KOTHARI - B",
"THEERTH KRISH S - B",
"SUDEEP M KANNAN - B",
"VISHAL M - B",
"JACOB MAXIMUS A - B",
"SHRISHAA MEENAA R K - G",
"ARMAAN MEHTA - B",
"SOWDHANYA NAKSHATHRA M - G",
"LIYAN NAZEER - B",
"KEERTHI P - G",
"KAVI PRASATH M P - B",
"AMOL VIJAYACHANDRAN - B",
"JANANI R - G",
"MADHUMITHA R - G",
"CYNTHIA ROSELINE ROZARIO - G",
"ASHWIN S - B",
"DHITSITHAA S - G",
"GAURAVKUMAR S - B",
"HARISHWA S - B",
"NISHANT S JAIN - B",
"PRAGYA S - G",
"SUDHARSANA SARAVANAN S - B",
"AKSHAYA SRI D - G",
"HARINDERAN T - B",
"JAISHREE V P - G" 
]

print("Strength:" ,len(students))

students.sort()

print("How would you like to sort:")
print("Alphabetical or Roll Number")
choice = input().strip().lower()
print("How many students in each batch? (15 - 18)")
no = int(input())

if not (choice == "roll number" or choice == "alphabetical"): 
    quit()
if not (no >= 15 and no <= 18):
    quit()

if(choice == "roll number"):
    girls = []
    boys = []
    for name in students:
        if " - G" in name:
            girls.append(name)
        if " - B" in name:
            boys.append(name)

    students = girls + boys

outer = 1
length = len(students)
while outer <= math.ceil(length / no):
    i = 0
    while i < no:
        name = students[0]
        name = name[0: len(name) - 4]
        print(name)
        i += 1
        students.pop(0)
        if(len(students) == 0):
            break
    outer += 1
    print()
