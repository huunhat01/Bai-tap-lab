def convert_Number(n,b):
	if(n<0 or b<2 or b>16 ):
		return "";

	sb="";
	m=0;
	remainder=n;

	while (remainder>0):
		if(b>10):
			m=remainder%b;
			if(m>=10):
				sb=sb+str(chr(55+m));
			else:
				sb=sb+str(m);
		else:
			sb=sb+str(remainder%b);
		remainder=int (remainder/b);
	return "".join(reversed(sb));

n= int (input("nhap so nguyen duong n:"));
print ("He co so 2 cua n:", n, "la:", convert_Number(n, 2))

print ("He co so 16 cua n:", n, "la:", convert_Number(n, 16))


