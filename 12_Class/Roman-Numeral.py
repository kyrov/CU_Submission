class roman:
    def __init__(self,r):
        self.r = r
    def __lt__(self,rhs):
        return int(self) < int(rhs)
    def __str__(self):
        return self.r
    def __int__(self):
        su = 0
        i = 0
        while i < len(self.r):
            if self.r[i]=="M":
                su += 1000
            elif self.r[i]=="D":
                su += 500
            elif self.r[i]=="C":
                if(i != len(self.r)-1):
                    if(self.r[i+1]=="M"):
                        su += 900
                        i += 1
                    elif(self.r[i+1]=="D"):
                        su += 400
                        i += 1
                    else:
                        su += 100
                else:
                    su += 100
            elif self.r[i]=="L":
                su += 50
            elif self.r[i]=="X":
                if(i != len(self.r)-1):
                    if(self.r[i+1]=="C"):
                        su += 90
                        i += 1
                    elif(self.r[i+1]=="L"):
                        su += 40
                        i += 1
                    else:
                        su += 10
                else:
                    su += 10
            elif self.r[i]=="V":
                su += 5
            elif self.r[i]=="I":
                if(i != len(self.r)-1):
                    if(self.r[i+1]=="X"):
                        su += 9
                        i += 1
                    elif(self.r[i+1]=="V"):
                        su += 4
                        i += 1
                    else:
                        su += 1
                else:
                    su += 1
            i += 1
        return su
    def __add__(self,rhs):
        num = int(self) + int(rhs)
        ans = ""
        while num > 0:
            if(num>=1000):
                ans += "M"
                num -= 1000
            elif(num >=900):
                ans += "CM"
                num -= 900
            elif(num >= 500):
                ans += "D"
                num -= 500
            elif(num >=400):
                ans += "CD"
                num -= 400
            elif(num >= 100):
                ans += "C"
                num -= 100
            elif(num >= 90):
                ans += "XC"
                num -= 90
            elif(num >= 50):
                ans += "L"
                num -= 50
            elif(num >= 40):
                ans += "XL"
                num -= 40
            elif(num >= 10):
                ans += "X"
                num -= 10
            elif(num >= 9):
                ans += "IX"
                num -= 9
            elif(num >= 5):
                ans += "V"
                num -= 5
            elif(num >= 4):
                ans += "IV"
                num -= 4
            elif(num >= 1):
                ans += "I"
                num -= 1
        return roman(ans)
t, r1, r2 = input().split()
a = roman(r1)
b = roman(r2)
if t == '1':
    print(a < b)
elif t == '2':
    print(int(a), int(b))
elif t == '3':
    print(str(a), str(b))
elif t == '4':
    print(int(a + b))
else:
    print(str(a + b))