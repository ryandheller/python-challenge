import os
import csv
csvpath=os.path.join("..","Pypoll","election_data.csv")
total_votes=0
data=[]
all_cand=[]
khan=0
otooley=0
li=0
correy=0
with open(csvpath, "r") as f:
    reader=csv.reader(f)
    for row in reader:
        total_votes+=1
        data.append(row)
    for x,y,z in data:
        all_cand.append(z)
        if z=="Khan":
            khan+=1
        elif z=="O'Tooley":
            otooley+=1
        elif z=="Li":
            li+=1
        elif z=="Correy":
            correy+=1
    all_cand.remove("Candidate")
    output=set(all_cand)
    total_votes+=(-1)
    per_khan=round(khan/total_votes,3)*100
    per_otooley=round(otooley/total_votes,3)*100
    per_li=round(li/total_votes,3)*100
    per_correy=round(correy/total_votes*100,3)
    cands=["Khan","Li","Correy","O'Tooley"]
    votes=[khan, li, correy, otooley]
    
        
print("Election Results")
print("--------------")
print(f"Total Votes:{total_votes}")
print("--------------")
print(f"Khan:{per_khan}% ({khan})")
print(f"Correy: {per_correy}% ({correy})")
print(f"Li: {per_correy}% ({li})")
print(f"O'Tooley: {per_otooley}% ({otooley})")
print("--------------")
print(f"Winner:{cands[votes.index(max(votes))]}")

file=open("Pypoll_solved.txt","w")
file.write("Election Results"+"\n")
file.write("--------------"+"\n")
file.write(f"Total Votes:{total_votes}"+"\n")
file.write("--------------"+"\n")
file.write(f"Khan:{per_khan}% ({khan})"+"\n")
file.write(f"Correy: {per_correy}% ({correy})"+"\n")
file.write(f"Li: {per_correy}% ({li})"+"\n")
file.write(f"O'Tooley: {per_otooley}% ({otooley})"+"\n")
file.write("--------------"+"\n")
file.write(f"Winner:{cands[votes.index(max(votes))]}")
file.close()