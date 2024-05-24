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
4. Extinction Coefficient ( in M$^-1$cm$^-1$

The optional '-c' will provide generate the file above, plus an additional CSV file with each protein's amino acid breakdown (only 20 canconcial ones).

###Example
####Input file
| Name      | Type      | Sequence    |
| :---      | :---      | :---        |
|Protein1   | D         | ATGACGCGC   |
|Protein2   | RNA       | AUGAAUUUU   |
|Protein3   | Protein   | MTRREA      |

####Output file "Protein_results.csv"
| Name    | Type    | Sequence    | Translation  | Protein Length| MW (g/mol)| Extinction Coefficent|
| :---    | :---    | :---        | :---         | :---          | :---      | :---                 |
|Protein1 | D       | ATGACGCGC   | MTR          | 3             | 406.49    | 0
|Protein2 | RNA     | AUGAAUUAC   | MNY          | 3             | 426.47    | 1490
|Protein3 | Protein | MTRWEA      | MTRWEA       | 6             | 792.89    | 5500



