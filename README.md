# Fake News Detection

This project aims to develop a machine learning model for detecting fake news using natural language processing (NLP) techniques. The model is trained on a labeled dataset of news articles categorized as either true or false, providing a reliable tool for identifying misinformation.

## Project Overview
- **Goal:** Build a machine learning model capable of classifying news articles as true or false.
- **Approach:** Utilized supervised learning techniques with text-based data.
- **Dataset:** Labeled dataset containing articles marked as true or false.
- **Technologies Used:** Python, Scikit-Learn, Pandas, NumPy, NLTK, Matplotlib

## Features
- **Data Preprocessing:**
  - Text cleaning (removal of stopwords, punctuation, and non-alphanumeric characters)
  - Tokenization and vectorization using TF-IDF
- **Model Training:**
  - Tested multiple classifiers including Logistic Regression, Random Forest, and Support Vector Machines (SVM)
- **Evaluation:**
  - Metrics: Accuracy, Precision, Recall, F1-score
  - Cross-validation for performance stability

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Nidhal-Jegham/fake-news-detector.git
   ```
2. Navigate to the project directory:
   ```bash
   cd fake-news-detector
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```


## Results
- Achieved **96% accuracy** on the test set.
- Demonstrated effective performance in identifying fake news with minimal false positives.

## Future Improvements
- Experiment with deep learning techniques like LSTM and BERT.
- Expand the dataset for better generalization.


