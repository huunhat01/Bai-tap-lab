import math

def isPrimeNumber(n):
	if(n<2):
		return False;
	squareRoot= int (math.sqrt(n));
	for i in range (2, squareRoot+1):
		if(n%i==0):
			return False;
	return True;

n=int (input("Mhap vao so nuyen n:"));
print("Tat ca cac so nguyen nho hon:", n, "la:");
sb="";
if(n>=2):
	if(isPrimeNumber(i)):
		sb=sb+str(i)+"";
	i=i+2;
print(sb);

