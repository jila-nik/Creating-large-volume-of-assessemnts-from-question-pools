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
NumberofVariantsinPools = int(input("Enter the size of each question pool: (Only 3,4,5,7,8,9,11,13,16,17,19,23,25,27 and 29 are valid)"))
NumberofQuestionsInCommon = int(input("Enter the number of questions in common: (Only 1 or 2 are valid)"))
checking=False # If you want to verify the statement of theorem for the above values, turn this to true. It may take a few hours for c=2 and big n. Otherwise, a file with all arrays is created.
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
if ((NumberofVariantsinPools==4) or (NumberofVariantsinPools==8) or (NumberofVariantsinPools==16)) and b==0:
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
elif NumberofVariantsinPools==16:
#########################################################################################
#########################################################################################
########     Multiplication Table:
 gensixteen=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                [0, 2, 4, 6, 8, 10, 12, 14, 3, 1, 7, 5, 11, 9, 15, 13],
                [0, 3, 6, 5, 12, 15, 10, 9, 11, 8, 13, 14, 7, 4, 1, 2],
                [0, 4, 8, 12, 3, 7, 11, 15, 6, 2, 14, 10, 5, 1, 13, 9],
                [0, 5, 10, 15, 7, 2, 13, 8, 14, 11, 4, 1, 9, 12, 3, 6],
                [0, 6, 12, 10, 11, 13, 7, 1, 5, 3, 9, 15, 14, 8, 2, 4],
                [0, 7, 14, 9, 15, 8, 1, 6, 13, 10, 3, 4, 2, 5, 12, 11],
                [0, 8, 3, 11, 6, 14, 5, 13, 12, 4, 15, 7, 10, 2, 9, 1],
                [0, 9, 1, 8, 2, 11, 3, 10, 4, 13, 5, 12, 6, 15, 7, 14],
                [0, 10, 7, 13, 14, 4, 9, 3, 15, 5, 8, 2, 1, 11, 6, 12],
                [0, 11, 5, 14, 10, 1, 15, 4, 7, 12, 2, 9, 13, 6, 8, 3],
                [0, 12, 11, 7, 5, 9, 14, 2, 10, 6, 1, 13, 15, 3, 4, 8],
                [0, 13, 9, 4, 1, 12, 8, 5, 2, 15, 11, 6, 3, 14, 10, 7],
                [0, 14, 15, 1, 13, 3, 2, 12, 9, 7, 6, 8, 4, 10, 11, 5],
                [0, 15, 13, 2, 9, 6, 4, 11, 1, 14, 12, 3, 8, 7, 5, 10]]
