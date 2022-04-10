t= int(input())
for j in range(1,t+1):
  r1 = list(map(int,input().split()))
  r2 = list(map(int,input().split()))
  r3 = list(map(int,input().split()))
  x= min(r1[0],r2[0],r3[0])
  y= min(r1[1],r2[1],r3[1])
  z= min(r1[2],r2[2],r3[2])  
  w= min(r1[3],r2[3],r3[3])  
  ress = x+y+z+w 
  
  if ress==1000000:

    print('Case #'+str(j)+':',x,y,z,w)
  elif ress<1000000:
    print('Case #'+str(j)+': IMPOSSIBLE')
  else:
    ress=0 
    i=0
    l1=[x,y,z,w]
    while ress<1000000:
      ress = ress + l1[i]
      i+=1 
    if ress==1000000:
      l2=l1[:i]
    else:
      l2= l1[:i-1]
      l2.append(1000000-sum(l1[:i-1]))
    l2.extend(list(map(int,list('0'*(4-len(l2))))))
    print('Case #'+str(j)+':',*l2)