import os
import csv

pollcsv = os.path.join('Resources', 'election_data.csv')

with open (pollcsv) as election_data:
    read = list(csv.reader(election_data))
    #next(election_data)
    
    votes = []
    candidates = []
    
    
#use counts
    for row in read:
        votes.append(row[2])
    
    for candidate in votes:
        if candidate not in candidates:
            candidates.append(candidate)
    Khan = votes.count('Khan')
    Correy = votes.count('Correy')
    Li = votes.count('Li')
    oTooley = votes.count("O'Tooley")
    total_count = len(votes)-1 

    Khan_perecent = Khan/total_count
    Correy_perecent = Correy/total_count
    Li_perecent = Li/total_count
    oTooley_perecent = oTooley/total_count
    result_dict = {'Khan': Khan, 'Correy': Correy, 'Li':Li, "O'Tooley":oTooley }
    result_max = max(result_dict, key=result_dict.get)
    
    
    
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " f"{total_count}")
    print("-------------------------")
    print("Khan: {:.3%} ({})".format(Khan_perecent, Khan))
    print("Khan: {:.3%} ({})".format(Correy_perecent, Correy))
    print("Khan: {:.3%} ({})".format(Li_perecent, Li))
    print("Khan: {:.3%} ({})".format(oTooley_perecent, oTooley))
    print("-------------------------")
    print("Winner:" f"{result_max}")
    print("-------------------------")
    
    with open("PyPoll\Outfile.txt", "w") as text_file:
        print("Election Results", file = text_file)
        print("-------------------------", file = text_file)
        print("Total Votes: " f"{total_count}", file = text_file)
        print("-------------------------", file = text_file)
        print("Khan: {:.3%} ({})".format(Khan_perecent, Khan), file = text_file)
        print("Khan: {:.3%} ({})".format(Correy_perecent, Correy), file = text_file)
        print("Khan: {:.3%} ({})".format(Li_perecent, Li), file = text_file)
        print("Khan: {:.3%} ({})".format(oTooley_perecent, oTooley), file = text_file)
        print("-------------------------", file = text_file)
        print("Winner:" f"{result_max}", file = text_file)
        print("-------------------------", file = text_file)