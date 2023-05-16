# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.

#q1 = input(": ")
import json

Q = input("Input Question: ")

questions = []
for i in range(4):
    questions.append(input(f"Answer {i + 1}: "))

answer = str(input("Input Correct Answer: "))

Json = {"Question":Q, "Answers":questions, "Correct": answer}

with open("Question.json", "w") as f:
    f.write(json.dumps(Json))

#filehandle = open("questions.txt", 'w')

#filehandle.write(input("Input Question: "))