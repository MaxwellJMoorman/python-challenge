### PyPoll

# Load CSV and os
import csv
import os

# Create Lists
total_votes = []
whom_vote = []
Unique_ID = []

# Open CSV
with open('election_data.csv') as csvDataFile:
    csvreader = csv.reader(csvDataFile)
    csv_header = next(csvDataFile)

    # Assign data into lists
    for row in csvreader:
        total_votes.append(row[0])
        whom_vote.append((row[2]))
        
        #
        if row[2] not in Unique_ID:
            Unique_ID.append(row[2])    

    #Print Results
    print('Election Results')
    print('Total # of Votes: {}'.format(len(total_votes)))
    for name in Unique_ID:
        print('{}: {:.2f}% ({})'.format(name,(whom_vote.count(name)/len(total_votes))*100,whom_vote.count(name)))        

        
# Create txtfile 
outpath = os.path.join('election_data_analysis.txt')

# Copy analysis to txtfile
with open(outpath, 'w', newline="") as txtfile:
    writer = csv.writer(csvDataFile)
    txtfile.write('Election Results')
    txtfile.write('\n')
    txtfile.write('-------------------')
    txtfile.write('\n')
    txtfile.write('Total # of Votes: {}'.format(len(total_votes)))
    txtfile.write('\n')
    txtfile.write('{}: {:.2f}% ({})'.format(name,(whom_vote.count(name)/len(total_votes))*100,whom_vote.count(name)))


    

    


    
