from collections import Counter
import matplotlib.pyplot as plt

amino = [['Phe', 'UUU', 'UUC'], ['Leu', 'UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], ['Ile', 'AUU', 'AUC', 'AUA'],
 ['Met', 'AUG'], ['Val', 'GUU', 'GUC', 'GUA', 'GUG'], ['Ser', 'UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
 ['Pro', 'CCU', 'CCC', 'CCA', 'CCG'], ['Thr', 'ACU', 'ACC', 'ACA', 'ACG'],
 ['Ala', 'GCU', 'GCC', 'GCA', 'GCG'],
 ['Tyr', 'UAU', 'UAC'], ['Stop', 'UAA', 'UAG', 'UGA'], ['His', 'CAU', 'CAC'], ['Gln', 'CAA', 'CAG'],
 ['Asn', 'AAU', 'AAC'], ['Lys', 'AAA', 'AAG'], ['Asp', 'GAU', 'GAC'], ['Glu', 'GAA', 'GAG'],
 ['Cys', 'UGU', 'UGC'],
 ['Trp', 'UGG'], ['Arg', 'CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
 ['Gly', 'GGU', 'GGC', 'GGA', 'GGG']
 ]
 
print("Welcome to the amino acid sequencer!")
print("Simply enter your codon sequence and press enter to begin visualizing your data!\n")

while True:
    temp_codon_sequence = (input("Enter your codon sequence:\n"))
    codon_sequence = temp_codon_sequence.replace(" ", "")
    if not any(str.isdigit(c) for c in codon_sequence):
        pass
     else:
         print("Please enter a valid codon sequence")
         continue
     
    if len(codon_sequence) > 2:
        amino_acid_present = [codon_sequence[x:x + 3].upper() for x in range(0, len(codon_sequence), 3)]
    else:
        print("Please enter a valid codon sequence")
        continue

    i = 0
    for aa in amino_acid_present:
        if aa == 'UAA' or aa =='UAG' or aa == 'UGA':
            del amino_acid_present[i:]
        else:
            i +=1
            continue
            
    chain_length = len(amino_acid_present)
    if 2 < chain_length < 50:
        print(f"Your codon sequence represents a peptide of {chain_length} amino acids!")
    elif chain_length > 50:
        print(f"Your codon sequence represents a polypeptide of {chain_length} amino acids!")
    elif 1 < chain_length < 3:
        print("Your codon sequence represents 2 peptides!")
    else:
        print("Your codon sequence represents 1 peptide!")
    
    new_list = []
    def analyze_sequence(string):
        for value in amino_acid_present:
            for sublist in amino:
                for element in sublist:
                    if element == value:
                        new_list.append(sublist[0])
        return '-'.join(new_list)
    
    print()
 
    print(f"Your amino acid chain is:\n{analyze_sequence(codon_sequence)}\n")

    aa_dict = Counter(new_list)
    print(f"Here is a summary of your data: {dict(aa_dict)}\n")
 
    aa_list = []
    aa_counts = []
    for key, value in aa_dict.items():
        aa_list.append(key)
        aa_counts.append(value)

    def create_h_bar_chart():
        plt.style.use('seaborn-bright')
        plt.barh(aa_list, aa_counts, height=0.5)
        plt.title('Amino Acid Composition')
        plt.xlabel('Counts')
        plt.ylabel('Amino Acids')
        plt.tight_layout()
        plt.show()
 
    def create_bar_chart():
        plt.style.use('seaborn-bright')
        plt.bar(aa_list, aa_counts, width=0.5)
        plt.title('Amino Acid Composition')
        plt.xlabel('Amino Acids')
        plt.ylabel('Counts')
        plt.tight_layout()
        plt.show()
 
    def create_pie_chart():
        plt.style.use('seaborn-bright')
        plt.pie(aa_counts, labels=aa_list, wedgeprops={'edgecolor': 'black'}, autopct='%1.1f%%')
        plt.title('Amino Acid Composition')
        plt.tight_layout()
        plt.show()

    while True:
        user_choice = input("How would you like to visualize your data?\nPlease choose from a Pie Chart, Bar Chart, o
        if user_choice.lower() == 'pie chart' or user_choice.lower() == 'pie':
            create_pie_chart()
            break
        elif user_choice.lower() == 'horizontal bar chart' or user_choice.lower() == 'horizontal':
            create_h_bar_chart()
            break
        elif user_choice.lower() == 'bar chart' or user_choice.lower() == 'bar':
            create_bar_chart()
            break
        else:
            print("Please enter a valid visualization")
            continue
    break
