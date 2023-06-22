n=int(input())
l=list(map(int,input().split()))
l.remove(min(l))
l.remove(max(l))
lt=len(l)
for i in range(lt):
        total=sum(l)/lt
o=format(total, ".8f")
print(o)

        
