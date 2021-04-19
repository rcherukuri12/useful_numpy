# this will remove empty columns in a loaded numpy matrix
# 
import numpy as np
from sklearn.datasets import load_svmlight_file
X,y = load_svmlight_file("./test.svm")
m = np.sum(X,axis=0) > 0.0
Xnew = X[:,np.nonzero(m)[1]]
print(X.shape)
print(Xnew.shape)
