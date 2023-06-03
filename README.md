# PhindersKeepers
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://pypi.org/project/PhageOrder/)
This is a simple python script designed to help parse data from inphared.

## Acknowledgement
Hopefully Inphared keeps up the good work for the phage community...
We're all counting on you [Ryan Cook](https://github.com/RyanCook94/inphared)

## Install
```
pip install PhindersKeepers
```

## Usage
To see options
```
phinders_keepers.py --help
```

## Example using data from 1May2023
This command returns a single phage in the output directory, this phage is the Koomba-kaat_1 Silviavirus.
```
phinders_keepers.py -g 1May2023_genomes_excluding_refseq.fa -d 1May2023_data_excluding_refseq.tsv -o <PATH TO OUTPUT DIR> --query OP263969 --search Accession
```

## Output
In the output directory you will have:
* Individual fasta files with the genome accession number as the name of the file
* A 'data.tsv' with some information about each phage genome in this output directory
