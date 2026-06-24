import math


s=int(input()) #start value 0
e=int(input()) #end value 100
w=int(input()) #step size 20

f=s # f=0
while f<=e: # 0<=100 i.e True
	celsius=(f-32)*5/9 #conversion formula   (0-32)*5/9=-17.7777
	if celsius>=0:  #if -17.7777>=0
		print(f,math.floor(celsius))  #for -ve numbers, ceil rounds towards 0
	else:
		print(f,math.ceil(celsius)) #rounds to ceil value i.e -17 coz    <-----18_____-17.777_____-17------>
	f+=w   #f=f+w i.e f=0+20= f=20

"""
2nd iteration

f=20
20<=100
celsius=(20-32)*5/9 = -6.6666
celsius>=0
-6.6666<=0
else:
	20,6 is o/p
f=20+20=40	

	
3rd iteration
	
f=40
40<=100
celsius=(40-32)*5/9=4.4444
celsius>=0
4.4444>0
if:
    40,4 is o/p
f=40+20=60

    




"""