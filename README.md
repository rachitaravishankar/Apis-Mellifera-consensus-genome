# Constructing a consensus genome on the example of Apis Mellifera 

## Table of Contents 
#### i. Introduction
#### ii. Resources 
#### iii. Remarks and Future Direction

### i. INTRODUCTION
A consensus genome is a haploid linear genome which incorporates more of the allelic variation information by replacing the minor allele of the gene with its major allele in a reference genome. The aim of this project was to construct a consensus genome for Apis mellifera. 

The current reference genome for this species, Amel_HAv3.1 with the accession number GCA_003254395.2 was constructed using multiple long read technologies like PacBio, 10x chromium, Bionano and Hi-C using DNA from one haploid male drone from a mixed European genetic background (line DH4). 

A. mellifera has almost 30 subspecies whose morphological, behavioural, physiological and ecological characteristics have been defined. This information has been taken into account to build the reference genome for A. mellifera.

Studies investigating their health on a molecular level could potentially benefit from a consensus genome which better represents the species or a specific population. Constructing a consensus genome for this species will also aid invaluable research investigating recombination hotspots and haplotype structure.

As proof of concept the consensus genome has been constructed using the Carnica subspecies. The code was written in Python. 

### ii. RESOURCES
The A. mellifera refernece genome was donloaded through this link "https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_003254395.2/" onto BASH command line. 

Two of the datasets that were utilized in this project were downloaded through the public website made available through Wragg et al., (2022) "https://datashare.ed.ac.uk/handle/10283/3852". 
  
The first dataset is a metadata set – a .csv file containing genotype data of 698 honeybee 204 haploid drones representing samples from 14 different countries and 7 genetic types. 
  
The second data set which was also the main source of information was a .vcf file. The Wragg et al., (2022) study sequenced 870 samples for SNP detection and the detailed genetic analysis used 629 samples. The whole .vcf file is 298.9Mb in size. 

### iii. REMARKS AND FUTURE DIRECTION
This is just the first step towards building a comprehensive consensus genome for the A. mellifera species. The current form of the consensus genome has been constructed for the Carnica type, but it would be ideal to see consensus genomes constructed for each of the
honey bee type.

The consensus genome would also need to be incorporated with the INDELS information which unfortunately have not been quality filtered but have been made publicly available by Wragg et al., (2022).




*For more information and insights please feel free to get in touch with me*