########
########      Addition Table:
 gensixteenadd=[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],
                [2, 3, 0, 1, 6, 7, 4, 5, 10, 11, 8, 9, 14, 15, 12, 13],
                [3, 2, 1, 0, 7, 6, 5, 4, 11, 10, 9, 8, 15, 14, 13, 12],
                [4, 5, 6, 7, 0, 1, 2, 3, 12, 13, 14, 15, 8, 9, 10, 11],
                [5, 4, 7, 6, 1, 0, 3, 2, 13, 12, 15, 14, 9, 8, 11, 10],
                [6, 7, 4, 5, 2, 3, 0, 1, 14, 15, 12, 13, 10, 11, 8, 9],
                [7, 6, 5, 4, 3, 2, 1, 0, 15, 14, 13, 12, 11, 10, 9, 8],
                [8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7],
                [9, 8, 11, 10, 13, 12, 15, 14, 1, 0, 3, 2, 5, 4, 7, 6],
                [10, 11, 8, 9, 14, 15, 12, 13, 2, 3, 0, 1, 6, 7, 4, 5],
                [11, 10, 9, 8, 15, 14, 13, 12, 3, 2, 1, 0, 7, 6, 5, 4],
                [12, 13, 14, 15, 8, 9, 10, 11, 4, 5, 6, 7, 0, 1, 2, 3],
                [13, 12, 15, 14, 9, 8, 11, 10, 5, 4, 7, 6, 1, 0, 3, 2],
                [14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4, 5, 2, 3, 0, 1],
                [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
########
########      Squre of elements:
 gensixteensquared=[]
 for m in range(NumberofVariantsinPools):
  gensixteensquared.append(gensixteen[m][m])
########
 def sixteenadd(x,y):
  result=gensixteenadd[x][y]
  return result
#########################################################################################
 countingn=int(math.ceil(countingthirty/(NumberofVariantsinPools+2))+b)
 countingsize=0
 for k in range(nnewsq): # Coefficients i, j, k are used to create linear combination of two or three vectors.
    for j in range(NumberofVariantsinPools):
      for i in range(NumberofVariantsinPools):
        gen=[]
        counting=countingthirty
        countingsize=countingsize+1
        for p in range(countingn): # This loops produces a vector in GF(NumberofVariantsinPools)^30 by creating copies.
          for m in range(NumberofVariantsinPools): # Using m creates two of the vector basis: <0,1,2,3,...> and <0,1,4,9,...>.
            x=gensixteen[m][j]
            y=gensixteen[gensixteensquared[m]][k]
            if p==0:
              gen.append(sixteenadd(sixteenadd(i,x),y))
            if (countingsize>startsubsetindex and countingsize<=endsubsetindex) or b==1:
              if counting>1:
                print(sixteenadd(sixteenadd(i,x),y),end="")
                print("/",end="")
              elif counting==1:
                print(sixteenadd(sixteenadd(i,x),y),end="")
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
              print(j,end="")
              print(",",end="")
          if b==1 and p==0:
            gen.append(j)
          elif b==0 and p==0:
            gen.append(j)
            gen.append(k)
          counting=counting-1
          if p==0: #This appends one copy of each vector to df.
            genelem=[]
            for m in range(numcols+1):
              genelem.append(gen[m])
            rows.append(genelem)
#########################################################################################
elif NumberofVariantsinPools==25:
#########################################################################################
#########################################################################################
########     Multiplication Table:
 gentwentyfive=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24] ,
