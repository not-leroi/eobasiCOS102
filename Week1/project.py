p = int(input("Input your principal: "))
r= int(input("Input the rate: "))
t = int(input("Input the number of years: "))
n = int(input("How many times did the interest apply per time: "))
pmt = int(input("Input your PMT: "))
calculate = input("What do you want to calculate? SI (Simple interest), CI (Compound Interest) or AP(Annuity Plan)? ").upper()

if calculate == "SI":
    a = p * (1 + (r / 100) * t)
    print("Your simple interest is: N" + str(a))
elif calculate == "CI":
    a = p * (1 + r / n) ** (n * t)
    print("The compound interest is: N" + str(a))
elif calculate == "AP":
    a = pmt * ((1 + r / n ** (n * t)) - 1) / (r / n)
    print("Your annuity plan is: N " + str(a))
else :
    print("Answer not applicable")
