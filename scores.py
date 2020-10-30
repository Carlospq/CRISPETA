#Calculates the Rule set 2 score for the given 30-mer
#Input: 1. 30mer sgRNA+context sequence, NNNN[sgRNA sequence]NGGNNN
#       2. Amino acid cut position, for full model prediction only
#       3. Percent peptide, for full model prediction only
#Output: Rule set 2 score

import sys
import pandas as pd
import csv, argparse, sys
import pickle
import model_comparison
import sklearn

model_file_1 = 'saved_models/V3_model_nopos.pickle'
model_file = model_file_1
with open(model_file, 'rb') as f:
    model= pickle.load(f)

fi = open(sys.argv[1], 'r')
for line in fi:

    if line.startswith(">"):
        continue

    seq = line.strip().upper()  
    if "N" in seq:
        continue
    if len(seq)!=30: 
        continue
    
    if seq[25:27] == 'GG':
        score = model_comparison.predict(seq, -1, -1, model=model)
        print '%.4f'% (score)