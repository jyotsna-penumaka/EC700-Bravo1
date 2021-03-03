import pickle
import glcr
aa=glcr.longest_common_subsequence(None,'malware.txt','/glcr_cache',1)
with open('result_malware','wb') as f:
    pickle.dump(aa,f)