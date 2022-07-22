

Multiple sequence alignment (MSA) methods refer to a series of algorithmic solution for the alignment of evolutionarily related sequences, while taking into account evolutionary events such as mutations, insertions, deletions and rearrangements under certain conditions. 

These methods can be applied to DNA, RNA or protein sequences. 

A large number of in silico analyses depend on MSA methods:

- Domain analysis
- Phylogenetic reconstruction
- Motif finding

The newest generation of MSAMs have beeb designed to cater for evolutionary and structural modeling.

Shifting modeling needs can also drive the developments of novel heuristics, a fact well illustrated by the recent development of phylogeny-aware aligners. 

Another driving force behind the development of new heuristics has been the increasing availability of structural data that has fueled the development of hybrid methods able to simultaneously deal with sequences and secondary (RNA) or tertiary (RNA and proteins) structures.

Given a set of biological sequences (RNA, proteins, DNA), the purpose of a MSA method is to align the sequences in a way that will either reflect their evolutionary, functional or structural relationship.

In a correct MSA, aligned residues should be maximally similar according to some specified criteria. For instance, if the alignment is meant for evolutionary reconstruction, the residues should be homologous, that is to say, correspond to the same residue in the last unique common ancestor of the considered sequences. 

If the alignment is meant to be a structural model, aligned residues should have comparable positions in their respective 2D or 3D structures. If the alignment is functional, as may happen when analyzing genomic data, aligned positions are expected to support similar functions.

Two structures may be similar as a consequence of convergent evolution but non-homologous from an evolutionary point of view.

To build an MSA, one needs a scoring function (objective function) able to quantify the relative merits of any alternative alignment with respect to the modeled relationship. 

The MSA can then be estimated by computing an optimally scoring model. The objective function is a critical parameter, as it precisely defines the modeling accuracy of an MSA and its predictive capacity. When it comes to evolutionary reconstructions, the most commonly used objective functions involve maximizing weighted similarities (as provided by a PAM or BLOSUM substitution matrix) while using an affine gap penalty to estimate indels costs. The substitution cost can be adjusted using tree-based weighting schemes that reflect the independent information contribution of each sequence, and the score of columns is estimated by considering the total all-against-all (sums-of-pairs) substitution cost. 

The combination between a tree-based progressive strategy and a global pairwise alignment algorithm forms the backbone of most available methods, including ClustalW, T-Coffee and ProbCons. It is also particularly well adapted for the design of iterative strategies, involving reestimating trees and alignments until both converge, as implemented in MUSCLE, MAFFT and Clustal Omega.

A major milestone in the development of MSAMs has been the introduction of structure-based reference alignments that can be used to compare the relative capacities of various methods to reconstruct structurally correct alignments from sequence only. The choice of structure seems rather natural because 3D features are known to be more evolutionary resilient than the underlying sequences. On the other hand, this approach relies on the unproven rationale that structurally and evolutionary correct alignments are identical. 

Another major potential discrepancy between structural and evolutionary alignments results from convergent evolution. Whenever such a process has shaped some portions of a sequence data set, the resulting alignment matching convergent regions will be structurally correct and evolutionary false—and reciprocally.

Phylogeny-aware aligners

PRANK was one of the first. It relies on the idea that correct MSAs must have indels patterns properly reflecting the underlying phylogenetic tree. PRANK was rapidly followed by SATé, an iterative multiple aligner derived from MAFFT that attempts to estimate the MSA supporting the highest-scoring maximum likelihood tree. An important merit of this approach is to depart from the long-held assumption that the best MSA is the one maximizing similarity between sequences.

In the context of phylogeny-aware aligners, the best MSA is defined as the one yielding the best phylogenetic model.

It has been pointed out that phylogeneticists are usually dissatisfied with similarity-based alignments and tend to manually edit their MSAs to produce alignments more likely to reflect homology from a true evolutionary stand-point.

Thanks to its high evolutionary resilience, structural information can help produce high-quality models, especially in situations where one aims at modeling structural and functional relationships.

Structural information has long been known to be more resilient than its underlying sequence counterpart [Twilight zone of protein sequence alignments](https://academic.oup.com/peds/article/12/2/85/1550637)

