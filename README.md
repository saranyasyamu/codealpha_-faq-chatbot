# 🤖 Hybrid Chatbot

## Description
Hybrid Chatbot is an AI-powered chatbot that combines a large FAQ dataset with AI-generated responses. It first searches the FAQ dataset for an exact or similar answer. If no suitable answer is found, it uses AI to generate a relevant response. The chatbot provides fast, accurate, and user-friendly assistance through a simple Streamlit web interface.

## Features
- Answers questions from a large FAQ dataset
- AI-generated responses for unknown questions
- Fast and user-friendly interface
- Built using Python and Streamlit
- Easy to deploy and use

## Technologies Used
- Python
- Streamlit
- Pandas
- NLP
- AI Model (Gemini/OpenAI, if used)

## How to Run
1. Clone the repository.
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Project Structure
```
hybrid-chatbot/
│── app.py
│── faq_dataset.csv
│── requirements.txt
│── README.md
```

## Author
Saranya
