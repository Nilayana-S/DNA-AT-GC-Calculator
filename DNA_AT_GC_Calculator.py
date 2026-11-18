# DNA GC and AT Content Calculator
# This script calculates the GC content of a given DNA sequence based on user input.
while True:
    dna_sequence = input("Enter the DNA sequence: ")
    dna_sequence = dna_sequence.upper().strip().replace(' ', '')  # Remove any leading/trailing whitespace and any spaces within the sequence
    if len(dna_sequence) == 0: # Check if the input sequence is empty.
        print("Please enter a valid DNA sequence. The sequence cannot be empty.")
    else:
        # Validate the DNA sequence
        for base in dna_sequence:
            if base not in 'ATCGNatcgn':  # Check if the base is not one of the valid DNA bases (A, T, C, G, N) in either uppercase or lowercase.
                print("Invalid DNA sequence. Please enter a sequence containing only A, T, C, G, or N.")
                break
        # for else is a special loop/construct in Python that allows you to execute a block of code if the loop completes without encountering a break statement. 
        # In this case, if the loop finishes checking all bases without finding an invalid one, the else block will execute.
        else:
            # Calculate the GC content
            gc_count = dna_sequence.count('G') + dna_sequence.count('C') #Sequence is converted to uppercase to ensure accurate counting of G and C bases regardless of case.
            at_count = dna_sequence.count('A') + dna_sequence.count('T')
            total_length = len(dna_sequence)
            gc_content = float((gc_count / total_length) * 100)
            at_content = float((at_count / total_length) * 100)
            print("DNA Sequence:", dna_sequence.upper())
            print('Length of the DNA sequence is:', total_length)
            print('The GC content of the DNA sequence is:', gc_content)
            print('The AT content of the DNA sequence is:', at_content)
            # Check for the presence of 'N' bases in the DNA sequence and calculate their percentage if present.
            if "N" in dna_sequence: 
                count_n = dna_sequence.count('N')
                percentage_n = (count_n/len(dna_sequence)*100)
                print("WARNING! WARNING! WARNING! \nThe DNA sequence requires quality control as it contains 'N' bases")
                print("The 'N' bases in the DNA sequence, represent unknown nucleotides. \nThe percentage of 'N' bases in the sequence is:", percentage_n)
                print("Please note these 'N' bases were not included in the AT or GC content calculation. \nBut they were included in the total length of the sequence.")
    question = input("Do you want to enter another DNA sequence? (yes/no): ")
    if question.lower() != 'yes':
        print("Thank you for using the DNA GC and AT Content Calculator.")
        break   
    else:
        continue