[0, 2, 4, 1, 3, 10, 12, 14, 11, 13, 20, 22, 24, 21, 23, 5, 7, 9, 6, 8, 15, 17, 19, 16, 18] ,
[0, 3, 1, 4, 2, 15, 18, 16, 19, 17, 5, 8, 6, 9, 7, 20, 23, 21, 24, 22, 10, 13, 11, 14, 12] ,
[0, 4, 3, 2, 1, 20, 24, 23, 22, 21, 15, 19, 18, 17, 16, 10, 14, 13, 12, 11, 5, 9, 8, 7, 6] ,
[0, 5, 10, 15, 20, 9, 14, 19, 24, 4, 13, 18, 23, 3, 8, 17, 22, 2, 7, 12, 21, 1, 6, 11, 16] ,
[0, 6, 12, 18, 24, 14, 15, 21, 2, 8, 23, 4, 5, 11, 17, 7, 13, 19, 20, 1, 16, 22, 3, 9, 10] ,
[0, 7, 14, 16, 23, 19, 21, 3, 5, 12, 8, 10, 17, 24, 1, 22, 4, 6, 13, 15, 11, 18, 20, 2, 9] ,
[0, 8, 11, 19, 22, 24, 2, 5, 13, 16, 18, 21, 4, 7, 10, 12, 15, 23, 1, 9, 6, 14, 17, 20, 3] ,
[0, 9, 13, 17, 21, 4, 8, 12, 16, 20, 3, 7, 11, 15, 24, 2, 6, 10, 19, 23, 1, 5, 14, 18, 22] ,
[0, 10, 20, 5, 15, 13, 23, 8, 18, 3, 21, 6, 16, 1, 11, 9, 19, 4, 14, 24, 17, 2, 12, 22, 7] ,
[0, 11, 22, 8, 19, 18, 4, 10, 21, 7, 6, 17, 3, 14, 20, 24, 5, 16, 2, 13, 12, 23, 9, 15, 1] ,
[0, 12, 24, 6, 18, 23, 5, 17, 4, 11, 16, 3, 10, 22, 9, 14, 21, 8, 15, 2, 7, 19, 1, 13, 20] ,
[0, 13, 21, 9, 17, 3, 11, 24, 7, 15, 1, 14, 22, 5, 18, 4, 12, 20, 8, 16, 2, 10, 23, 6, 19] ,
[0, 14, 23, 7, 16, 8, 17, 1, 10, 24, 11, 20, 9, 18, 2, 19, 3, 12, 21, 5, 22, 6, 15, 4, 13] ,
[0, 15, 5, 20, 10, 17, 7, 22, 12, 2, 9, 24, 14, 4, 19, 21, 11, 1, 16, 6, 13, 3, 18, 8, 23] ,
[0, 16, 7, 23, 14, 22, 13, 4, 15, 6, 19, 5, 21, 12, 3, 11, 2, 18, 9, 20, 8, 24, 10, 1, 17] ,
[0, 17, 9, 21, 13, 2, 19, 6, 23, 10, 4, 16, 8, 20, 12, 1, 18, 5, 22, 14, 3, 15, 7, 24, 11] ,
[0, 18, 6, 24, 12, 7, 20, 13, 1, 19, 14, 2, 15, 8, 21, 16, 9, 22, 10, 3, 23, 11, 4, 17, 5] ,
[0, 19, 8, 22, 11, 12, 1, 15, 9, 23, 24, 13, 2, 16, 5, 6, 20, 14, 3, 17, 18, 7, 21, 10, 4] ,
[0, 20, 15, 10, 5, 21, 16, 11, 6, 1, 17, 12, 7, 2, 22, 13, 8, 3, 23, 18, 9, 4, 24, 19, 14] ,
[0, 21, 17, 13, 9, 1, 22, 18, 14, 5, 2, 23, 19, 10, 6, 3, 24, 15, 11, 7, 4, 20, 16, 12, 8] ,
[0, 22, 19, 11, 8, 6, 3, 20, 17, 14, 12, 9, 1, 23, 15, 18, 10, 7, 4, 21, 24, 16, 13, 5, 2] ,
[0, 23, 16, 14, 7, 11, 9, 2, 20, 18, 22, 15, 13, 6, 4, 8, 1, 24, 17, 10, 19, 12, 5, 3, 21] ,
[0, 24, 18, 12, 6, 16, 10, 9, 3, 22, 7, 1, 20, 19, 13, 23, 17, 11, 5, 4, 14, 8, 2, 21, 15]]
########
########      Addition Table:
 gentwentyfiveadd=[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24] ,
