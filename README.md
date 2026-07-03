# Protein Translation Pipeline

## Description
A Python script for translating FASTA-formatted RNA nucleotide sequences into amino acid sequences using Biopython.


## Features
- Converts RNA (U) to DNA (T)
- Translates nucleotide sequences into protein sequences
- Preserves internal stop codons using "_"
- Automatically trims incomplete codons
- Outputs translated protein sequences in FASTA format

## Requirements
Python 3 and Biopython

Install Biopython: 
```bash
pip install biopython
```

## Usage
```bash
python fna_to_faa.py input.fna output.faa
```

Example:
```bash
python fna_to_faa.py chimera_inframe.fna chimera_test.faa
```

## Input

- FASTA (.fna)

## Output:

- Translated protein FASTA (.faa)

## Author 

Ciarán Mc Gettrick
