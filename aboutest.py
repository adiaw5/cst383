from sdbindex  import *
import sys

index = Index(None, "colname", 0)
index.entries = []

# insert entries with values 102..300 by 2

for i in range(100):
   index.insert(i, 300-2*i)
   
