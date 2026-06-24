class A:
    def test1(self):
        print("method named test1 of A called")


class B(A): # Class B inherits features from parent class A
    def test1(self):
        print("method named test1 of B called")


class C(A): # Class C inherits features from parent class A
    def test1(self):
        print("method named test1 of C called")


class D(B, C): # Class D inherits features from more than one parent class i.e B & C
    def test2(self):
        print("method named test2 of D called")


object1=D()
object1.test1() #looks for test1 in D. Its not there...

"""
Method Resolution Order (MRO) ---
    The rule set python uses to determine the order in which to search for methods in a hierarchy. 
    You can see this order for any class by calling D.mro()
    
    Python follows the MRO to deterimne which parent to check next.
    For class D(B, C) the search order is: D-->B-->C-->A
    
    Python finds test1 in class B first
    
    It executes the code in B printing: "method named test1 of B called".

"""