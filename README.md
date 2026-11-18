# DNA Sequence AT/GC Content Calculator 🧬

An interactive command-line Python script designed for researchers and students to calculate the **GC** and **AT content** of DNA sequences. It includes built-in sequence validation, handling for lowercase/uppercase inputs, and quality control (QC) tracking for unknown or ambiguous nucleotides (`N`). <br>

> ⚠️ **Important Note:** This script is optimized for short sequences (up to ~1,000 bp). Pure Python loops are not designed to handle massive whole-genome files (like 1M+ bases).

## ✨ Features

* **Flexible Input Sanitization:** Automatically converts sequences to uppercase, strips leading/trailing whitespaces, and removes any embedded spaces.
* **Efficient Sequence Validation:** Utilizes Python's native **`for...else`** construct to cleanly validate sequence characters (`A`, `T`, `C`, `G`, `N`) without messy flag variables.
* **Ambiguous Base QC Warnings:** Detects 'N' bases (representing unknown nucleotides from sequencing data), calculates their percentage, and triggers a quality control warning.
* **Interactive Session Loop:** Allows users to analyze multiple sequences in a single run without restarting the script.

## 🚀 Getting Started

### Prerequisites
* **Python 3.x** installed on your system. No external libraries or dependencies are required!

### Running the Script
1. Clone the repository or download `DNA_AT_GC_Calculator.py`.
2. Open your terminal or command prompt in the project directory.
3. Run the script using Python:
   ```bash
   python DNA_AT_GC_Calculator.py
   ```

## 💡 Example Usage

### Input:
Enter the DNA sequence: ATGCCTCGCCTGTTTTTTTTCCACCTGCTAGGAGTCTGTTTACTACTGAACCAATTTTCCAGAGCAGTCG
CGGACTCATGGATGGAGGAAGTTATTAAATTATGCGGCCGCGAATTAGTTCGCGCGCAGATTGCCATTTG
CGGCATGAGCACCTGGAGCAAAAGGTCTCTGAGCCAGGAAGATGCTCCTCAGACACCTAGACCAGTGGCA
GGTGATTTTATTCAAACAGTCTCACTGGGAATCTCACCGGACGGAGGGAAAGCACTGAGAACAGGAAGCT
GCTTCACCCGAGAGTTCCTTGGTGCCCTTTCCAAATTGTGCCATCCTTCATCAACAAAGATACAGAAACC <br>
NNNNNNNNNNNNNNNNNNNNNNNNNN

### Output:
Length of the DNA sequence is: 376 <br>
The GC content of the DNA sequence is: 46.01063829787234 <br>
The AT content of the DNA sequence is: 47.07446808510639 <br>
WARNING! WARNING! WARNING! <br>
The DNA sequence requires quality control as it contains 'N' bases <br>
The 'N' bases in the DNA sequence, represent unknown nucleotides. <br>
The percentage of 'N' bases in the sequence is: 6.914893617021277 <br>
Please note these 'N' bases were not included in the AT or GC content calculation. <br>
But they were included in the total length of the sequence. <br>
Thank you for using the DNA GC and AT Content Calculator.

## 🛠️ Limitation

Currently, this script is built for localized analysis and only handles short sequences.

## 🧬 Why Track 'N' Bases?

In genomic sequencing, N represents regions of sequencing uncertainty or low-quality reads. Separately tracking and reporting their percentage helps wet-lab scientists and bioinformaticians assess data quality before downstream analysis.


## 📄 License

This project is open-source and available under the MIT License.