import pandas as pd
import sys
import argparse

parser = argparse.ArgumentParser(
        description = ("A CSV parser that takes in the specific file and outputs "
                        "several protein properties including protein sequence, " 
                        "molecular weight (in g/mol or kDa), and the "
                        "extinction coefficient (in A280/M*cm). "
                        "Optional argument '-c' after the file  gives amino acid composition in a new file"
                        ),
        epilog = "Outputs a file with protein information as 'Protein_results.csv' \n"
                "with 'Translation', 'Molecular Weight' in g/mol, and "
                "'Extinction Coefficient' in A280/M*cm' and optionally amino acid composition"
                                )
parser.add_argument("file", metavar = "-file", help = "The CSV file with 3 columns: \n"
                                                       "'Name' - Name of gene.\n"
                                                       "'Type' - DNA, RNA, or Protein.\n"
                                                       "'Sequence' - The sequence of specified gene.\n")
parser.add_argument("-c", "--composition", action = "store_true",
                    help = "optional argument placed after the file that produces another CSV file with amino acid composition"
                    )

args = parser.parse_args()

def pandas_functions(fileinput):
    #Creates a pandas dataframe, then add columns based on functions, then returns a CSV file with results
    df = pd.read_csv(fileinput)
    df.columns = df.columns.str.title()
    df["Translation"] = df.apply(seq_to_prot, axis = 1)
    df["Protein Length"] = df["Translation"].apply(prot_length)
    df["MW (g/mol)"] = df["Translation"].apply(prot_MW)
    df["Extinction Coefficient"] = df["Translation"].apply(ex_coef)
    df.to_csv("Protein_results.csv", encoding = "utf-8", index = False)
    print("File 'Protein_results.csv' complete")

def seq_to_prot(user_input):
    try:
        #Checks if 'Type' column is either DNA, RNA or Protein and returns the string of the input to appropirate function.
        if user_input["Type"] in ["D", "DNA", "d", "dna"]:
            DNA_input = str(user_input["Sequence"]).upper().strip()
            prot_seq = translate(DNA_input)
            return prot_seq
    
        elif user_input["Type"] in ["RNA", "rna", "R", "r"]:
            DNA_input = str(user_input["Sequence"]).upper().strip()
            DNA_input = DNA_input.replace("U", "T")
            prot_seq = translate(DNA_input)
            return prot_seq
    
        elif user_input["Type"] in ["Protein", "P", "protein", "PROTEIN"]:
            prot_seq = str(user_input["Sequence"]).upper().strip()
            return prot_seq
        
        else:
            raise ValueError
    
    except (ValueError, TypeError):
        return "Invalid input in 'Type' field"
        pass
        
def translate(DNA_input):
    #Create codon table of all possible 3 combinations. '*' is stop codon
    codon_table = {
            'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
            'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
            'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
            'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
            'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
            'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
            'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
            'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
            'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
            'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
            'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
            'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
            'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
            'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
            'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*', 
            'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W', 
            } 
        
    protein_seq = ""
    DNA_input = str(DNA_input).strip()
    
    try:
        #DNA or RNA length must be divisible by 3
        if len(DNA_input) % 3 == 0:
            for i in range(0, len(DNA_input), 3):
                codon = DNA_input[i:i+3]
                protein_seq += codon_table[codon]
            return protein_seq
        else:
            return "Not a divisble CDS"
    
    except:
        return "Invalid entry in the 'Sequence' field"
        pass

def prot_length(Prot_input):
    #Returns the length of protein 
    if Prot_input.startswith(("Not", "Invalid")):
        return "0"
    else:
        return len(Prot_input)

def prot_MW(Prot_input):
    #Create dic with amino acid molecular weight in g/mol 
    AA_MW = {
    "A": 71.0788,   "R": 156.1875, "N": 114.103,
    "D": 115.0886,  "C": 103.1388, "E": 129.115,
    "Q": 128.1307,  "G": 57.0519,  "H": 137.1411,
    "I": 113.1594,  "L": 113.1594, "K": 128.1741,
    "M": 131.1926,  "F": 147.1766, "P": 97.1167, 
    "S": 87.0782,   "T": 101.1051, "W": 186.2132,
    "Y": 163.1760,  "V": 99.1326,  "*": 0,
    "U": 150.0388,  "O": 237.3018, "-": 0, 
    "X": 110.000,   "B": 114.5962, "Z": 128.6231,
    " ": 0,          "": 0
    }
    
    ##The 18 refers to the weight of water, total, present in N (2 H's) and C (1 O) terminal
    prot_mol_weight = 18
    amino_acids = list(Prot_input)

    ##For loop adds the mol weight dictionary key into the prot_mol_weight
    try:
        for aa in amino_acids:
            prot_mol_weight += AA_MW[aa]
    
        return f"{prot_mol_weight:.2f}"
    
    except:
        return "Invalid amino acid"
        pass

def ex_coef(Prot_input):
    ##Determinest he extinction coefficient at 280 nm to determine protein concentration
    num_trp = 0
    num_tyr = 0
    num_cys = 0
    
    try:
        for aa in list(Prot_input):
            if aa == "W":
                num_trp += 1
            elif aa == "Y":
                num_tyr += 1
            elif aa == "S":
                num_cys += 1
            else:
                pass
    ##Calculates extinction based on number of specific residue's values
        ext_coef = num_trp * 5500 + num_tyr * 1490 + num_cys * 125
    
        return ext_coef
    
    except:
        pass

def aa_count (fileinput):

    #This method counts the number of amino acids in each protein in this specific order
    amino_acids = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]
    df = pd.read_csv(fileinput)
    df.columns = df.columns.str.title()
    df["Translation"] = df.apply(seq_to_prot, axis = 1)
    
    #Create new dataframe with only 'Translation' of protein
    df2 = pd.DataFrame([])
    df2["Sequence"] = df["Translation"]
    df2.set_index(df["Name"], inplace = True)
    
    #Replaces invalid protein translations with blanks
    cond = df2["Sequence"].str.startswith(("Not", "Invalid"))
    df2.loc[cond, "Sequence"] = ""
    
    #Create a new dataframe that will count each occurance from each amino acid in a transposed method
    df3 = pd.DataFrame([])
    
    #Uses panda's own count of each letter by order of the amino_acids above
    for aa in amino_acids:
        df3[aa] = df2["Sequence"].str.count(aa)
    
    #Transpose so that amino acids are rows and not columns then add index name
    df3 = df3.T
    df3.index.name = "Amino Acid"
    
    #Exports the second sheet
    df3.to_csv("Protein_AA_counts.csv", encoding = "utf-8", index = True)
    print("File 'Protein_AA_counts.csv' complete")
    
    
if __name__ == "__main__":
    try:
        if len(sys.argv) >= 2:
            #Checks of there are 2 or more command line inputs
            if len(sys.argv) == 2:
                if sys.argv[1].endswith((".csv", ".CSV")):
                    df1 = pandas_functions(sys.argv[1])
            #If '-c' is added, then does two functions instead of 1
            elif len(sys.argv) == 3 and sys.argv[2] == "-c":
                if sys.argv[1].endswith((".csv", ".CSV")):
                    df1 = pandas_functions(sys.argv[1])
                    df2 = aa_count(sys.argv[1])
                else:
                    raise IOError
            else:
                raise IOError     
        else:
            raise FileNotFoundError
    
    except (FileNotFoundError, IOError):
        print ("The file does not exist or is not a CSV file or incorrect arguments")