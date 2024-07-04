from datasets import load_dataset
import pandas as pd
import re
from openai import OpenAI
import os

# Set up your OpenAI API key (ensure this is kept secure)
client = OpenAI(
    api_key=""
)

# Load data
df = load_dataset('kmkarakaya/turkishReviews-ds')
df = df['train'].to_pandas().head(1000)

# Function to extract the first sentence from a text
def extract_first_sentence(text):
    # Splitting on period followed by space to capture end of sentence
    sentences = re.split(r'\.\s+', text)
    if sentences:
        return sentences[0]
    return ""

# Append a definition to the sentence
def append_definition(sentence, definition):
    return f"{sentence}. {definition}"

# Function to make OpenAI API call
def get_openai_response(prompt):
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a customer complaining."},
                {"role": "user", "content": prompt}
            ],
            model="gpt-3.5-turbo",
            max_tokens=150,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print("Error with OpenAI API:", e)
        return None


# Add a new column with the first sentence and the definition
definition = " Sen bir tüketicisin. Bu konuda günlük dilde 80-120 kelimelik bir şikayet metini yaz. Talep ediyorum, Aksi takdirde, arz ederim gibi kalıplar kullanma, resmi dil kullanma. Örnek Girdi: A101 Reklamınızı Yaptığınız Ürününü Bulamamak. Örnek Çıktı: A101 Reklamınızı Yaptığınız Ürününü Bulamamak. 21.05.2020 tarihinde satışa sunduğunuz filtre kahve makinenizi Ankara'da esat semtinde 8.40'de reşit galip şubesi. 8.50'de esat caddesindeki daha sonra yine 9.02'de esat caddesindeki öbür şubenize sordum ikisi gelmediğini diğeri de 1 tane geldiğini onunda satıldığını söylediler. Nasıl oluyor reklamın"

ai_data = pd.DataFrame({
    'prompt': df['review'].apply(lambda x: append_definition(extract_first_sentence(x), definition))
})

# Apply the function to generate responses and store them in a new column
ai_data['review'] = ai_data['prompt'].apply(get_openai_response)

# Optional: Save the dataframe with prompts if necessary
ai_data.to_csv('ai_data.csv', index=False, encoding='utf-8-sig')
