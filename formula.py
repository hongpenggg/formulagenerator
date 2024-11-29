from tkinter import *

maths = {
    '1': '(a+b)^n = a^n + (nC1)*a^(n-1)*b^1 + (nC2)*a^(n-2)*b^2 + ... + b^n',
    '2': '(nCr) = n!/(r!*(n-r)!)',
    '3': "f(x) = f(0) + xf'(0) + 0.5x^2f''(0) + ... + (1/n!)x^nf^(n)(0)",
    '4': '(1+x)^n = 1 + nx + 0.5(n)(n-1)x^2 + ... + (1/r!)(n)(n-1)...(n-r+1)x^r + ...',
    '5': 'e^x = 1 + x + 0.5x^2 + 1/6x^3 + ... + (x^r)/(r!) + ...',
    '6': 'sin(x) = x - (x^3)/6 + (x^5)/(5!) + ... + ((-1^r) * x^(2r+1))/((2r+1)!) + ...',
    '7': 'cos(x) = 1 - 0.5x^2 + (x^4)/(4!) - ... + ((-1^r) * x^2r)/((2r)!)',
    '8': 'ln(1+x) = x - 0.5x^2 + (x^3)/3 - ... + (-1^(r+1) * x^r)/r',
    '9': '(px+q)/(ax+b)(cx+d) = A/(ax+b) + B/(cx+d)',
    '10': '(px^2 + qx + r)/(ax+b)(cx+d)^2 = A/(ax+b) + B/(cx+d) + C/(cx+d)^2',
    '11': '(px^2 + qx + r)/(ax+b)(x^2 + c^2) = A/(ax+b) + (Bx+C)/(x^2 + c^2)',
    '12': 'sin(A+B) = sinAcosB + cosAsinB; sin(A-B) = sinAcosB - cosAsinB',
    '13': 'cos(A+B) = cosAcosB - sinAsinB; cos(A-B) = cosAcosB + sinAsinB',
    '14': 'tan(A+B) = (tanA + tanB)/(1 - tanAtanB); tan(A-B) = (tanA - tanB)/(1 + tanAtanB)',
    '15': 'sin(2A) = 2sinAcosA',
    '16': 'cos(2A) = (cosA)^2 - (sinA)^2 = 2(cosA^2 - 1 = 1 - 2(sinA)^2',
    '17': 'tan(2A) = (2tanA)/(1 - (tanA)^2)',
    '18': 'sinP + sinQ = 2sin0.5(P+Q)cos0.5(P-Q)',
    '19': 'sinP - sinQ = 2cos0.5(P+Q)sin0.5(P-Q)',
    '20': 'cosP + cosQ = 2cos0.5(P+Q)cos0.5(P-Q)',
    '21': 'cosP - cosQ = -2sin0.5(P+Q)sin0.5(P-Q)',
}

phys = {
    "1": "An object at rest stays at rest and an object in motion stays in motion with the same velocity and in the same direction unless acted upon by an unbalanced force.",
    "2": "F = m x a --> \nThe acceleration of an object as produced by a net force is directly proportional to the magnitude of the net force, in the same direction as the net force, and inversely proportional to the mass of the object.",
    "3": "For every action, there is an equal and opposite reaction.",
    "4": "P = m x V, \nwhere P = Momentum, \nm = Mass of object, \nV = Velocity of object",
    "5": "ΔP =  ∫ F dt = FΔt, \nwhere ΔP = change in momentum, \nF = force acting on the object, \nΔt = time",
    "6": "The principle of conservation of momentum states that the total momentum before the collision is equal to the total momentum after the collision, provided no external force.",
    "7": "(m1)(U1) + (m2)(U2) = (m1 + m2)(V1), \nwhere m1 = mass of object 1, \nU1 = initial velocity of object 1, \nm2 = mass of object 2, \nU2 = initial velocity of object 2, \nV1 = final velocity of both objects",

}