[1, 2, 3, 4, 0, 6, 7, 8, 9, 5, 11, 12, 13, 14, 10, 16, 17, 18, 19, 15, 21, 22, 23, 24, 20] ,
[2, 3, 4, 0, 1, 7, 8, 9, 5, 6, 12, 13, 14, 10, 11, 17, 18, 19, 15, 16, 22, 23, 24, 20, 21] ,
[3, 4, 0, 1, 2, 8, 9, 5, 6, 7, 13, 14, 10, 11, 12, 18, 19, 15, 16, 17, 23, 24, 20, 21, 22] ,
[4, 0, 1, 2, 3, 9, 5, 6, 7, 8, 14, 10, 11, 12, 13, 19, 15, 16, 17, 18, 24, 20, 21, 22, 23] ,
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0, 1, 2, 3, 4] ,
[6, 7, 8, 9, 5, 11, 12, 13, 14, 10, 16, 17, 18, 19, 15, 21, 22, 23, 24, 20, 1, 2, 3, 4, 0] ,
[7, 8, 9, 5, 6, 12, 13, 14, 10, 11, 17, 18, 19, 15, 16, 22, 23, 24, 20, 21, 2, 3, 4, 0, 1] ,
[8, 9, 5, 6, 7, 13, 14, 10, 11, 12, 18, 19, 15, 16, 17, 23, 24, 20, 21, 22, 3, 4, 0, 1, 2] ,
[9, 5, 6, 7, 8, 14, 10, 11, 12, 13, 19, 15, 16, 17, 18, 24, 20, 21, 22, 23, 4, 0, 1, 2, 3] ,
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9] ,
[11, 12, 13, 14, 10, 16, 17, 18, 19, 15, 21, 22, 23, 24, 20, 1, 2, 3, 4, 0, 6, 7, 8, 9, 5] ,
[12, 13, 14, 10, 11, 17, 18, 19, 15, 16, 22, 23, 24, 20, 21, 2, 3, 4, 0, 1, 7, 8, 9, 5, 6] ,
[13, 14, 10, 11, 12, 18, 19, 15, 16, 17, 23, 24, 20, 21, 22, 3, 4, 0, 1, 2, 8, 9, 5, 6, 7] ,
[14, 10, 11, 12, 13, 19, 15, 16, 17, 18, 24, 20, 21, 22, 23, 4, 0, 1, 2, 3, 9, 5, 6, 7, 8] ,
[15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] ,
[16, 17, 18, 19, 15, 21, 22, 23, 24, 20, 1, 2, 3, 4, 0, 6, 7, 8, 9, 5, 11, 12, 13, 14, 10] ,
[17, 18, 19, 15, 16, 22, 23, 24, 20, 21, 2, 3, 4, 0, 1, 7, 8, 9, 5, 6, 12, 13, 14, 10, 11] ,
[18, 19, 15, 16, 17, 23, 24, 20, 21, 22, 3, 4, 0, 1, 2, 8, 9, 5, 6, 7, 13, 14, 10, 11, 12] ,
[19, 15, 16, 17, 18, 24, 20, 21, 22, 23, 4, 0, 1, 2, 3, 9, 5, 6, 7, 8, 14, 10, 11, 12, 13] ,
[20, 21, 22, 23, 24, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19] ,
[21, 22, 23, 24, 20, 1, 2, 3, 4, 0, 6, 7, 8, 9, 5, 11, 12, 13, 14, 10, 16, 17, 18, 19, 15] ,
[22, 23, 24, 20, 21, 2, 3, 4, 0, 1, 7, 8, 9, 5, 6, 12, 13, 14, 10, 11, 17, 18, 19, 15, 16] ,
[23, 24, 20, 21, 22, 3, 4, 0, 1, 2, 8, 9, 5, 6, 7, 13, 14, 10, 11, 12, 18, 19, 15, 16, 17] ,
[24, 20, 21, 22, 23, 4, 0, 1, 2, 3, 9, 5, 6, 7, 8, 14, 10, 11, 12, 13, 19, 15, 16, 17, 18] ]
########
########      Squre of elements:
 gentwentyfivesquared=[]
 for m in range(NumberofVariantsinPools):
  gentwentyfivesquared.append(gentwentyfive[m][m])
