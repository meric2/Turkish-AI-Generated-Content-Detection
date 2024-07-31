# Turkish-AI-Generated-Content-Detection

This project focuses on detecting AI-generated user complaints in Turkish. It utilizes a dataset of human-written complaints and AI-generated complaints created using GPT-3.5 and GPT-4 calls. Three groups of models are trained for this purpose: baseline models, advanced NLP models, and NLP models with Adversarial Training. The goal is to compare the performance of these models against traditional Machine Learning models on this dataset and to assess whether Adversarial Training enhances the results of the NLP models.  

## Project Overview

The key aspects of this project include:

- Data scraping by sending API calls  
- Preprocessing data by common methods for NLP  
- Visualizations for intuitive analysis of the dataset  
- Baseline model training: SVM, Naive Bayes, Logistic Regression  
- NLP model training: BERT, RoBERTa, GPT-2, XLNet, Electra, DistilBERT
- Adversarial model training   
- Comparing model performances to see which method or model is the best    

## Tech Stack

**Language**: Python  
**Technologies**: Pandas, Matplotlib, Seaborn, Numpy, Transformers, NLTK   
**Environment**: Jupyter Notebook  

## Getting Started  

### Prerequisites
- Python 3
- Jupyter Notebook

### Installation

- Clone the repository
  ```bash
  git clone https://github.com/meric2/Turkish-AI-Generated-Content-Detection.git
  ```

- Start Jupyter notebook
  ```bash
  jupyter notebook
  ```

- Install dependencies
  ```bash
  pip install -r requirements.txt
  ```

- Download human dataset from [here](https://huggingface.co/datasets/kmkarakaya/turkishReviews-ds)  
- AI-data that is scraped is in `ai_data.csv`, if you want to scrape again, please refer to `data_scraping.py`  
- The merged data of human and ai datasets are in `reviews.csv`  

- Use `baseline_models.ipynb` for baseline model training  
- Use `TuringBench.ipynb` for NLP model training  
- Use `AdversarialTraining.ipynb` for NLP model adversarial training  
- Use `test/Test.ipynb` to single-shot test the models with the trained models.  


## Contributors

- [Halil Erkan](https://github.com/halilerkan-cs)
- [Zeynep Meriç Aşık](https://github.com/meric2)