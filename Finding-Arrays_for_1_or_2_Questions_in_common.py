import numpy as np
import pandas as pd
import os
import openpyxl
# This code creates arrays for n^3 assessment variants. It checks the first n^2 for 1 question in common if entered b=1. It checks the entire set for two questions in common if b=2.
#########################################################################################
n=5
n = int(input("Enter the size of each question pool: (3,4,5,7,8,9,11,13,17 or 19 are accpeted only)"))
c = int(input("Enter the number of questions in common: (1 or 2 are accepted only)"))
checking=True # If you want to verify the statement of theorem for the above values, turn this to true and good luck. It may take a few hours for c=2 and big n. Otherwise, a file with all arrays is created.
##########################################################################################
cttwo=n*n
ctthree=n*n*n
if c==1:
  ct=cttwo
  b=1
  numcols=n
elif c==2:
  ct=ctthree
  b=0
#########################################################################################
  if (n==4) or (n==8):
    numcols=n+1
  else:
    numcols=n  
#########################################################################################
else:
  print("Error")  

cols=[]
numbtxt=["zero", "one", "two", "three", "four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
for i in range(numcols+1):
 cols.append(numbtxt[i]) 
rows = []
if (n==3) or (n==5) or (n==7) or (n==11) or (n==13) or (n==17) or (n==19):
 for k in range(n):
  for i in range(n):
    for  j in range(n):
        gen=[]
        gen=[k+b*j,(i+j+k)%n,(i+2*j+4*k)%n,(i+3*j+9*k)%n,(i+4*j+16*k)%n,(i+5*j+25*k)%n,(i+6*j+36*k)%n,(i+7*j+49*k)%n,(i+8*j+64*k)%n,(i+9*j+81*k)%n,(i+10*j+100*k)%n,(i+11*j+121*k)%n,(i+12*j+144*k)%n,(i+13*j+169*k)%n,(i+14*j+196*k)%n,(i+15*j+225*k)%n,(i+16*j+256*k)%n,(i+17*j+289*k)%n,(i+18*j+324*k)%n,(i+19*j+361*k)%n]
        genelem=[]
        for m in range(numcols+1):
          genelem.append(gen[m])         
        rows.append(genelem)
elif n==4:
#########################################################################################
########     Multiplication Table:
 genfour=[[0,0,0,0],
          [0,1,2,3],
          [0,2,3,1],
          [0,3,1,2]]  
########
########      Addition Table:
 genfouradd=[ 
    [0,1,2,3],
    [1,0,3,2],
    [2,3,0,1],
    [3,2,1,0]]
########
########      Squre of elements:
 genfoursquared=[]
 for m in range(n):
  genfoursquared.append(genfour[m][m]) 
########
 def fouradd(x,y):
  result=genfouradd[x][y]
  return result
#########################################################################################
 for k in range(n):
   for i in range(n):
    for  j in range(n):
        if b==1:
          gen=[j]
        else:
          gen=[j,k]  
        for m in range(n):
          x=genfour[m][j]
          y=genfour[genfoursquared[m]][k]
          gen.append(fouradd(fouradd(i,x),y))
        genelem=[]
        for m in range(numcols+1):
          genelem.append(gen[m])         
        rows.append(genelem)  
elif n==8:  
#########################################################################################
########     Multiplication Table:
 geneight=[[0,0,0,0,0,0,0,0],
           [0,1,2,3,4,5,6,7],
           [0,2,4,6,3,1,7,5],
           [0,3,6,5,7,4,1,2],
           [0,4,3,7,6,2,5,1],
           [0,5,1,4,2,7,3,6],
           [0,6,7,1,5,3,2,4],
           [0,7,5,2,1,6,4,3]]
########
########      Addition Table:
 geneightadd=[ 
    [0,1,2,3,4,5,6,7],
    [1,0,3,2,5,4,7,6],
    [2,3,0,1,6,7,4,5],
    [3,2,1,0,7,6,5,4],  
    [4,5,6,7,0,1,2,3], 
    [5,4,7,6,1,0,3,2],
    [6,7,4,5,2,3,0,1],
    [7,6,5,4,3,2,1,0]]
########
########      Squre of elements:
 geneightsquared=[]
 for m in range(n):
  geneightsquared.append(geneight[m][m]) 
########
 def eightadd(x,y):
  result=geneightadd[x][y]
  return result
#########################################################################################
 for k in range(n):
   for i in range(n):
    for  j in range(n):
        if b==1:
          gen[j]
        else:
          gen=[j,k] 
        for m in range(n):
          x=geneight[m][j]
          y=geneight[geneightsquared[m]][k]
          gen.append(eightadd(eightadd(i,x),y))
        genelem=[]
        for m in range(numcols+1):
          genelem.append(gen[m])         
        rows.append(genelem) 
elif n==9:
#########################################################################################
########     Multiplication Table:
 gennine=[[0,0,0,0,0,0,0,0,0],[0,1,2,3,4,5,6,7,8],
    [0,2,1,6,8,7,3,5,4], 
    [0,3,6,2,5,8,1,4,7], 
    [0,4,8,5,6,1,7,2,3], 
    [0,5,7,8,1,3,4,6,2], 
    [0,6,3,1,7,4,2,8,5], 
    [0,7,5,4,2,6,8,3,1],
    [0,8,4,7,3,2,5,1,6]]
########
########      Addition Table:
 gennineadd=[ 
    [0,1,2,3,4,5,6,7,8],
    [1,2,0,4,5,3,7,8,6],
    [2,0,1,5,3,4,8,6,7],
    [3,4,5,6,7,8,0,1,2],
    [4,5,3,7,8,6,1,2,0],
    [5,3,4,8,6,7,2,0,1],
    [6,7,8,0,1,2,3,4,5],
    [7,8,6,1,2,0,4,5,3],
    [8,6,7,2,0,1,5,3,4]]
########
########      Squre of elements:
 genninesquared=[]
 for m in range(n):
  genninesquared.append(gennine[m][m]) 
########
 def nineadd(x,y):
  result=gennineadd[x][y]
  return result
#########################################################################################
 for k in range(n):
   for i in range(n):
    for  j in range(n):
        gen=[k+b*j]
        for m in range(n):
          x=gennine[m][j]
          y=gennine[genninesquared[m]][k]
          gen.append(nineadd(nineadd(i,x),y))
        genelem=[]
        for m in range(numcols+1):
          genelem.append(gen[m])         
        rows.append(genelem)      
else:
  print("You entered a wrong number.")   

df = pd.DataFrame(rows, columns=cols)
with pd.option_context('display.max_rows', None,'display.max_columns', None,'display.precision', 3):
  print(df) 
if checking==True:
  okzero=0
  okone=0
  oktwo=0
  pairerror=0
  for k in range(ct):
    for m in range(k+1,ct):
      j=0
      for col in cols:
        x=df.loc[k][col]
        y=df.loc[m,col]
        if x==y:
          j=j+1
      if j>2:
        pairerror=pairerror+1
      elif j==0:
        okzero=okzero+1
      elif j==1:
        okone=okone+1
      elif j==2:
        oktwo=oktwo+1
      else:  
        pairerror=pairerror+1
  if c==1:
    print("A set of size ", ct," of assessment variants was created and we checked ",int(ct*(ct-1)/2),"pairs of aseessment variants.")
  elif c==2:
    print("A set of size ", ct," of assessment variants was created and we checked ",int(ct*(ct-1)/2),"pairs of aseessment variants.")      
    print("Pairs with 0 common questions:",okzero,"--Pairs with 1 common question:",okone,"--Pairs with 2 common questions:",oktwo,"--Pairs with more than 2 common questions:",pairerror)
  if c==1:
    print("Total number of pairs with strictly less that 2 questions in common:",okzero+okone)
  elif c==2: 
    print("Total number of pairs with strictly less that 3 questions in common:",okzero+okone+oktwo)
    print("Total Pairs checked: ",okzero+okone+oktwo+pairerror )
else:
  directory = 'Excel Files'
  nstr=str(n)
  cstr=str(c)
  file = nstr + '-' + cstr+ r'Pools.xlsx'
  #%%
  if not os.path.exists(directory):
      os.makedirs(directory)
  #%%
  df.to_excel(os.path.join(directory, file))    