########
 def twentyfiveadd(x,y):
  result=gentwentyfiveadd[x][y]
  return result
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
            x=gentwentyfive[m][j]
            y=gentwentyfive[gentwentyfivesquared[m]][k]
            if p==0:
              gen.append(twentyfiveadd(twentyfiveadd(i,x),y))
            if (countingsize>startsubsetindex and countingsize<=endsubsetindex) or b==1:
              if counting>1:
                print(twentyfiveadd(twentyfiveadd(i,x),y),end="")
                print("/",end="")
              elif counting==1:
                print(twentyfiveadd(twentyfiveadd(i,x),y),end="")
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
              print(j,end="")
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
elif NumberofVariantsinPools==27:
#########################################################################################
#########################################################################################
########     Multiplication Table:
 gentwentyseven=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
                  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26] ,
                  [0, 2, 1, 6, 8, 7, 3, 5, 4, 18, 20, 19, 24, 26, 25, 21, 23, 22, 9, 11, 10, 15, 17, 16, 12, 14, 13] ,
                  [0, 3, 6, 9, 12, 15, 18, 21, 24, 5, 8, 2, 14, 17, 11, 23, 26, 20, 7, 1, 4, 16, 10, 13, 25, 19, 22] ,
                  [0, 4, 8, 12, 16, 11, 24, 19, 23, 14, 15, 10, 26, 18, 22, 2, 3, 7, 25, 20, 21, 1, 5, 6, 13, 17, 9] ,
                  [0, 5, 7, 15, 11, 13, 21, 26, 19, 23, 25, 18, 2, 4, 6, 17, 10, 12, 16, 9, 14, 22, 24, 20, 1, 3, 8] ,
                  [0, 6, 3, 18, 24, 21, 9, 15, 12, 7, 4, 1, 25, 22, 19, 16, 13, 10, 5, 2, 8, 23, 20, 26, 14, 11, 17] ,
                  [0, 7, 5, 21, 19, 26, 15, 13, 11, 16, 14, 9, 1, 8, 3, 22, 20, 24, 23, 18, 25, 17, 12, 10, 2, 6, 4] ,
                  [0, 8, 4, 24, 23, 19, 12, 11, 16, 25, 21, 20, 13, 9, 17, 1, 6, 5, 14, 10, 15, 2, 7, 3, 26, 22, 18] ,
                  [0, 9, 18, 5, 14, 23, 7, 16, 25, 15, 24, 6, 11, 20, 2, 13, 22, 4, 21, 3, 12, 26, 8, 17, 19, 1, 10] ,
                  [0, 10, 20, 8, 15, 25, 4, 14, 21, 24, 7, 17, 23, 3, 13, 19, 2, 9, 12, 22, 5, 11, 18, 1, 16, 26, 6] ,
                  [0, 11, 19, 2, 10, 18, 1, 9, 20, 6, 17, 25, 8, 16, 24, 7, 15, 26, 3, 14, 22, 5, 13, 21, 4, 12, 23] ,
                  [0, 12, 24, 14, 26, 2, 25, 1, 13, 11, 23, 8, 22, 7, 10, 6, 9, 21, 19, 4, 16, 3, 15, 18, 17, 20, 5] ,
                  [0, 13, 26, 17, 18, 4, 22, 8, 9, 20, 3, 16, 7, 11, 21, 12, 25, 2, 10, 23, 6, 24, 1, 14, 5, 15, 19] ,
                  [0, 14, 25, 11, 22, 6, 19, 3, 17, 2, 13, 24, 10, 21, 8, 18, 5, 16, 1, 12, 26, 9, 23, 7, 20, 4, 15] ,
                  [0, 15, 21, 23, 2, 17, 16, 22, 1, 13, 19, 7, 6, 12, 18, 20, 8, 14, 26, 5, 11, 10, 25, 4, 3, 9, 24] ,
                  [0, 16, 23, 26, 3, 10, 13, 20, 6, 22, 2, 15, 9, 25, 5, 8, 12, 19, 17, 21, 1, 4, 11, 24, 18, 7, 14] ,
                  [0, 17, 22, 20, 7, 12, 10, 24, 5, 4, 9, 26, 21, 2, 16, 14, 19, 6, 8, 13, 18, 25, 3, 11, 15, 23, 1] ,
                  [0, 18, 9, 7, 25, 16, 5, 23, 14, 21, 12, 3, 19, 10, 1, 26, 17, 8, 15, 6, 24, 13, 4, 22, 11, 2, 20] ,
                  [0, 19, 11, 1, 20, 9, 2, 18, 10, 3, 22, 14, 4, 23, 12, 5, 21, 13, 6, 25, 17, 7, 26, 15, 8, 24, 16] ,
                  [0, 20, 10, 4, 21, 14, 8, 25, 15, 12, 5, 22, 16, 6, 26, 11, 1, 18, 24, 17, 7, 19, 9, 2, 23, 13, 3] ,
                  [0, 21, 15, 16, 1, 22, 23, 17, 2, 26, 11, 5, 3, 24, 9, 10, 4, 25, 13, 7, 19, 20, 14, 8, 6, 18, 12] ,
                  [0, 22, 17, 10, 5, 24, 20, 12, 7, 8, 18, 13, 15, 1, 23, 25, 11, 3, 4, 26, 9, 14, 6, 19, 21, 16, 2] ,
                  [0, 23, 16, 13, 6, 20, 26, 10, 3, 17, 1, 21, 18, 14, 7, 4, 24, 11, 22, 15, 2, 8, 19, 12, 9, 5, 25] ,
                  [0, 24, 12, 25, 13, 1, 14, 2, 26, 19, 16, 4, 17, 5, 20, 3, 18, 15, 11, 8, 23, 6, 21, 9, 22, 10, 7] ,
                  [0, 25, 14, 19, 17, 3, 11, 6, 22, 1, 26, 12, 20, 15, 4, 9, 7, 23, 2, 24, 13, 18, 16, 5, 10, 8, 21] ,
                  [0, 26, 13, 22, 9, 8, 17, 4, 18, 10, 6, 23, 5, 19, 15, 24, 14, 1, 20, 16, 3, 12, 2, 25, 7, 21, 11]]
