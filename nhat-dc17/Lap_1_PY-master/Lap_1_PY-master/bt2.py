n=int(input("Nhap sp can tinh giai thua:"))
def giaiThua(n):
	if n==0:
		return 1
	return n*giaiThua(n-1)
print(giaiThua(n))