class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self,a,b):
        return self.a+self.b
    def subtraction(self,a,b):
        return self.a-self.b
    def multiplication(self,a,b):
        return self.a*self.b
    def division(self,a,b):
        if b==0:
            return "invalid"
        else:
            return self.a/self.b
    
a=float(input("Enter number :" ))
b=float(input("enter number : "))
calci=calculator(a,b)

choice=input("enter choice(+,-,*,/): ")
if choice=="+":
    print("result:",calci.addition(a,b))
elif choice=="-":
    print("result:",calci.subtraction(a,b))
elif choice=="*":
    print("result:",calci.multiplication(a,b))
elif choice=="/":
    print("result:",calci.division(a,b))
else:
    print("error")

