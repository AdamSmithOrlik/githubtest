#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[1]:


import numpy as np


# In[2]:


# Want to find the determinant of an NxN matrix
# Using the criss-cross symbolic method 


# # Functions

# In[198]:


def det(A):
    dim=np.shape(A)
    N=dim[0]
    assert N==dim[1], "Matrix must be NxN"
    if N==1:
        return A
    elif N==2:
        return A[0,0]*A[1,1]-A[0,1]*A[1,0]
    else:
        sA=symArray(A)
        print(sA)
        sA=symArray(A).flatten()
        M=np.shape(symArray(A))[1] # length of rows
        pdiag=0
        ndiag=0
        print("Pos")
        for n in range(0,N):
            diag=[sA[(m*N)+n] for m in twos(A)]
            print(diag)
            pdiag+=np.prod(diag) # sum of the product of diagonals
        print("Neg")
        for n in range(0,N):
            diag=[sA[(M-1)*m-n] for m in ones(A)]
            print(diag)
            ndiag+=np.prod(diag)  
        return pdiag-ndiag


# In[146]:


def symArray(A):
    N=np.shape(A)[0]
    extra=A[:,:N-1]
    return np.hstack((A,extra))

def twos(A):
    N=np.shape(A)[0]
    multiples=[]
    for n in range(N):
        m=2*n
        multiples.append(m)
    return multiples

def ones(A):
    N=np.shape(A)[0]
    multiples=[]
    for n in range(N):
        m=n+1
        multiples.append(m)
    return multiples


# # Tests

# In[201]:


a=np.random.randint(0,10,(3,3))
print(a)


# In[202]:


np.linalg.det(a)


# In[203]:


det(a)


# In[204]:


a


# In[ ]:




