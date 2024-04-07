import numpy as np
import pandas as pd
import os
import openpyxl
import math
# This code pints vectors for a vector subspace of size min(NumberofVariantsinPools^2,2001) (when NumberofQuestionsInCommon=1) or min(NumberofVariantsinPools^3,2001) (when NumberofQuestionsInCommon=2) subset of GF(NumberofVariantsinPools)^30. 
# It also creates a data frame df where each row is a vector in GF(NumberofVariantsinPools)^{NumberofVariantsinPools+1}. If checking is set to be true, the program also checks that that each pair of vectors in the data frame has at most NNumberofQuestionsInCommon questions in common.
# The vector subspaces in GF(NumberofVariantsinPools)^{NumberofVariantsinPools+1} GF(NumberofVariantsinPools)^{NumberofVariantsinPools+2]GF(NumberofVariantsinPools)^{NumberofVariantsinPools+2} are the same as in the article https://www.tandfonline.com/doi/pdf/10.1080/0020739X.2023.2236612. 
# Each printed vector is contanicated copies of a vector in GF(NumberofVariantsinPools)^{NumberofVariantsinPools+1} or GF(NumberofVariantsinPools)^{NumberofVariantsinPools+2}.  
#########################################################################################
NumberofVariantsinPools = int(input("Enter the size of each question pool: (Only 3,4,5,7,8,9,11,13,17,19,23 and 29 are valid)"))
NumberofQuestionsInCommon = int(input("Enter the number of questions in common: (Only 1 or 2 are valid)"))
checking=True # If you want to verify the statement of theorem for the above values, turn this to true and good luck. It may take a few hours for c=2 and big n. Otherwise, a file with all arrays is created.
##########################################################################################
cttwo=NumberofVariantsinPools*NumberofVariantsinPools
ctthree=NumberofVariantsinPools*NumberofVariantsinPools*NumberofVariantsinPools
##########################################################################################
if NumberofVariantsinPools>13:
 subsetsize=2001
else:
  subsetsize=ctthree
startsubsetindex=cttwo
endsubsetindex=subsetsize+startsubsetindex
##########################################################################################
if NumberofQuestionsInCommon==1:
  ct=cttwo #Maximum assessment variant count available for  
  nnewsq=1
  b=1
  numcols=NumberofVariantsinPools
elif NumberofQuestionsInCommon==2:
  ct=ctthree
  nnewsq=NumberofVariantsinPools
  b=0
else:
  print("You entered wrong number for maximum number of questions in common.")
#########################################################################################
countingthirty=int(30) #The number of questions in each assessment.
#########################################################################################
if ((NumberofVariantsinPools==4) or (NumberofVariantsinPools==8)) and b==0:
    numcols=NumberofVariantsinPools+1
else:
    numcols=NumberofVariantsinPools
#########################################################################################
cols=[]
numbtxt=["zero", "one", "two", "three", "four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","twentyone","twentytwo","twentythree","twentyfour","twentyfive","twentysix","twentyseven","twentyeight","twentynine","thirty"]
for i in range(numcols+1):
 cols.append(numbtxt[i])