########
########      Addition Table:
 gentwentysevenadd=[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26] ,
                    [1, 2, 0, 4, 5, 3, 7, 8, 6, 10, 11, 9, 13, 14, 12, 16, 17, 15, 19, 20, 18, 22, 23, 21, 25, 26, 24] ,
                    [2, 0, 1, 5, 3, 4, 8, 6, 7, 11, 9, 10, 14, 12, 13, 17, 15, 16, 20, 18, 19, 23, 21, 22, 26, 24, 25] ,
                    [3, 4, 5, 6, 7, 8, 0, 1, 2, 12, 13, 14, 15, 16, 17, 9, 10, 11, 21, 22, 23, 24, 25, 26, 18, 19, 20] ,
                    [4, 5, 3, 7, 8, 6, 1, 2, 0, 13, 14, 12, 16, 17, 15, 10, 11, 9, 22, 23, 21, 25, 26, 24, 19, 20, 18] ,
                    [5, 3, 4, 8, 6, 7, 2, 0, 1, 14, 12, 13, 17, 15, 16, 11, 9, 10, 23, 21, 22, 26, 24, 25, 20, 18, 19] ,
                    [6, 7, 8, 0, 1, 2, 3, 4, 5, 15, 16, 17, 9, 10, 11, 12, 13, 14, 24, 25, 26, 18, 19, 20, 21, 22, 23] ,
                    [7, 8, 6, 1, 2, 0, 4, 5, 3, 16, 17, 15, 10, 11, 9, 13, 14, 12, 25, 26, 24, 19, 20, 18, 22, 23, 21] ,
                    [8, 6, 7, 2, 0, 1, 5, 3, 4, 17, 15, 16, 11, 9, 10, 14, 12, 13, 26, 24, 25, 20, 18, 19, 23, 21, 22] ,
                    [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 0, 1, 2, 3, 4, 5, 6, 7, 8] ,
                    [10, 11, 9, 13, 14, 12, 16, 17, 15, 19, 20, 18, 22, 23, 21, 25, 26, 24, 1, 2, 0, 4, 5, 3, 7, 8, 6] ,
                    [11, 9, 10, 14, 12, 13, 17, 15, 16, 20, 18, 19, 23, 21, 22, 26, 24, 25, 2, 0, 1, 5, 3, 4, 8, 6, 7] ,
                    [12, 13, 14, 15, 16, 17, 9, 10, 11, 21, 22, 23, 24, 25, 26, 18, 19, 20, 3, 4, 5, 6, 7, 8, 0, 1, 2] ,
                    [13, 14, 12, 16, 17, 15, 10, 11, 9, 22, 23, 21, 25, 26, 24, 19, 20, 18, 4, 5, 3, 7, 8, 6, 1, 2, 0] ,
                    [14, 12, 13, 17, 15, 16, 11, 9, 10, 23, 21, 22, 26, 24, 25, 20, 18, 19, 5, 3, 4, 8, 6, 7, 2, 0, 1] ,
                    [15, 16, 17, 9, 10, 11, 12, 13, 14, 24, 25, 26, 18, 19, 20, 21, 22, 23, 6, 7, 8, 0, 1, 2, 3, 4, 5] ,
                    [16, 17, 15, 10, 11, 9, 13, 14, 12, 25, 26, 24, 19, 20, 18, 22, 23, 21, 7, 8, 6, 1, 2, 0, 4, 5, 3] ,
                    [17, 15, 16, 11, 9, 10, 14, 12, 13, 26, 24, 25, 20, 18, 19, 23, 21, 22, 8, 6, 7, 2, 0, 1, 5, 3, 4] ,
                    [18, 19, 20, 21, 22, 23, 24, 25, 26, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17] ,
                    [19, 20, 18, 22, 23, 21, 25, 26, 24, 1, 2, 0, 4, 5, 3, 7, 8, 6, 10, 11, 9, 13, 14, 12, 16, 17, 15] ,
                    [20, 18, 19, 23, 21, 22, 26, 24, 25, 2, 0, 1, 5, 3, 4, 8, 6, 7, 11, 9, 10, 14, 12, 13, 17, 15, 16] ,
                    [21, 22, 23, 24, 25, 26, 18, 19, 20, 3, 4, 5, 6, 7, 8, 0, 1, 2, 12, 13, 14, 15, 16, 17, 9, 10, 11] ,
                    [22, 23, 21, 25, 26, 24, 19, 20, 18, 4, 5, 3, 7, 8, 6, 1, 2, 0, 13, 14, 12, 16, 17, 15, 10, 11, 9] ,
                    [23, 21, 22, 26, 24, 25, 20, 18, 19, 5, 3, 4, 8, 6, 7, 2, 0, 1, 14, 12, 13, 17, 15, 16, 11, 9, 10] ,
                    [24, 25, 26, 18, 19, 20, 21, 22, 23, 6, 7, 8, 0, 1, 2, 3, 4, 5, 15, 16, 17, 9, 10, 11, 12, 13, 14] ,
                    [25, 26, 24, 19, 20, 18, 22, 23, 21, 7, 8, 6, 1, 2, 0, 4, 5, 3, 16, 17, 15, 10, 11, 9, 13, 14, 12] ,
                    [26, 24, 25, 20, 18, 19, 23, 21, 22, 8, 6, 7, 2, 0, 1, 5, 3, 4, 17, 15, 16, 11, 9, 10, 14, 12, 13] ]
########
########      Squre of elements:
 gentwentysevensquared=[]
 for m in range(NumberofVariantsinPools):
  gentwentysevensquared.append(gentwentyseven[m][m])
########
 def twentysevenadd(x,y):
  result=gentwentysevenadd[x][y]
  return result
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
            x=gentwentyseven[m][j]
            y=gentwentyseven[gentwentysevensquared[m]][k]
            if p==0:
              gen.append(twentysevenadd(twentysevenadd(i,x),y))
            if (countingsize>startsubsetindex and countingsize<=endsubsetindex) or b==1:
              if counting>1:
                print(twentysevenadd(twentysevenadd(i,x),y),end="")
                print("/",end="")
              elif counting==1:
                print(twentysevenadd(twentysevenadd(i,x),y),end="")
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
              print(j,end="")
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
