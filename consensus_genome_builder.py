# Read in the .vcf file using Python pandas package
import pandas as pd 
path=(r'path to .vfc file')
vcf_full_file=pd.read_csv(path, sep='\t', skiprows=20)

# Query the data contained in the .vcf file with all the Carnica types
vcf_ff_carnica=vcf_full_file[["#CHROM", "POS", "REF", "ALT","FORMAT","CAR01", "CAR02", "CAR03", "CAR04", "CAR05", "CAR06", "CAR07", "CAR08", "CAR09", "CAR10", "CAR11", "CAR12", "CAR13", "CAR14", "CAR15", "CAR16", "CAR17", "CAR18", "CAR19", "CAR20", "CAR21", "CAR22", "CAR23", "CAR25", "CAR26", "CAR28", "CAR29", "CAR30", "CAR31", "Carnica_BE1", "Carnica_BE10", "Carnica_BE11", "Carnica_BE12", "Carnica_BE2", "Carnica_BE3", "Carnica_BE4", "Carnica_BE5", "Carnica_BE6", "Carnica_BE7", "Carnica_BE8", "Carnica_BE9", "Carnica_SL1", "Carnica_SL10", "Carnica_SL11", "Carnica_SL12", "Carnica_SL13", "Carnica_SL14", "Carnica_SL15", "Carnica_SL16", "Carnica_SL17", "Carnica_SL18", "Carnica_SL2", "Carnica_SL3", "Carnica_SL4", "Carnica_SL5","Carnica_SL6","Carnica_SL7", "Carnica_SL8","Carnica_SL9", "DEU17"]]

# Convert the dataframe into a list
full_list=vcf_ff_carnica.values.tolist()

# Obtain chromsome positions that would need to be replaced
    # 50% of the 1/1 occuring through out the Carnica types are taken into account
carnica_ff_output=open("carnica_changes_fullfile.txt", "w")
carnica_ff_output.write("#CHROM\tPOS\tREF\tALT\n")
for line in full_list:
    x=line[5::]
    y=x.count('1/1')
    z=y/len(x)
    if z >= 0.5:
        w=line[0:4]
        carnica_ff_output.write(str(w[0])+ "\t" + str(w[1])+ "\t"+ str(w[2])+ "\t" + str(w[3]) + "\n")
carnica_ff_output.close()

# Create a Python dictionary containing information of the alleles that would need to be replaced
chromosome_dict={}
with open("carnica_changes_fullfile.txt","r") as file:
    for line in file:
        if not line.startswith("#"):
            line=line.strip('\n').split('\t')
            i_dict = chromosome_dict.get(line[0])
            if i_dict is None:
                chromosome_dict.update({line[0]: {line[1]: (line[2], line[3])}})
            else:
                i_dict.update({line[1]: (line[2], line[3])})

# Use BioPython package SeqIO to construct the consensus genome
# A loop is created through the python dictionary to combine the A.mellifera reference genome and the new sequence containing the replaced alleles
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
name_dict={"ENA|CM009931|CM009931.2": "1", "ENA|CM009932|CM009932.2": "2", "ENA|CM009933|CM009933.2" : "3", "ENA|CM009934|CM009934.2" : "4", "ENA|CM009935|CM009935.2" : "5", "ENA|CM009936|CM009936.2" : "6", "ENA|CM009937|CM009937.2" : "7", "ENA|CM009938|CM009938.2" : "8", "ENA|CM009939|CM009939.2" : "9", "ENA|CM009940|CM009940.2" : "10", "ENA|CM009941|CM009941.2" : "11", "ENA|CM009942|CM009942.2" : "12", "ENA|CM009943|CM009943.2" : "13", "ENA|CM009944|CM009944.2" :"14", "ENA|CM009945|CM009945.2" : "15", "ENA|CM009946|CM009946.2" : "16"}
original_sequence=[]
new_sequences=[]
with open("Amel_HAv31.fasta", "r") as reference:
    for chromosome in SeqIO.parse(reference, "fasta"):
        name=name_dict.get(chromosome.id)
        if name is None:
            original_sequence.append(SeqRecord(Seq(chromosome), id=chromosome.id,description=""))
        else:
            new_seq=""
            position_dict=chromosome_dict.get(name)
            i=0
            for n in chromosome.seq:
                i+=1
                pos=position_dict.get(str(i))
                if pos is None:
                    new_seq+=n
                else:
                    if n != pos[0]:
                        print("Warning:This position does not exist")
                    else:
                        new_seq+=pos[1]
            new_sequences.append(SeqRecord(Seq(new_seq), id=chromosome.id, description=""))

combined_sequences=original_sequence + new_sequences

with open("output_consensus.fasta", "w") as output_file:
    SeqIO.write(combined_sequences, output_file, "fasta")
