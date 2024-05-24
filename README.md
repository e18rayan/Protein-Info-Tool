"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~                                                                  ~
~ .#####..#####...####..######.######.######.##..##.               ~
~ .##..##.##..##.##..##...##...##.......##...###.##.               ~
~ .#####..#####..##..##...##...####.....##...##.###.               ~
~ .##.....##..##.##..##...##...##.......##...##..##.               ~
~ .##.....##..##..####....##...######.######.##..##.               ~
~ ..................................................               ~
~ .######.##..##.######..####.........######..####...####..##..... ~
~ ...##...###.##.##.....##..##..........##...##..##.##..##.##..... ~
~ ...##...##.###.####...##..##..........##...##..##.##..##.##..... ~
~ ...##...##..##.##.....##..##..........##...##..##.##..##.##..... ~
~ .######.##..##.##......####...........##....####...####..######. ~
~ ................................................................ ~
~                                                                  ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

## Protein Information Tool

This tool takes in a CSV file with protein names, sequences, types (DNA, RNA, or protein input), then generates a CSV file with:
1. Protein Translation Sequence
2. Protein Length
3. Molecular Weight (in g/mol)
4. Extinction Coefficient ( in M<sup>-1</sup> cm<sup>-1</sup>)

The optional '-c' will provide generate the file above, plus an additional CSV file with each protein's amino acid breakdown (only 20 canconcial ones).

#### Running the script
```
python Protein_Info.py Sequences.csv [-c]
```

### Example
#### Input file
| Name      | Type      | Sequence       |
| :---      | :---      | :---           |
|Protein1   | D         | ATGACG...TAA   |
|Protein2   | RNA       | AUGGAU...UAA   |
|Protein3   | Protein   | MNF...PTV      |

#### Output file "Protein_results.csv"
| Name    | Type    | Sequence    | Translation  | Protein Length| MW (g/mol)| Extinction Coefficent|
| :---    | :---    | :---        | :---         | :---          | :---      | :---                 |
|Protein1 | D       | ATG...TAA   | MTR...PTV*   | 577           | 64209.38  | 35985                |
|Protein2 | RNA     | AUG...UAA   | MDS...DSD*   | 387           | 43495.1   | 31140                |
|Protein3 | Protein | MNF...PTV   | MNF...PTV    | 565           | 62778.78  | 35985                |

#### Output file will generate above plus "Protein_AA_Counts.csv" from optional '-c'
| Amino Acid   | Protein1  | Protein2  | Protein3  |
| :---         | :---      | :---      | :---      |
| A            | 61        | 20        | 59        |
| R            | 41        | 20        | 38        |
| N            | 25        | 12        | 25        |
| D            | 22        | 23        | 21        |
| C            | 3         | 12        | 3         |
| Q            | 39        | 20        | 39        |
| E            | 38        | 31        | 36        |
| G            | 37        | 16        | 37        |
| H            | 9         | 10        | 9         |
| I            | 20        | 9         | 20        |
| L            | 34        | 33        | 33        |
| K            | 40        | 29        | 40        |
| M            | 25        | 9         | 24        |
| F            | 25        | 10        | 25        |
| P            | 40        | 32        | 40        |
| S            | 33        | 30        | 33        |
| T            | 29        | 35        | 27        |
| W            | 2         | 2         | 2         |
| Y            | 14        | 11        | 14        |
| V            | 40        | 23        | 40        |

## Requirements
### Required dependecies 
Dependencies for script:
```
python 3.2 or above
pandas 2.2.1 or above
```
The rest are standard Python libraries.

### Input File
A sample sheet named "Sample_Sheet.csv" is included if desired.

Input file can be any name but must be a CSV file and contain the following fields within the file:
- Name
  - Column header must be typed exactly **Name** .
  - Protein or sequence names can be any acceptable text.
- Type
  - Column header must be typed exactly **Type**.
  - Fields can be: DNA, dna, D, RNA, rna, R, Protein, protein, P.
  - Any other input will cause it to give you an "Invalid type".
- Sequence
  - Column header must be typed exactly **Sequence**.
  - DNA can contain any base "ATCG" while RNA can contain bases "AUGC".
    - No mixing DNA and RNA bases (e.g. "ATCU" not allowed).
    - No degenerate bases.
    - Does not have to contain start (ATG) or stop codons (TAG, TAA, TGA).
    - Must be Open Reading Frame (ORF) that is divisble by 3.
  - Proteins can contain any 1-letter code for the 20 amino acids as well as the 5 other non-canoncial amino acids:
    - B, J, O, U, X, Z
      - These are counted if "Protein" type is marked in the **Type** field.
      - They will be used to calculate length and MW, but will not be counted in the optional amino acid counts file.
    - Does not have to end with common stop codon indicators (*, -), though "STOP" is invalid.

For all these fields, please be aware of any leading or trailing white spaces.



















