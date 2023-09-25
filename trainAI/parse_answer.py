import json

data = open("Questionnaire-legacy.txt", "r").readlines()
data = [line.strip() for line in data]
data = [x for x in data if len(x) > 0]
# data = [x for x in data if x[0] == "Q" or x[0] == "A"]

category = ""
product = ""
questions = []
testing_questions = []
answer = ""
training_data = []
testing_data = []

for line in data:
    if ("Product" in line):
        product = line.split(" : ")[-1].strip()
        continue
    if ("Category" in line):
        category = line.split(" : ")[-1].strip()
        continue
    if line[0] == "Q":
        if ("5: ") in line:
            testing_questions.append(line[6:].strip(" "))
        else:
            questions.append(line[6:].strip(" "))
    else:
        answer = line.find(":") 
        if answer == -1:
            answer = line
        else:
            answer = line[answer+1:].strip(" ")
        for i in range(len(questions)):
            training_data.append({"prompt": "Summary: {}\n\nSpecific information: {}\nCustomer: {}\nAgent:".format(product, category, questions[i]),
                                  "completion": answer + "\n###"})
        for i in range(len(testing_questions)):
            testing_data.append({"prompt": "Summary: {}\n\nSpecific information: {}\nCustomer: {}\nAgent:".format(product, category, testing_questions[i]),
                                  "completion": answer + "\n###"})
        questions = []
        testing_questions = []


with open("training2.jsonl", "w") as f:
    for line in training_data:
        f.write(json.dumps(line,  ensure_ascii=False) + "\n")

with open("testing2.jsonl", "w") as f:
    for line in testing_data:
        f.write(json.dumps(line,  ensure_ascii=False) + "\n")
