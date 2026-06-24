def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


ans = fact(9)
print(ans)

"""
fact = 1 i=1
fact=1*1
fact=1

fact=1 i=2
fact=1*2
fact=2

fact=2 i=3
fact=2*3
fact=6

fact=6 i=4
fact=6*4
fact=24

fact=24 i=5
fact=24*5
fact=120

return(fact) = retrun(120)




"""