def menu():
  keep = True
  
  while keep != False:
    print("What subject's formulae would you like to check?")
    print("1. Mathematics")
    print("2. Physics")
    print("3. Computing")
    print("4. Chemistry")
    print("5. Biology")
    print("6. Economics")
    print("0. Exit")

    choice = input("Enter your choice: ")
    print("")

    try:
      choice = int(choice)
    except:
      choice = choice

    if choice == 1:
      print("List of Formulae:")
      print("1. Binomial Expansion")
      print("2. n Choose r")
      print("3. Maclaurin Expansion: f(x)")
      print("4. Maclaurin Expansion: (1+x)^n")
      print("5. Maclaurin Expansion: e^x")
      print("6. Maclaurin Expansion: sin(x)")
      print("7. Maclaurin Expansion: cos(x)")
      print("8. Maclaurin Expansion: ln(1+x)")
      print("9. Partial Fractions: Non-repeated Linear Factors")
      print("10. Partial Fractions: Repeated Linear Factors")
      print("11. Partial Fractions: Non-repeated Quadratic Factor")
      print("12. Trigonometry: Two Angle Formula for sin")
      print("13. Trigonometry: Two Angle Formula for cos")
      print("14. Trigonometry: Two Angle Formula for tan")
      print("15. Trigonometry: Double Angle Formula for sin")
      print("16. Trigonometry: Double Angle Formula for cos")
      print("17. Trigonometry: Double Angle Formula for tan")
      print("18. Trigonometry: sinP + sinQ")
      print("19. Trigonometry: sinP - sinQ")
      print("20. Trigonometry: cosP + cosQ")
      print("21. Trigonometry: cosP - cosQ")

      uc = int(input("Which to display: "))

      print("")
      print(maths[str(uc)]) if (uc>0 and uc<22) else print("Choose something from 1 to 21!")
      print("")

      con = True
      while con != False:
        cont = input("Do you want to continue? (y/n) ")
        if cont == "y" or cont == "Y":
          print("Alright, heading back...")
          print("")
          con = False
          keep = True
        elif cont == 'n' or cont == 'N':
          print("Alright, exiting program...")
          print("")
          con = False
          keep = False
        else:
          print("That wasn't an option!")
          print("")
    
    elif choice == 2:
      print("List of Formulae:")
      print("1. Newton's First Law of Motion")
      print("2. Newton's Second Law of Motion")
      print("3. Newton's Third Law of Motion")
      print("4. Linear Momentum")
      print("5. Impulse")
      print("6. Property of the Conservation of Momentum")
      print("7. Inelastic Collisions")

      uc = int(input("Which to display: "))

      print("")
      print(phys[str(uc)]) if (uc>0 and uc<8) else print("Choose something from 1 to 7!")
      print("")

      con = True
      while con != False:
        cont = input("Do you want to continue? (y/n) ")
        if cont == "y" or cont == "Y":
          print("Alright, heading back...")
          print("")
          con = False
          keep = True
        elif cont == 'n' or cont == 'N':
          print("Alright, exiting program...")
          print("")
          con = False
          keep = False
        else:
          print("That wasn't an option!")
          print("")

    elif choice == 3:
      pass
    elif choice == 4:
      pass
    elif choice == 5:
      pass
    elif choice == 6:
      pass
    elif choice == 0:
      con = True
      while con != False:
        cont = input("Are you sure you want to exit? (y/n) ")
        if cont == "n" or cont == "N":
          print("Alright, heading back...")
          print("")
          con = False
          keep = True
        elif cont == 'y' or cont == 'Y':
          print("Alright, exiting program...")
          print("")
          con = False
          keep = False
        else:
          print("That wasn't an option!")
          print("")
    
    else:
      print("Please enter a number from 0 to 6.")
      print("")

      con = True
      while con != False:
        cont = input("Do you want to continue? (y/n) ")
        if cont == "y" or cont == "Y":
          print("Alright, heading back...")
          print("")
          con = False
          keep = True
        elif cont == 'n' or cont == 'N':
          print("Alright, exiting program...")
          print("")
          con = False
          keep = False
        else:
          print("That wasn't an option!")

menu()