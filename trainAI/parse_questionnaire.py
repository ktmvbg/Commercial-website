import json

data = open("Questionnaire-legacy.txt", "r").readlines()
data = [line.strip() for line in data]
data = [x for x in data if len(x) > 0]
# data = [x for x in data if x[0] == "Q" or x[0] == "A"]

category = ""
product = ""
questions = []
testing_questions = []
answers = ""
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
        if("5: ") in line:
            testing_questions.append(line[6:].strip(" "))
        else:
            questions.append(line[6:].strip(" "))
    else:
        answers = line[3:]
        for i in range(len(questions)):
            training_data.append({"prompt": questions[i], "completion": " \nSummary: {}\n\nSpecific information: {}\n###".format(
                product, category)})
        for i in range(len(testing_questions)):
            testing_data.append({"prompt": testing_questions[i], "completion": " \nSummary: {}\n\nSpecific information: {}\n###".format(
                product, category)})
        questions = []
        testing_questions = []
        

with open("train1.jsonl", "w") as f:
    for line in training_data:
        f.write(json.dumps(line,  ensure_ascii=False) + "\n")

with open("test1.jsonl", "w") as f:
    for line in testing_data:
        f.write(json.dumps(line,  ensure_ascii=False) + "\n")
