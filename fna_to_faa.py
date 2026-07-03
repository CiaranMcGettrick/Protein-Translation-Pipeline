from Bio import SeqIO
from Bio.Seq import Seq
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

out = open(output_file, "w")

for record in SeqIO.parse(input_file, "fasta"):
    sequence = str(record.seq).upper()
    sequence = sequence.replace("U", "T")

    remainder = len(sequence) % 3
    if remainder != 0:
        sequence = sequence[:-remainder]

    protein = Seq(sequence).translate(table=1, stop_symbol="_", to_stop=False)
    protein = str(protein)

    out.write(">" + record.description + "\n")

    for i in range (0, len(protein), 40):
        out.write(protein[i:i+40] + "\n")

    out.write("\n")

out.close()
