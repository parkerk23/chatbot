import os
import openai
openai.organization = "YOUR_ORG_ID"
openai.api_key = os.getenv("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")
openai.Model.list()
question = input("What seesm to be the issue") 
openai.Completion.create(
  model="text-davinci-003",
  prompt=question,
  max_tokens=7,
  temperature=0
)
