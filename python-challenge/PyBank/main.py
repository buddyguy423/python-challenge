import os
import csv

bankcsv = os.path.join('Resources', 'budget_data.csv')



with open(bankcsv) as csvfile:
    read = csv.reader(csvfile)
    
    next(read)
    dates = []
    rev = []
    delta = []
    
    for row in read:
        rev.append(float(row[1]))
        dates.append(row[0])
        
    for i in range(1, len(rev)):
        delta.append(rev[i]-rev[i-1])
        avg_delta = sum(delta)/len(rev)
        
        min_delta = min(delta)
        max_delta = max(delta)
        max_d_date = str(dates[delta.index(max(delta))])
        min_d_date = str(dates[delta.index(min(delta))])
    
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(dates))
    print("Total Revenue: $", sum(rev))
    print("Average Revenue Change: $", round(avg_delta))
    print("Greatest Increase in Revenue: " f"{max_d_date},", f"({max_delta})")
    print("Greatest Decrease in Revenue: " f"{min_d_date},", f"({min_delta})")
    
    
    
    with open ("PyBank\Outfile.txt", "w") as text_file:
        print("Financial Analysis", file= text_file)
        print("-----------------------------------", file = text_file)
        print("Total Months:", len(dates), file= text_file)
        print("Total Revenue: $", sum(rev), file= text_file)
        print("Average Revenue Change: $", round(avg_delta), file= text_file)
        print("Greatest Increase in Revenue: " f"{max_d_date},", f"({max_delta})",file= text_file)
        print("Greatest Decrease in Revenue: " f"{min_d_date},", f"({min_delta})",file= text_file)








    