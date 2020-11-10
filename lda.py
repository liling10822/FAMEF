import os
import pandas as pd
import re
import nltk
from string import punctuation
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import gensim
from gensim.utils import simple_preprocess
import pyLDAvis.gensim
import warnings
import pyLDAvis
import sys
from gensim import corpora,models
from nltk.corpus import stopwords
import json

stop_words = stopwords.words('english')


stop_words_new =['code','file','text','use','http','https','install','using','import','python','instal','example','documentation','rain'
                'contains','contain','data','chinese','korean','thai','japanese']
stop_words.extend(stop_words_new)



def functionality(repo):
    get_details(repo)


def preprocess(text):
    result = []
    for token in simple_preprocess(text):
        if token not in stop_words and len(token) > 3:


            result.append(token)

    return result

def get_details(repo):

    with open (repo,'r') as f:
        repo = json.load(f)

    excerpts = repo['description']

    input_excerpt = ""
    for excerpt in excerpts:
        input_excerpt += excerpt['excerpt']
    lda_model = gensim.models.ldamodel.LdaModel.load('./models/lda.model')
    dictionary = (lda_model.id2word)
    # bow_corpus = [dictionary.doc2bow(r) for r in repo]
    # tfidf = models.TfidfModel(bow_corpus)
    # corpus_tfidf = tfidf[bow_corpus]
    res = []
    bow_vector = dictionary.doc2bow(preprocess(input_excerpt))
    for index, score in sorted(lda_model[bow_vector][0], key=lambda tup: -1 * tup[1]):
        res.append((index, score))
    topics = lda_model.print_topics(-1,50)
    # LDAvis_prepared = pyLDAvis.gensim.prepare(lda_model, corpus_tfidf, dictionary,sort_topics=False)
    # pyLDAvis.save_html(p, 'lda.html')




    with open(sys.argv[2],'w') as f:
        for a,b in res:
           f.write('topic{}\t: probabiity = {}'.format(a,b))
           f.write('\n')
        f.write('\n')
        for t in topics:
            f.write('Topic No ={}\t words{}'.format((t[0]),t[1]))
            f.write('\n\n')

repo_details = sys.argv[1]
output_file = sys.argv[2]

functionality(repo_details)




