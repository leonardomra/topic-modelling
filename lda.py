import en_core_sci_md
import scispacy
import spacy
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from tqdm import tqdm
import pandas as pd
import numpy as np
import joblib

class LDA:

    nlp = None

    def __init__(self):
        self.nlp = en_core_sci_md.load(disable=['tagger', 'parser', 'ner'])
        self.nlp.max_length = 2000000
        self.expandStopWords()
        
    def expandStopWords(self):
        # New stop words list
        self.customize_stop_words = [
            'doi', 'preprint', 'copyright', 'peer', 'reviewed', 'org', 'https', 'et', 'al', 'author', 'figure', 
            'rights', 'reserved', 'permission', 'used', 'using', 'biorxiv', 'fig', 'fig.', 'al.',
            'di', 'la', 'il', 'del', 'le', 'della', 'dei', 'delle', 'una', 'da', 'dell', 'non', 'si',
            'preprint', 'copyright', 'peer-reviewed', 'author/funder', 'doi', 'license', 'biorxiv', 'medrxiv', 'international', 'right', 'display',
            'permission', 'cc-by-nc-nd', 'fig.', 'figure', '=', '°', 'show', 'contain', '<',
            '>', '+', 'al.', '␤', 'ct', '␣', 'ifn-', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
        # Mark them as stop words
        for w in self.customize_stop_words:
            self.nlp.vocab[w].is_stop = True

    def produceTopics(self, targetTexts, exists):
        vs = self.vectorize(targetTexts, exists)
        lda_tf = None
        if exists is True:
            lda_tf = joblib.load('./lda.csv')
        else:
            lda_tf = LatentDirichletAllocation(n_components=50, random_state=0, n_jobs=4) # TODO: tune n_components: how many topics make sense?
            lda_tf.fit(vs['tf'])
            joblib.dump(lda_tf, 'lda.csv')
        return {'tf_vectorizer': vs['tf_vectorizer'], 'tf': vs['tf'], 'lda_tf': lda_tf}

    def countWords(self, targetTexts, exists):
        vs = self.vectorize(targetTexts, exists)
        word_count = pd.DataFrame({'word': vs['tf_vectorizer'].get_feature_names(), 'count': np.asarray(vs['tf'].sum(axis=0))[0]})
        word_count = word_count.sort_values('count', ascending=False).set_index('word')[:20].sort_values('count', ascending=True)#.plot(kind='barh')
        return word_count.to_dict()

    def vectorize(self, targetTexts, exists):
        tf_vectorizer = None
        tf = None
        if exists is True:
            tf_vectorizer = joblib.load('./tf_vectorizer.csv')
            tf = joblib.load('./tf.csv')
        else:
            tf_vectorizer = CountVectorizer(tokenizer = self.spacyTokenizer)
            tf = tf_vectorizer.fit_transform(tqdm(targetTexts))
            self.dumpVecs(tf_vectorizer, tf)
        tf.shape
        return {'tf_vectorizer': tf_vectorizer, 'tf': tf}
    

    def dumpVecs(self, tf_vectorizer, tf):
        joblib.dump(tf_vectorizer, 'tf_vectorizer.csv')
        joblib.dump(tf, 'tf.csv')

    def spacyTokenizer(self, sentence):
        return [word.lemma_ for word in self.nlp(sentence) if not (word.like_num or word.is_stop or word.is_punct or word.is_space)] # remove numbers (e.g. from references [1], etc.)

    