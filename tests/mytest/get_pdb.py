import csv
import os
from Bio import PDB
from Bio.PDB import *
def download_pdb_and_rename(pdb_id, uniprot_id):
    pdbl = PDB.PDBList()
    pdb_path = pdbl.retrieve_pdb_file(pdb_id, pdir='.', file_format='pdb')
    os.rename(pdb_path, f"{uniprot_id}.pdb")

with open('/home/liang/test_ddg.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        pdb_id = row['pdb_id']
        uniprot_id = row['uniprot_id']
        download_pdb_and_rename(pdb_id, uniprot_id)
