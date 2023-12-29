from openai import OpenAI
import sys

model = "gpt-3.5-turbo"
client = OpenAI()
code_request = sys.argv[1]
behavior = """
You are an expert python developer.
I am going to create a python script directly from your answer (with no edits at all).
Don't write anything that isn't a working python code, which means no prefix or suffix to your answer
("Here's the code for a program that...", "I apologize for the error. Here's the fixed version")
Do not write any explanations, just show me the code itself.
Also please include unit tests that check the logic of the program using 5
different inputs and expected outputs.
"""

messages = [
    {"role": "system", "content": behavior},
    {"role": "user", "content": code_request}
]

for i in range(2, len(sys.argv), 2):
    messages.append(
        {"role": "assistant", "content": sys.argv[i]}
    )
    messages.append(
        {"role": "user", "content": f"""
Your code gave me the following errors:
{sys.argv[i + 1]}
Please write a fixed version of this code
"""}
)

response = client.chat.completions.create(
    model=model,
    messages=messages
)

python_code = response.choices[0].message.content
with open("created_code.py", "w") as file:
    file.write(python_code)
