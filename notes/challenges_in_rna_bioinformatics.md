# Viral bioinformatics

## [Challenges in RNA virus bioinformatics](https://europepmc.org/article/MED/24590443)

 With few exceptions, most viral genomes are thus relatively poorly annotated and few computational tools and techniques have been developed specifically for the many idiosyncratic features of individual virus families.
 
### DISCOVERY OF VIRAL SEQUENCES

In many metagenomics applications, however, classification is not possible because the majority of sequences have no known reference genome or homolog (Edwards and Rohwer, 2005). In this case, de novo discovery of viral species can be performed by state-of-the-art de novo genome assemblers. These methods try to assemble the genomes of the major species in the sample, ignoring low-frequency variants and technical errors.
 
Intra-host virus populations consist of many related mutants, generated by mutation, recombination and selection. Even low-frequency variants can be of great interest, for example, because they may harbor drug resistance mutations (Barzon et al. , 2011), facilitate immune escape (Luciani et al. , 2012) or affect virulence (Töpfer et al. , 2013a). Estimating intra-host viral genetic diversity and reconstructing the individual haplotype sequences relies on both error correction and read assembly.

Current viral haplotype reconstruction tools, reviewed in Beerenwinkel et al. (2012), Beerenwinkel and Zagordi (2011) and Vrancken et al. (2010), can quantify viral diversity from NGS data, with recombinant population structure (Töpfer et al. , 2013b), provided that haplotypes differ enough, reads are not too short and coverage is high (Zagordi et al. , 2012). A common prerequisite for these tools is a high-quality alignment of the reads.

### STRUCTURAL RNA ELEMENTS

The realization that conserved RNA structure plays a role in virology dates back to the beginning of the 1980s (Ahlquist et al. , 1981). Most of the structured viral RNA elements contained in the Rfam database are cis-acting elements, in particular internal ribosomal entry sites (IRES), cis-acting replication elements and other elements located in the untranslated regions (UTRs) of RNA viruses. Functional RNA structures also appear to be abundant within the viral coding regions. Furthermore, regular arrangements of hairpins throughout the genomic RNA have been shown to be instrumental for packaging in Leviviridae (Dykeman et al. , 2011) and some satellite viruses (Schroeder et al. , 2011). Evolutionary conserved large-scale ordering of RNA virus genomes seems to be abundant in many animal and plant viruses (Davis et al. , 2008).

The first systematic searches for conserved, and hence likely functional, RNA secondary structure elements were performed in RNA viruses by Rauscher et al. , 1997.

This stimulated the development of early computational methods (Hofacker and Stadler, 1999; Hofacker et al. , 1998) capable of surveying alignments of complete virus genomes (Thurner et al. , 2004; Witwer et al. , 2001) for __local RNA motifs in which the structure is more conserved than the underlying sequence__ . Somewhat surprisingly, however, the next generation of comparative RNA secondary structure predictors such as RNAz (Washietl et al. , 2005) and evofold (Pedersen et al. , 2006) apparently have not been used extensively on virus data. The results of (Davis et al. , 2008) suggest that coverage with conserved secondary structure varies substantially between virus families.

Viral RNAs have recently become accessible to structural probing at larger scales using combinations of __SHAPE__ and sequencing. The analysis of these data requires both elaborate processing of the raw SHAPE data (Pang et al. , 2011) and the incorporation of these data into RNA structure prediction algorithms in the form of constraints (Reuter and Mathews, 2010; Washietl et al. , 2012). First results include the HCV 5′ UTR (Pang et al. , 2011) and the secondary structure of a complete HIV-1 genome (Watts et al. , 2009). As essentially all RNA molecules form secondary structures, one has to keep in mind that the entire structure is not necessarily of functional relevance.

[SHAPE](https://en.wikipedia.org/wiki/Nucleic_acid_structure_determination#SHAPE)
 
## [Know Your Enemy: Successful Bioinformatic Approaches to Predict Functional RNA Structures in Viral RNAs.](https://europepmc.org/article/MED/29354101)

## [Advanced molecular surveillance of hepatitis C virus.](https://europepmc.org/article/MED/25781918)


