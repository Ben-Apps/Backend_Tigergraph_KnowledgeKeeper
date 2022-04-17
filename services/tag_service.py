import json
import pytextrank
import spacy
from collections import Counter
from services.suggestion_service import get_text_page

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("textrank")


def get_simlarity(text1, text2):
    if text1 == "" or text2 == "":
        return 0
    doc = nlp(text1)
    doc2 = nlp(text2)
    return doc.similarity(doc2)


def get_score(text):
    return nlp(text).vector

def get_top_rank_topics(url):
    text = get_text_page(url)['text']
    doc = nlp(text)
    phrases_count = {}
    phrases_score = {}
    tags = set()

    nouns = [chunk.text for chunk in doc if chunk.pos_ == "NOUN" or chunk.pos_ == "PROPN"]
    # examine the top-ranked phrases in the document
    for phrase in doc._.phrases:
        if phrase.text in nouns:
            phrases_count[phrase.text] = phrase.count
            phrases_score[phrase.text] = phrase.rank

    tags.update(dict(Counter(phrases_count).most_common(10)).keys())
    tags.update(dict(Counter(phrases_score).most_common(10)).keys())
    return json.dumps({"TAGS": list(tags)})
