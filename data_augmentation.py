import nltk
import pandas as pd
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Turkish stopwords
stop_words = set(stopwords.words('turkish'))

def synonym_replacement(text, n):
    words = word_tokenize(text)
    new_words = words.copy()
    random_word_list = list(set([word for word in words if word not in stop_words]))
    random.shuffle(random_word_list)
    num_replaced = 0
    for random_word in random_word_list:
        synonyms = get_synonyms(random_word)
        if len(synonyms) >= 1:
            synonym = random.choice(synonyms)
            new_words = [synonym if word == random_word else word for word in new_words]
            num_replaced += 1
        if num_replaced >= n:
            break

    sentence = ' '.join(new_words)
    return sentence

def get_synonyms(word):
    # This is a placeholder function. You would need to implement a way to get synonyms in Turkish.
    return [word]  # Return a list of synonyms

def random_insertion(text, n):
    words = word_tokenize(text)
    for _ in range(n):
        new_word = get_synonyms(random.choice(words))[0]
        insert_pos = random.randint(0, len(words))
        words.insert(insert_pos, new_word)
    sentence = ' '.join(words)
    return sentence

def random_swap(text, n):
    words = word_tokenize(text)
    length = len(words)
    for _ in range(n):
        idx1, idx2 = random.sample(range(length), 2)
        words[idx1], words[idx2] = words[idx2], words[idx1]
    sentence = ' '.join(words)
    return sentence

def random_deletion(text, p):
    words = word_tokenize(text)
    if len(words) == 1:
        return text
    remaining = list(filter(lambda x: random.random() > p, words))
    if len(remaining) == 0:
        return random.choice(words)  # prevent returning empty
    sentence = ' '.join(remaining)
    return sentence

# Load your data from an Excel file
df = pd.read_excel('aidataset.xlsx')

# Augment data
augmented_texts = []
for index, row in df.iterrows():
    text = row['output']
    # Apply multiple transformations
    for _ in range(5):  # Repeat each transformation 5 times
        augmented_texts.append(synonym_replacement(text, n=2))
        augmented_texts.append(random_insertion(text, n=3))
        augmented_texts.append(random_swap(text, n=2))
        augmented_texts.append(random_deletion(text, p=0.1))

augmented_df = pd.DataFrame(augmented_texts, columns=['output'])
augmented_df.to_csv('augmented_data.csv', index=False, encoding='utf-8-sig')

print("Augmentation done. Check the 'augmented_data.csv' file.")
