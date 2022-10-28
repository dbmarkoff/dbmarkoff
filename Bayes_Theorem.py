import math

def checker(p):
    try: 
        p = float(p)
        if p < 0 or p > 1:
            exit()
    except:
        print("All probabilities must be entered as decimals between 0 and 1.")
        exit()
    return float(p)

pab = 0

print(f"Bayes' Theorem Calculator")
print(f"Enter all probabilities as decimals between 0 and 1.")

a = input("Enter condition A: ")
b = input("Enter condition B: ")

pba = input(f"Enter the probabily of {b} given {a} is true: ")
pba = checker(pba)

pa = input(f"Enter the probabily of {a}: ")
pa = checker(pa)

pb = input(f"Enter the probabily of {b}: ")
pb = checker(pb)

pab = (pba * pa) / pb
print(f"The probability of {a} given {b} is true is {pab:.10f}.")