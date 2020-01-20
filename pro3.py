a=input("enter string")
count=count1=0
for i in a:
    if i.isdigit():
        count=count+1;
             elif i.isalpha():
        count1=count1+1;
      else:
       pass
      print("Letters",count)
       print("Digits",count1)