rows = []
if (NumberofVariantsinPools==3) or (NumberofVariantsinPools==5) or (NumberofVariantsinPools==7) or (NumberofVariantsinPools==11) or (NumberofVariantsinPools==13) or (NumberofVariantsinPools==17) or (NumberofVariantsinPools==19) or (NumberofVariantsinPools==23) or (NumberofVariantsinPools==29):
#########################################################################################
 countingn=int(math.ceil(countingthirty/(NumberofVariantsinPools+1))+b)
 countingsize=0
 for k in range(nnewsq): # Coefficients i, j, k are used to create linear combination of two or three vectors.
    for j in range(NumberofVariantsinPools):
      for i in range(NumberofVariantsinPools):
        gen=[]
        counting=countingthirty
        countingsize=countingsize+1
        for p in range(countingn): # This loops produces a vector in GF(NumberofVariantsinPools)^30 by creating copies.
          for m in range(NumberofVariantsinPools): # Using m creates two of the vector basis: <0,1,2,3,...> and <0,1,4,9,...>. 
            x=((m*j)%NumberofVariantsinPools)
            y=((m*m*k)%NumberofVariantsinPools)
            if p==0:
              gen.append((i+x+y)%NumberofVariantsinPools)
            if (countingsize>startsubsetindex and countingsize<=endsubsetindex) or b==1:
              if counting>1:
                print((i+x+y)%NumberofVariantsinPools,end="")
                print("/",end="")
              elif counting==1:
                print((i+x+y)%NumberofVariantsinPools,end="")
                print(",",end="")
            counting=counting-1
          if counting>1 and b==1:
            print(j,end="")
            print("/",end="")
          elif counting==1 and b==1:
            print(j,end="")
            print(",",end="")
          if countingsize>startsubsetindex and countingsize<=endsubsetindex:
            if counting>1 and b==0:
              print(k,end="")
              print("/",end="")
            elif counting==1 and b==0:
              print(k,end="")
              print(",",end="")
          if b==1 and p==0:
            gen.append(j)
          elif b==0 and p==0:
            gen.append(k)
          counting=counting-1
          if p==0: #This appends one copy of each vector to df.
            genelem=[]
            for m in range(numcols+1):
              genelem.append(gen[m])
            rows.append(genelem)
#########################################################################################
elif NumberofVariantsinPools==4:
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
 for m in range(NumberofVariantsinPools):
  genfoursquared.append(genfour[m][m])
########
 def fouradd(x,y):
  result=genfouradd[x][y]
  return result
#########################################################################################
 countingn=int(math.ceil(countingthirty/(n+2))+b)
 for k in range(nnewsq):  # Coefficients i, j, k are used to create linear combination of two or three vectors.
    for j in range(NumberofVariantsinPools):
      for i in range(NumberofVariantsinPools):
        counting=countingthirty
        for p in range(countingn): # This loops produces a vector in GF(NumberofVariantsinPools)^30 by creating copies.
          gen=[]
          for m in range(NumberofVariantsinPools): # Using m creates two of the vector basis: <0,1,2,3,...> and <0,1,4,9,...>.
            x=genfour[m][j]
            y=genfour[genfoursquared[m]][k]
            if p==0:
              gen.append(fouradd(fouradd(i,x),y))
            if counting>1:
              print(fouradd(fouradd(i,x),y),end="")
              print("/",end="")
            elif counting==1:
              print(fouradd(fouradd(i,x),y),end="")
              print(",",end="")
            counting=counting-1
          if b==1 and p==0:
            gen.append(j)
          if b==0 and p==0:
            gen.append(j)
            gen.append(k)
          if counting>1:
            print(j,end="")
            print("/",end="")
          if counting==1:
            print(j,end="")
            print(",",end="")
          counting=counting-1
          if counting>1 and b==0:
            print(k,end="")
            print("/",end="")
          if counting==1 and b==0:
            print(k,end="")
            print(",",end="")
          if b==0:
            counting=counting-1
          if p==0: #This appends one copy of each vector to df.
            genelem=[]
            for m in range(numcols+1):
              genelem.append(gen[m])
            rows.append(genelem)
elif NumberofVariantsinPools==8:
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
 for m in range(NumberofVariantsinPools):
  geneightsquared.append(geneight[m][m])
########
 def eightadd(x,y):
  result=geneightadd[x][y]
  return result
#########################################################################################
 countingn=int(math.ceil(countingthirty/(n+2))+b)
 for k in range(nnewsq):  # Coefficients i, j, k are used to create linear combination of two or three vectors.
    for j in range(NumberofVariantsinPools):
      for i in range(NumberofVariantsinPools):
        counting=countingthirty
        for p in range(countingn):  # This loops produces a vector in GF(NumberofVariantsinPools)^30 by creating copies.
          gen=[]
          for m in range(NumberofVariantsinPools): # Using m creates two of the vector basis: <0,1,2,3,...> and <0,1,4,9,...>.
            x=geneight[m][j]
            y=geneight[geneightsquared[m]][k]
            if p==0:
              gen.append(eightadd(eightadd(i,x),y))
            if counting>1:
              print(eightadd(eightadd(i,x),y),end="")
              print("/",end="")
            elif counting==1:
              print(eightadd(eightadd(i,x),y),end="")
              print(",",end="")
            counting=counting-1
          if b==1 and p==0:
            gen.append(j)
          if b==0 and p==0:
            gen.append(j)
            gen.append(k)
          if counting>1:
            print(j,end="")
            print("/",end="")
          if counting==1:
            print(j,end="")
            print(",",end="")
          counting=counting-1
          if counting>1 and b==0:
            print(k,end="")
            print("/",end="")
          if counting==1 and b==0:
            print(k,end="")
            print(",",end="")
          if b==0:
            counting=counting-1
          if p==0: #This appends one copy of each vector to df.
            genelem=[]
            for m in range(numcols+1):
              genelem.append(gen[m])
            rows.append(genelem)
