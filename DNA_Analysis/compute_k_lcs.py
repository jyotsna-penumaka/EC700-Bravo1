import pickle
import glcr
aa=glcr.longest_common_subsequence(None,'benign_sequences_dna.txt','/glcr_cache',1)
with open('results_lcs','wb') as f:
    pickle.dump(aa,f)
