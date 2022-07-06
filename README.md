# Creating-large-volume-of-assessemnts-from-question-pools<br>
<strong>Main25 file:</strong><br>
The Main25 file calls the question pools in <strong>Questions25</strong> 25 times.<br>
The result is a pdf of 25 exams and a list that indicates questions used in each exam.<br> 
Each pair of exams in the resulting odf have one question in common.<br>
The exams come from 6 pools of 5 questions. Each pool is focussed on one learning goal.<br>
<strong>Generator for Pools of 4,5,7,8,9,11,13,17 Questions File:</strong><br>
Let M be the number of learning goals and k be the size of the question pools.<br>
For M many learning goals, create M many folders names LearningGoalx where x=1,2,...,M.<br>
In each folder LearningGoalx, create LaTex files name LGxQn for each question, where n=1,2,...,k.
