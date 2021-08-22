import math
def main():
    #from math import sqrt
    a=int(4)
    b=int(5)
    op1=float((2*(3/4))+(4*(2/3))-(3*(1/5))+(5*(1/2))) 
    op2=float((2*(math.sqrt(35**2)))+(4*(math.sqrt(36**3)))-(6*(math.sqrt(49**2))))
    op3=float(((a**3)+(2*(b**2)))/(4*a))
    op4=float(((2*(a+b)**2)+(4*(a-b)**2))/(a*(b**2)))
    op5=float((math.sqrt(((a+b)**2)+(2**(a+b))))/((2*a+2*b)**2))
    print(round(op1,4))
    print(round(op2,4))
    print(round(op3,4))
    print(round(op4,4))
    print(round(op5,4))
    
if __name__ == '__main__':
    main()
