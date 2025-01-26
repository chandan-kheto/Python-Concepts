class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"


C1=C()

print(C1.varC)
print(C1.varB)
print(C1.varA)