elif NumberofVariantsinPools==9:
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
 for m in range(NumberofVariantsinPools):
  genninesquared.append(gennine[m][m])
########
 def nineadd(x,y):
  result=gennineadd[x][y]
  return result
#########################################################################################
 countingn=int(math.ceil(countingthirty/(NumberofVariantsinPools+1))+b)
 for k in range(nnewsq):  # Coefficients i, j, k are used to create linear combination of two or three vectors.
    for j in range(NumberofVariantsinPools):
      for i in range(NumberofVariantsinPools):
        gen=[]
        counting=countingthirty
        for p in range(countingn):  # This loops produces a vector in GF(NumberofVariantsinPools)^30 by creating copies.
          for m in range(NumberofVariantsinPools): # Using m creates two of the vector basis: <0,1,2,3,...> and <0,1,4,9,...>.
            x=gennine[m][j]
            y=gennine[genninesquared[m]][k]
            if p==0:
              gen.append(nineadd(nineadd(i,x),y))
            if counting>1:
              print(nineadd(nineadd(i,x),y),end="")
              print("/",end="")
            elif counting==1:
              print(nineadd(nineadd(i,x),y),end="")
              print(",",end="")
            counting=counting-1
          if counting>1 and b==1:
            print(j,end="")
            print("/",end="")
          elif counting==1 and b==1:
            print(j,end="")
            print(",",end="")
          if counting>1 and b==0:
            print(k,end="")
            print("/",end="")
          elif counting==1 and b==0:
            print(k,end="")
            print(",",end="")
          if b==1 and p==0:
            gen.append(j)
          elif b==0 and p==0:
            gen.append(k)
          counting=counting-1
          if p==0: # This appends one copy of each vector to df.
            genelem=[]
            for m in range(numcols+1):
              genelem.append(gen[m])
            rows.append(genelem)
#########################################################################################
else:
  print("You entered the wrong number.")
print()
if checking==True:
  df = pd.DataFrame(rows, columns=cols)
  with pd.option_context('display.max_rows', None,'display.max_columns', None,'display.precision', 3):
    print(df)
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
  if NumberofQuestionsInCommon==1:
    print("A set of size ", ct," of assessment variants was created and we checked ",int(ct*(ct-1)/2),"pairs of aseessment variants.")
  elif NumberofQuestionsInCommon==2:
    print("A set of size ", ct," of assessment variants was created and we checked ",int(ct*(ct-1)/2),"pairs of aseessment variants.")
    print("Pairs with 0 common questions:",okzero,"--Pairs with 1 common question:",okone,"--Pairs with 2 common questions:",oktwo,"--Pairs with more than 2 common questions:",pairerror)
  if NumberofQuestionsInCommon==1:
    print("Total number of pairs with strictly less that 2 questions in common:",okzero+okone)
  elif NumberofQuestionsInCommon==2:
    print("Total number of pairs with strictly less that 3 questions in common:",okzero+okone+oktwo)
    print("Total Pairs checked: ",okzero+okone+oktwo+pairerror )
  else:
    directory = 'Excel Files'
    nstr=str(NumberofVariantsinPools)
    cstr=str(c)
    file = nstr + '-' + cstr+ r'Pools.xlsx'
    #%%
    if not os.path.exists(directory):
        os.makedirs(directory)
    #%%
    df.to_excel(os.path.join(directory, file))
