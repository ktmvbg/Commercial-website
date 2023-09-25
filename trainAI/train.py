import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.FineTuningJob.create(training_file="file-DJXgg2nnoFwlD8RfICOABuHr", model="gpt-3.5-turbo")
print(response)
