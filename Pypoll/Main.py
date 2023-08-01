import csv

filePath = "Resources/election_data.csv"

totalvotes = 0

candidates = {}

votepercent = []

with open(filePath, "r", encoding = "UTF-8") as handler:
    csvreader = csv.reader(handler)
    next(csvreader)


    for row in csvreader:
        totalvotes += 1
        if row[2] not in candidates:
            candidates[row[2]] = 1 
        else:
            candidates[row[2]] += 1 


    candidate_key = max(candidates, key = candidates.get)   

    print("Election Results"
        "\n--------------------------"
        f"\n Total Votes: {totalvotes}"
        "\n--------------------------"
        )

    for key,value in candidates.items():
            print(f"{key} : {round((value/totalvotes)*100, 3)}% ({value})")
    print( "--------------------------"
        f"\n Winner: {candidate_key}"
        "\n--------------------------"
        )
        
txt_file_path = "Analysis/PyPoll_Analysis.txt"

with open(txt_file_path, 'w') as txt:
    print("Election Results"
          "\n-------------------------"
          f"\nTotal Votes: {totalvotes}"
          "\n-------------------------", file = txt)
    for key,value in candidates.items():
        print(f"{key} : {round((value/totalvotes)*100, 3)}% ({value})", file = txt)    
    print("-------------------------"
          f"\nWinner: {candidate_key}"
          "\n-------------------------", file = txt)















