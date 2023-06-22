str=input()
ldr=input()
l=len(str)
r=len(ldr)
if l==r:
        sorted1=sorted(str)
        sorted2=sorted(ldr)
        if sorted(str)==sorted(ldr):
                print("true")
        else:
                print("false")
else:
        print("false")
