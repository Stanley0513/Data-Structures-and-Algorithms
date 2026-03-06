import time

num=input("請輸入兩整數(用逗號區隔)：")
n=num.split(",")
n1=int(n[0])
n2=int(n[1])

def one(m,n):
	if m>n:
		m-=n
		one(m,n)
	elif m<n:
		n-=m
		one(m,n)
	elif m==n:
		print("GCD is:",m)

def two(m,n):
	while 1:
		if m>n:
			m-=n
			continue
		elif m<n:
			n-=m
			continue
		elif m==n:
			break
	return m

choice=int(input("請選擇1)遞迴2)迴圈解法"))
if choice==1:
	start=time.time()
	one(n1,n2)
if choice==2:
	start=time.time()
	print("GCD is:",two(n1,n2))
end=time.time()
t=end-start
print("計算時間為",t,"秒")