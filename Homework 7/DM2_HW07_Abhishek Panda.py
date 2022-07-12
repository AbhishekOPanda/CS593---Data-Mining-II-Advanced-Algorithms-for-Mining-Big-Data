#!/usr/bin/env python
# coding: utf-8

# 
# # First Name : Abhishek 
# # Last Name : Ponda
# # CWID : 10478684
# # Purpose : Assignment - HW07

# In[1]:


# Import Packages


# In[2]:


import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from numpy.linalg import matrix_power


# In[3]:


# Define Graph


# In[4]:


G=nx.DiGraph()


# In[5]:


pgs = ["A","B","C","D","E","F"]
G.add_nodes_from(pgs)
print("Nodes of graph: ")
print(G.nodes())


# In[6]:


G.add_edges_from([
('A','B'),('A','C'),('A','D'),
('B','D'),
('C','A'),('C','B'),('C','D'),('C','E'),
('D','A'),('D','C'),
('E','F'),
('F','C')
])


# In[ ]:


G.edges()


# In[7]:


nx.draw(G, with_labels = True)
plt.show()


# In[8]:


adj_mt = np.array([[0,0,1,1,0,0],
                  [1,0,1,0,0,0],
                  [1,0,0,1,0,1],
                  [1,1,1,0,0,0],
                  [0,0,1,0,0,0],
                  [0,0,0,0,1,0]]
                 )
print('Adjancency Matrix:'  )
print(adj_mt)
tran_mt = np.array([[0,0,1/4,1/2,0,0],
                  [1/3,0,1/4,0,0,0],
                  [1/3,0,0,1/2,0,1],
                  [1/3,1,1/4,0,0,0],
                  [0,0,1/4,0,0,0],
                  [0,0,0,0,1,0]]
                 )

print('Transition Matrix:'  )
print( tran_mt)

rank0 = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6,])
rank0


# In[9]:


print(rank0.T)
rank1=np.matmul(tran_mt,rank0.T)
print(rank1)
rank2=np.matmul(tran_mt,rank1)
print(rank2)


# In[10]:


tran_mt50=matrix_power(tran_mt, 50)
rank51=np.matmul( tran_mt50,rank1)
print(rank51) 


# In[ ]:




