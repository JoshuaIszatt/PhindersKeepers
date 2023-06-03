def main():

    from Bio import SeqIO
    import argparse
    import os
    import pandas as pd

    # Creating function to check directory path
    def valid_dir(dir_path):
        if not os.path.isdir(dir_path):
            raise argparse.ArgumentTypeError(
                f"{dir_path} is not a valid directory path")
        if not os.access(dir_path, os.R_OK):
            raise argparse.ArgumentTypeError(
                f"{dir_path} is not a readable directory")
        return dir_path

    def valid_file(file_path):
        if not os.path.isfile(file_path):
            raise argparse.ArgumentTypeError(
                f"{file_path} is not a valid file path")
        if not os.access(file_path, os.R_OK):
            raise argparse.ArgumentTypeError(
                f"{file_path} is not a readable file")
        return file_path

    def search_multifasta(name, multifasta_file, output_file):
        found_genomes = []
        with open(multifasta_file, 'r') as file:
            for record in SeqIO.parse(file, "fasta"):
                header = record.description
                if name in header:
                    found_genomes.append(record)
                    continue
        
        if found_genomes:
            print(f"Found genomes: {len(found_genomes)}")
            with open(output_file, 'w') as output:
                for genome in found_genomes:
                    SeqIO.write(genome, output, "fasta")
                    print(genome.description)
        else:
            print("No genomes found")

    # Adding arguments
    parser = argparse.ArgumentParser(description="Extract genomes from inphared multifasta and accompanying tsv file.\n(Tip: making and using a blastdb from the genomes is exponentially faster than this script...)")

    # Genomes file or blast db
    parser.add_argument("-g", "--genomes", required=True, type=valid_file, help="Path to the multifasta file")
    parser.add_argument("-o", "--output_dir", required=True, type=valid_dir, help="Directory to save the extracted genomes")
    parser.add_argument("-d", "--data", required=True, type=valid_file, help="TSV file matching the genomes")
    parser.add_argument("-q", "--query", required=True, help="Query string (E.g 'Staphylococcus')")
    parser.add_argument("-s", "--search", required=True, help="Header to search through (E.g 'Host')")
    args = parser.parse_args()

    genomes = os.path.abspath(args.genomes)
    outdir = os.path.abspath(args.output_dir)
    data = os.path.abspath(args.data)
    query = str(args.query)
    header = str(args.search)

    # Data frames
    df = pd.read_csv(data, sep='\t')
    df2 = pd.DataFrame(columns=["Accession", 
                            'Genome Length (bp)', 
                            'molGC (%)', 
                            'Number CDS', 
                            'Positive Strand (%)', 
                            'Negative Strand (%)', 
                            'Coding Capacity(%)', 
                            'tRNAs', 
                            'Host',
                            'Family',
                            'Genus'])

    rows = []
    for index, row in df.iterrows():
        if query in row[header]:
            extraction = os.path.join(f"{outdir}/{row['Accession']}.fasta")
            new_row = {
                'Accession': row['Accession'],
                'Genome Length (bp)': row['Genome Length (bp)'],
                'molGC (%)' : row['molGC (%)'] ,
                'Number CDS' : row['Number CDS'],
                'Positive Strand (%)' : row['Positive Strand (%)'],
                'Negative Strand (%)' : row['Negative Strand (%)'],
                'Coding Capacity(%)' : row['Coding Capacity(%)'],
                'tRNAs' : row['tRNAs'],
                'Host' : row['Host'],
                'Family' : row['Family'],
                'Genus' : row['Genus']
            }
            rows.append(new_row)
            
            if not os.path.exists(extraction):
                try:
                    search_multifasta(row['Accession'], genomes, extraction)
                except:
                    print(f"Error extracting {row['Accession']}")
            else:
                print(f"Genome already extracted: {row['Accession']}")

    df2 = pd.concat([df2, pd.DataFrame(rows)], ignore_index=True)
    df2.to_csv(f"{outdir}/data.tsv", index=False, sep='\t')

if __name__ == "__main__":
    exit(main())
