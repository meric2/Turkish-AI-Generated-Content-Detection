import openai
import json

openai.api_key = 'your_openai_api_key'

prompts = [
    "Write a short story about a futuristic city.",
    "Explain the concept of machine learning.",
    # Add more prompts as needed
]

ai_generated_texts = []

for prompt in prompts:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    ai_generated_texts.append({
        "prompt": prompt,
        "response": response.choices[0].text.strip()
    })

# Save the data to a JSON file
with open('ai_generated_texts.json', 'w') as f:
    json.dump(ai_generated_texts, f, indent=4)
