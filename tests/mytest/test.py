import pandas as pd
import numpy as np
from math import sqrt
from sklearn.metrics import mean_squared_error
from Bio.PDB import *

path='./'

import sys
sys.path.append("/home/liang/code/acdc-nn/acdc_nn")
import util
import nn

p53_pred_dir=list()
p53_pred_inv=list()

p53_dir=pd.read_csv('/home/liang/test_ddg.csv', sep=',',header= None)
p53_inv=p53_dir.copy()
print(p53_inv.columns)
p53_inv.loc[:,1]=p53_inv.loc[:,1].apply(lambda x : x[-1]+x[1:-1]+x[0])
p53_inv.loc[:,2]=p53_inv.loc[:,2].apply(lambda x : -x)


# building the specific model with cv weights

path_weights=path+"weights_cv/Weights_PostTL_CV_5"
num_H=[32,16]
d=0.2
ACDC_NN=nn.build_acdc_3d(num_H,d,25)[0]
ACDC_NN.load_weights(path_weights)

#Ssym dir prediction
for protein,mut in zip(list(p53_dir[0]),list(p53_dir[1])):

  prof_path ='/home/liang/code/acdc-nn/tests/profiles' + protein +'.prof' 
  pdb_path= '/home/liang/code/acdc-nn/tests/structures' + protein +'.pdb'
  chain = 'A'

  # information processing
  # get structure and other information
  structure, pchain, seq, d_seq2pdb, d_pdb2seq  = util.pdb2info(pdb_path, chain)
  prof = util.getProfile(prof_path)

  kvar=(mut[0],d_pdb2seq[mut[1:-1]],mut[-1])
  kvar_pdb=(mut[0],mut[1:-1],mut[-1])

  dist_neigh_3d= util.get_neigh_ps(kvar_pdb,5,d_seq2pdb,pchain) 
  list_dist_neigh_3d = dist_neigh_3d[kvar]

  # extracting features
  codif=util.getMutCod(mut)
  all_profile = util.Unified_prof(kvar[1],prof,seq, list_dist_neigh_3d)
  
  #dir 
  To_predict_dir=pd.DataFrame([*codif,*all_profile,*np.zeros(600-len(all_profile))]).T

  #inv (dir)
  To_predict_inv=To_predict_dir.copy()
  To_predict_inv.iloc[:,:20]=To_predict_inv.iloc[:,:20].replace([1.0,-1.0],[-1.0,1.0])
  
  # Making input in the proper shape 
  Xm_d, X1D_d, X3D_d = nn.mkInp(np.asarray(To_predict_dir).astype(np.float32),500)
  Xm_i, X1D_i, X3D_i = nn.mkInp(np.asarray(To_predict_inv).astype(np.float32),500)  

  #predict
  prediction=ACDC_NN.predict([X3D_d, X1D_d, Xm_d , X3D_i, X1D_i, Xm_i])
  p53_pred_dir.append(prediction[0][0][0])

#Ssym inv prediction
for protein,mut in zip(list(p53_inv[0]),list(p53_inv[1])):
  
  mut_dir=mut[-1]+mut[1:-1]+mut[0]
  prof_path ='/home/liang/code/acdc-nn/tests/profiles' + protein +'.prof' 
  pdb_path= '/home/liang/code/acdc-nn/tests/structures' + protein +'.pdb'
  chain = 'A'

  # information processing
  # get structure and other information
  structure, pchain, seq, d_seq2pdb, d_pdb2seq  = util.pdb2info(pdb_path, chain)
  prof = util.getProfile(prof_path)

  kvar=(mut[0],d_pdb2seq[mut[1:-1]],mut[-1])
  kvar_pdb=(mut[0],mut[1:-1],mut[-1])

  dist_neigh_3d= util.get_neigh_ps(kvar_pdb,5,d_seq2pdb,pchain) 
  list_dist_neigh_3d = dist_neigh_3d[kvar]

  # extracting features
  codif=util.getMutCod(mut)
  all_profile = util.Unified_prof(kvar[1],prof,seq, list_dist_neigh_3d)
  
  #dir
  To_predict_dir=pd.DataFrame([*codif,*all_profile,*np.zeros(600-len(all_profile))]).T
  
  #dir (inv)
  To_predict_inv=To_predict_dir.copy()
  To_predict_inv.iloc[:,:20]=To_predict_inv.iloc[:,:20].replace([1.0,-1.0],[-1.0,1.0])
  
  # Making input in the proper shape 
  Xm_d, X1D_d, X3D_d = nn.mkInp(np.asarray(To_predict_dir).astype(np.float32),500)
  Xm_i, X1D_i, X3D_i = nn.mkInp(np.asarray(To_predict_inv).astype(np.float32),500)  

  #predict
  prediction=ACDC_NN.predict([X3D_d, X1D_d, Xm_d , X3D_i, X1D_i, Xm_i])
  p53_pred_inv.append(prediction[0][0][0])

