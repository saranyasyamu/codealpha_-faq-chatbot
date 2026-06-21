import streamlit as st
import pandas as pd
import nltk
import string
import wikipedia
import urllib.parse

from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download tokenizer
nltk.download("punkt")

# -----------------------------
# Load FAQ Dataset
# -----------------------------
df = pd.read_csv("faq_dataset_2500.csv")

questions = df["Question"].tolist()
answers = df["Answer"].tolist()

# -----------------------------
# Text Preprocessing
# -----------------------------
def preprocess(text):
    text = text.lower()

    tokens = word_tokenize(text)

    tokens = [
        word for word in tokens
        if word not in string.punctuation
    ]

    return " ".join(tokens)

processed_questions = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(processed_questions)

# -----------------------------
# FAQ Search
# -----------------------------
def search_faq(user_question):

    user_processed = preprocess(user_question)

    user_vector = vectorizer.transform([user_processed])

    similarity = cosine_similarity(
        user_vector,
        faq_vectors
    )

    best_match = similarity.argmax()

    score = similarity[0][best_match]

    if score > 0.25:
        return answers[best_match]

    return None

# -----------------------------
# Wikipedia Search
# -----------------------------
def search_wikipedia(question):

    try:

        wikipedia.set_lang("en")

        answer = wikipedia.summary(
            question,
            sentences=2,
            auto_suggest=True
        )

        return answer

    except:

        return None

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(
    page_title="Hybrid FAQ Chatbot",
    page_icon="🤖"
)

st.title("🤖 Hybrid FAQ Chatbot")

st.write("Ask me anything!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Type your question...")

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Step 1 : FAQ
    answer = search_faq(prompt)

    # Step 2 : Wikipedia
    if answer is None:
        answer = search_wikipedia(prompt)

    with st.chat_message("assistant"):

        if answer:

            st.success(answer)

            st.session_state.messages.append(
                {
                    "role":"assistant",
                    "content":answer
                }
            )

        else:

            st.warning("Sorry, I couldn't find an answer.")

            query = urllib.parse.quote(prompt)

            google_url = f"https://www.google.com/search?q={query}"

            st.markdown(
                f"🔍 **Search on Google:** [Click Here]({google_url})"
            )

            st.session_state.messages.append(
                {
                    "role":"assistant",
                    "content":"Sorry, I couldn't find an answer."
                }
            )