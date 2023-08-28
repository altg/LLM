import pickle
from Questions import *

#obj = Questions()

with open("objects.pkl", 'rb') as file:
    obj = pickle.load(file)

# for i in obj.Questions:
#     print(i.question)
#     for k , v in enumerate(i.MultipleChoices):
#         print(k+1 , ":" , v.choice_ans , end=" | ")
#     print("-")
#     ans = input("Answer 1-4:")
#     if int(ans) == int(i.correct_ans) + 1:
#         print(ans , "Correct !!!\n")
#     else:
#         print("Wrong ! Correct Answer: " , int(i.correct_ans) + 1 , ":" , i.MultipleChoices[int(i.correct_ans)].choice_ans , '\n')

Q1 = obj.Questions[0]

print(len(obj.Questions))