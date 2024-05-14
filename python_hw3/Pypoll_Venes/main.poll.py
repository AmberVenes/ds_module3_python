#  Import csv module
import csv

# declared variables
total_votes = 0
can_dictionary = {}
winner_can = ""
max_votes = 0

# Define path by copying the relative path of CSV
csvpath = "Pypoll_Venes/Resources_poll/election_data.csv"

# Use with to open and finish the program
with open(csvpath, encoding='UTF-8') as csvfile:
     # CSV reader specifies delimiter and separates data to make readable
    csvreader = csv.reader(csvfile, delimiter=',')

    # Used next to skip the csv header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # assigned variable "row" to every element of the list
    for row in csvreader:
        
          # count the number of votes   
          total_votes += 1

          # listing out names of candidates and number of votes they got. Used the keys to summon dictionary
          can_row = row[2]
          if can_row in can_dictionary.keys():
               can_dictionary[can_row] += 1
          else:
               can_dictionary[can_row] = 1

# I understand up until this point the way the outputs are formatted confused me. I used professer Booths code and office hours as refereance for the rest.

output = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------\n"""

for candidate in can_dictionary.keys():
    # get votes
    votes = can_dictionary[candidate]
    perc = 100 * (votes / total_votes)

    line = f"{candidate}: {round(perc, 3)}% ({votes})\n"
    output += line

    # get max of dictionary
    if votes > max_votes:
          max_cand = candidate
          max_votes = votes
          
last_line = f"""-------------------------
Winner: {max_cand}
-------------------------"""
output += last_line

print(output)

with(open("output_venes_poll.txt", 'w') as f):
    f.write(output)
