import os
from Bio import SeqIO

class GenBankRecord:
    """ """
    def __init__(self, genbank_filepath):
        """ """
        gb_records = list(SeqIO.parse(open(genbank_filepath,"r"), "genbank"))
        if len(gb_records) > 1:
            raise Exception("Accepts single record files only.")
        self.gb_record = gb_records[0]
        self.annotation_names = self._get_annotation_names()
    
    def _get_annotation_names(self):
        """Get the annnotation names as a list"""
        return list(self.gb_record.annotations)
    
    def get_sequence(self):
        """Get the record full sequence as a string."""
        return str(self.gb_record.seq)
    
    def get_first_accession(self):
        """ """
        return self.gb_record.annotations["accessions"][0]
    
    def get_id(self):
        """ """
        self.gb_record.id
    
    def get_annotation_map(self):
        """ """
        annotation_map = {}
        for annotation_name in self.annotation_names:
            annotation_map[annotation_name] = self.gb_record.annotations[annotation_name]
        return annotation_map

    def get_features_map(self):
        """ """
        features_map = dict()
        for feature in self.gb_record.features:
            if feature.type in features_map:
                features_map[feature.type].append(feature)
            else:
                features_map[feature.type] = []
                features_map[feature.type].append(feature)
        return features_map
    
class GenBankFeature:
    
    def __init__(self, feature, parent_sequence):
        self.feature = feature
        self.parent_sequence = parent_sequence
        self.feature_type = feature.type
        
    def get_parent_sequence(self):
        """ """
        return self.feature.parent_sequence
        
    def get_feature_map(self):
        """ """
        if self.feature.type == "gene":
            feature_map = self.gene_feature_map()
            return feature_map
        return {}
    
    def gene_feature_map(self):
        gene_sequence_map = dict()
        gene_name = self.feature.qualifiers["gene"][0]
        gene_sequence = self.feature.extract(self.parent_sequence)
        gene_sequence_map[gene_name] = str(gene_sequence)
        return gene_sequence_map
    
    def get_qualifiers(self):
        """ """
        return self.feature.qualifiers