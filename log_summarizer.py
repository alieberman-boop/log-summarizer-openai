import os
from openai import OpenAI
client = OpenAI()
log = "Failed SSH login from 45.83.220.11"
resp = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": f"Summarize: {log}"}])
print(resp.choices[0].message.content)
