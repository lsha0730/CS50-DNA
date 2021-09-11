import csv
import sys

def main():
    # Validate usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py [Profiles.csv] [Sample.txt]")

    # Dictionary of people and their DNA counts
    people = []
    with open(sys.argv[1], 'r') as profiles:
        reader = csv.reader(profiles)
        header = next(reader)
        for row in reader:
            people.append(row)


    # Create list of possible STRs
    STRs = []
    for i in range(1, len(header), 1):
        STRs.append(header[i])

    # Create dictionary of every sample STR
    STR_counts = dict.fromkeys(STRs, 0)

    # Read the sequence
    f = open(sys.argv[2], 'r')
    sequence = f.read()

    # Find the longest sequence of each STR
    for STR in STRs:

        # Make a list of the sequence lengths
        seq_lengths = [0]
        longest = 0

        i = 0
        for letter in sequence:
            if is_STR(STR, i, sequence):
                i += len(STR)
                longest += 1
            else:
                if not(longest==0):
                    seq_lengths.append(longest)
                longest = 0
                i += 1

        # Put the greatest sequence count for each STR in the dict
        seq_lengths.sort(reverse=True)
        STR_counts[STR] = seq_lengths[0]


    # Check if it matches anyone, then print their name
    for person in people:
        matches = []
        for i in range(len(header) - 1):
            matches.append(False)
            
        for i in range(1, len(person), 1):
            if int(person[i]) == int(STR_counts[header[i]]):
                matches[i - 1] = True
        
        guilty = True
        if False in matches:
            guilty = False

        if guilty:
            print (person[0])
            return

    print("No match")


def is_STR(STR, index, sequence):
    count = 0
    for i in range(len(STR)):
        if (index + i) < len(sequence) and sequence[index + i] == STR[i]:
            count += 1

    if count == len(STR):
        return True

    return False

main()