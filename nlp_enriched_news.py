import json
import pandas as pd
from utils.entity_detection import load_spacy_model, extract_organizations
from utils.topic_classification import classify_article, load_topic_model
from utils.sentiment_analysis import analyze_and_classify_article_sentiment
from utils.scandal_detection import load_embedding_model, detect_scandal

# Define ANSI color codes
COLOR_GREEN = '\033[92m'
COLOR_YELLOW = '\033[93m'
COLOR_CYAN = '\033[96m'
COLOR_MAGENTA = '\033[95m'
COLOR_RESET = '\033[0m'

# def load_articles_from_data(data_dir='data'):
#     """
#     Load articles from JSONL files in the data directory.
#     """
#     articles = []
#     for filename in os.listdir(data_dir):
#         if filename.endswith('.jsonl'):
#             with open(os.path.join(data_dir, filename), 'r') as f:
#                 for line in f:
#                     articles.append(json.loads(line))
#     return articles