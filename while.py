#while loops

i=1
while i<6:
 print(i)
 i+=1

print('\n')

#continue
i=0
while i<6:
 i+=1
 if(i==3):
  continue
 print(i)
 
 #break
print('\n')

i=0
while i<6:
 i+=1
 if(i==3):
  break
 print(i)

print('\n')

i=1
while i<6:
 print(i)
 i+=1
else:
  print("end")
