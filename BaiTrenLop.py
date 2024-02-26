# bài tập nhập một số nguyên thoải 0<0<100
# a kiểm tra n có phải là số nguyên tố ko
# b in ra các số nguyên số < n

#buoc1
while True:
    n = int(input("Nhập số nguyên n:"))
    if n>0 and n<=1000:
        break
print("số vừa nhập là: ", n)
#định nghĩa một hàm coi có phải là số nguyên tố hay ko
def laSNT(n):
    if n < 2:
        return False
    for i in range(2,n//2+1):
        if n% i ==0:
            return False
    return  True
if laSNT(n):
    print("{} la so nguyen to".format(n))
else:
    print("{} bu shi nguyen to shu".format(n))

#B
for i in range(2,n+1):
    if laSNT(i):
        print("%5d" % i, end=" ")