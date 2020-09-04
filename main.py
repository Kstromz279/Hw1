# Author: Khalil Stroman kzs5955@psu.edu
gp1 = input("Enter your course 1 letter grade: ")
if gp1 == "A":
 gp1 = 4.0
elif gp1 == "A-":
  gp1 = 3.67
elif gp1 == "B+":
  gp1 = 3.33
elif gp1 == "B":
  gp1 = 3.0
elif gp1 == "B-":
  gp1 = 2.67
elif gp1 == "C+":
  gp1 = 2.33
elif gp1 == "C":
  gp1 = 2.0
elif gp1 == "D":
  gp1 = 1.0
else :
  gp1 = 0.0 
credit1 = input("Enter your course 1 credit: ")
print(f"Grade point for course 1 is: {gp1}")
credit1 = float(credit1)
gp2 = input("Enter your course 2 letter grade: ")
if gp2 == "A":
 gp2 = 4.0
elif gp2 == "A-":
  gp2 = 3.67
elif gp2 == "B+":
  gp2 = 3.33
elif gp2 == "B":
  gp2 = 3.0
elif gp2 == "B-":
  gp2 = 2.67
elif gp2 == "C+":
  gp2 = 2.33
elif gp2 == "C":
  gp2 = 2.0
  print(f"Grade point for course 2 is: {gp2}")
elif gp2 == "D":
  gp2 = 1.0
else :
  gp2 = 0.0
credit2 = input("Enter your course 2 credit: ")
print(f"Grade point for course 2 is: {gp2}")
credit2 = float(credit2)
gp3 = input("Enter your course 3 letter grade: ")
if gp3 == "A":
 gp3 = 4.0
elif gp3 == "A-":
  gp3 = 3.67
elif gp3 == "B+":
  gp3 = 3.33
elif gp3 == "B":
  gp3 = 3.0
elif gp3 == "B-":
  gp3 = 2.67
elif gp3 == "C+":
  gp3 = 2.33
elif gp3 == "C":
  gp3 = 2.0
elif gp3 == "D":
  gp3 = 1.0
else :
  gp3 = 0.0
credit3 = input("Enter your course 3 credit: ")
print(f"Grade point for course 3 is: {gp3}")
credit3 = float(credit3)
GPA = ((gp1*credit1)+(gp2*credit2)+(gp3*credit3))/(credit1+credit2+credit3)
print(f"Your GPA is: {GPA}")