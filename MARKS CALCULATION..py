print("The current problem how to calculate state board 2020-2021 total marks!!")
a=[]
n=int(input("Enter number of subjects in 10 th:"))
for i in range(1,n+1):
    b=int(input("Enter mark :"))
    a.append(b)
a.sort()
k=(((a[n-1]+a[n-2]+a[n-3])/300)*0.5)*100
x=k+30
y=[]
g=int(input("Enter number of subjects in 11 th excluding your internal and practical marks :"))
for h in range(1,g+1):
    l=int(input("Enter mark :"))
    y.append(l)
ab=((((y[g-6])/90)*100)*0.2)
bc=((((y[g-5])/90)*100)*0.2)
cd=((((y[g-4])/90)*100)*0.2)
de=((((y[g-3])/70)*100)*0.2)
ef=((((y[g-2])/70)*100)*0.2)
fg=((((y[g-1])/70)*100)*0.2)
Total=((ab+x)+(bc+x)+(cd+x)+(de+x)+(ef+x)+(fg+x))
print("Your Final Mark in 12 th state board examination is :",Total)
z=((cd+x)+((de+x)/2)+((ef+x)/2))
print("Your Cut off is :",z)


