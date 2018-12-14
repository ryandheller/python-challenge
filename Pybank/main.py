import os
import csv
import numpy as np
csvpath=os.path.join("..","Pybank","budget_data.csv")
date_index=[]
date_min=[]
date_max=[]
months=0
data=[]
net_amount=[]
month=[]
pairs=[]
diffs=[]
with open(csvpath,"r") as f:
    reader=csv.reader(f)
    for row in reader:
        data.append(row)
        #print(row)
    
    for index, row in enumerate(data):
        try:
            pairs.append((row[1], data[index+1][1]))
        except IndexError:
            pass
        #list(zip(data,data[1:]))
        month.append(row[0])
    
    
    for pair in pairs[1:]:
        first, second=pair
        diff=int(second)-int(first)
        diffs.append(diff)
        
        #print("Average Change:", np.mean(diffs))

    for date,profit in data:
        net_amount.append(profit)
        if date==date:
            months+=1

    
    
    
    diffs=[int(i)for i in diffs]    
    net_amount.remove("Profit/Losses")
    net_amount=[int(i) for i in net_amount]
    
    
    print("Financial Analysis")
    print("--------------")
    print(f"Total Months:,({months}-1)")
    print(f"Total:${sum(net_amount)}")
    print(f"Average Change: $ {round(np.mean(diffs),2)}")
    print(f"Greastest Increase in Profits: {month[diffs.index(max(diffs))+1]} ${max(diffs)}")
    print(f"Greastest Decrease in Profits: {month[diffs.index(min(diffs))+1]} ${min(diffs)}")

    file=open("Pybank_Solved.txt","w")
    file.write("Financial Analysis" +"\n")
    file.write("--------------" + "\n")
    file.write(f"Total Months:,({months-1})"+"\n")
    file.write(f"Total:${sum(net_amount)}"+"\n")
    file.write(f"Average Change: $ {round(np.mean(diffs),2)}"+"\n")
    file.write(f"Greastest Increase in Profits: {month[diffs.index(max(diffs))+1]} ${max(diffs)}" +"\n")
    file.write(f"Greastest Decrease in Profits: {month[diffs.index(min(diffs))+1]} ${min(diffs)}"+"\n")
    file.close()

   
    

    
    #for row, bull in reader:
     #   net_amount.append(bull)
      #  month.append(bull)
       # if row==row:
        #    months+=1
    #net_amount.remove("Profit/Losses")
    #net_amount=[int(i) for i in net_amount]
    

    #print("Total:",sum(net_amount))
    #print("Total Months:",months)
    #print(combined)
        
    
    #b=0
    #b+=sum(float(net_amount))
    #print(b)
    #for date, profit in reader:
       #if date==date:
           #months+=float(1)
       #if profit==profit:
           #net_amount.append(profit)
    #print("The totalt number of months is", months)
    
    #for x in net_amount:
        #xy=int(x)
    #print(net_amount)

#profit=[100,-200,50,1000,50,200]
#diffs.index(max(diffs))
#months[diffs.index(max(diffs))]