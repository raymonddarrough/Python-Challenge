import csv

filePath = "Resources/budget_data.csv"

numberOfMonths = []
profitLoss = []
profitLossDifferences = []

# Open csv file
with open(filePath, "r", encoding = "UTF-8") as handler:
    csvreader = csv.reader(handler)
    next(csvreader)

    for columns in csvreader:
        numberOfMonths.append(columns[0])
        profitLoss.append(int(columns[1]))
    for i in range(len(profitLoss)-1):
        profitLossDifferences.append(profitLoss[i+1]-profitLoss[i])


totalmonths = len(numberOfMonths)

nettotal = sum(profitLoss)  

advchanges = sum(profitLossDifferences) / len(profitLossDifferences)

increase =max(profitLossDifferences)   

decrease = min(profitLossDifferences)


maxmonth = numberOfMonths[profitLossDifferences.index(increase)+1]

minmonth = numberOfMonths[profitLossDifferences.index(decrease)+1]

analysis = (f"Financial Analysis"
"\n----------------------------"
f"\nTotal Months: {totalmonths}"
f"\nTotal: ${nettotal}"
f"\nAverage Change: ${advchanges}"
f"\nGreatest Increase in Profits: {maxmonth} (${increase})"
f"\nGreatest Decrease in Profits: {minmonth} (${decrease})")

print(analysis)

txt_file_path = "Analysis/PyBank_Analysis.txt"

with open(txt_file_path, 'w') as txt:
    txt.write(analysis)




