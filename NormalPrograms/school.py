import math

def alpha(students, no):
    outer = 1
    i = 0
    length = len(students)
    orino = no
    while outer <= math.ceil(length / orino):
        while i < no:
            name = students[i]
            name = name[0: len(name) - 4]
            print(name)
            i += 1
        no += orino
        if(no > len(students)):
            no = len(students)
        outer += 1
        print()


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

#print("Strength:" ,len(students))
students.sort()
alpha(students, 17)