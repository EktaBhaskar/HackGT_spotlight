#!/usr/bin/env python
# coding: utf-8
import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
import re
from constants import TEXT_DIR

# def apostrophe_normalisation(data):        
#     for (i, j) in [(r"n\'t", " not"), (r"\'re", " are"), (r"\'s", " is"), (r"\'d", " would"), (r"\'ll", " will"), (r"\'t", " not"), (r"\'ve", " have"), (r"\'m", " am"), (r"\'Cause", "because")]:
#         data = re.sub(i, j, data)
#     return data
 
def read_article(file_name):
    file_x = f'{TEXT_DIR}/{file_name}'
    file = open(file_x, "r")
    filedata = file.readlines()
    # article = convert_text_into_good_sentences(filedata[0])
    sentences = []

    for sentence in filedata[0].split(" "):
        # sentence = apostrophe_normalisation(sentence)
        print(sentence)
        # sentence = sentence.replace('\n','')
        # sentence = sentence.replace('\t','')
        # sentence similarity
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop() 
    
    return sentences

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
 
    all_words = list(set(sent1 + sent2))
 
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
 
    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
 
    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
 
    return 1 - cosine_distance(vector1, vector2)
 
def build_similarity_matrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2: #ignore if both are same sentences
                continue 
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix


def generate_summary(file_name, top_n=5):
    nltk.download("stopwords")
    stop_words = stopwords.words('english')
    summarize_text = []

    # Step 1 - Read text anc split it
    sentences =  read_article(file_name)

    # Step 2 - Generate Similary Martix across sentences
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)

    # Step 3 - Rank sentences in similarity martix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)

    # Step 4 - Sort the rank and pick top sentences
    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    
    # print("Indexes of top ranked_sentence order are ", ranked_sentence)    

    print("test1:", ranked_sentence)
    for i in range(top_n):
      summarize_text.append(" ".join(ranked_sentence[i][1]))
    #   print("test", ranked_sentence[i][0])

    # Step 5 - Offcourse, output the summarize text
    print("Summarize Text: \n", ". ".join(summarize_text))

def convert_text_into_good_sentences(text):
    text = text.replace("if I", ". if I")
    text = text.replace(" I'm", ". I'm")
    text = text.replace(" and", ".")
    text = text.replace("..", ".")

    good_sent = []
    for i in nltk.sent_tokenize(text):
        if len(i) >= 20:
            good_sent.append(i)

    text = " ".join(good_sent)
    return text

generate_summary( "calculus_test.txt", 2)