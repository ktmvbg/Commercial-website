import openai
import json

FINE_TUNED_MODEL = "davinci:ft-personal-2023-09-17-05-19-34"
CONTEXT_FINE_TUNED_MODEL = "davinci:ft-personal-2023-09-17-03-25-57"
RESPONSE_FINE_TUNED_MODEL = "davinci:ft-personal-2023-09-17-05-19-34"

def test(chat, expected_response):
    get_context_completion = openai.Completion.create(
        model=CONTEXT_FINE_TUNED_MODEL,
        prompt=chat,
        max_tokens=256,
        n=1,
        temperature=0.0,
        stop="\n###"
    )
    prompt = get_context_completion.choices[0].text + "###" + "Customer:" + chat + "\n" + "Agent:"
    response = openai.Completion.create(
        model=RESPONSE_FINE_TUNED_MODEL,
        prompt=prompt,
        max_tokens = 256,
        n = 1,
        temperature = 0.0,
        stop = "\n###"
    )
    response = response.choices[0].text
    print("Chat: " + chat)
    print("Response: " + response)
    print("Expected Response: " + expected_response)
    result = response.strip().strip(" ") == expected_response.strip().strip(" ")
    print(result)
    return result

data = open("test2.jsonl", "r").readlines()
data = [json.loads(line.strip()) for line in data]
success = 0
for i in range(len(data)):
    chat = data[i]["prompt"]
    expected_response = data[i]["completion"]
    if test(chat, expected_response):
        success += 1
print("Success: " + str(success) + "/" + str(len(data)))
