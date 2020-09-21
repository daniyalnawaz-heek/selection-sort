
def sorto(list1):
  for i in range (len(list1)):
    index=i
    for y in range(i+1,len(list1)):
      if list1[index]>list1[y]:
        list1[index],list1[y]=list1[y],list1[index]
    
      
      
list2=[39,53,64,65,6,67,56,54,34]   
sorto(list2)   
print(list2)
