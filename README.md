# Creating-large-volume-of-assessemnts-from-question-pools
## Main25 LaTex File:
The Main25 file calls the question pools in <strong>Questions25</strong> 25 times.<br>
The result is a pdf of $25$ exams and a list that indicates questions used in each exam.<br> 
Each pair of exams in the resulting odf have one question in common.<br>
The exams come from 6 pools of 5 questions. Each pool is focussed on one learning goal.<br>
*******************************************************************************************************************************************************************
## Generator for Pools of $4,5,7,8,9,11,13,17$ Questions LaTex File:
Let M be the number of learning goals and k be the size of the question pools.<br>
For M many learning goals, create $M$ many folders names LearningGoalx where $x=1,2,...,M.$ <br>
In each folder LearningGoalx, create LaTex files name LGxQn for each question, where $n=1,2,...,k.$<br>
*******************************************************************************************************************************************************************
## Finding Arrays for 1 or 2 Questions in Common Python File:
If checking $=False$, for $n=4,5,7,8,9,11,13,17$ create arrays for each assessment variants that has $c=1,2$ questions in common.<br>
If checking $=True$, for $n=4,5,7,8,9,11,13,17$ create arrays for each assessment variants and verifies that there are at most $c=1,2$ many questions in common.<br>
*******************************************************************************************************************************************************************
## Finding Arrays for $3$ Questions in Common Python File:
This has the same property as the one for for 1 or 2 questions in common.<br>
<strong>All Arrays for Pools cq equals to 1 or 2 Excel File:</strong><br>
A worksheet containing sheets of results of the Python code for $cq=1$ and $cq=2$
*******************************************************************************************************************************************************************
This project is related to [this paper](https://drive.google.com/file/d/145Zz3A-hlF_oXfGSZowlXzbd6XrR4keh/view). 
