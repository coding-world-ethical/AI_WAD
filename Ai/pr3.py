import nltk
import pandas as pd
from nltk.tokenize import (
    sent_tokenize,
    word_tokenize,
    TreebankWordTokenizer,
    WordPunctTokenizer,
    RegexpTokenizer,
    WhitespaceTokenizer
)
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

# PART 1 :- TEXT TOKENIZATION

txt = "Let's see how it's, working. in such a high #temparature# also"

sent_tokens = sent_tokenize(txt)
word_tokens = word_tokenize(txt)

print("Sentence Tokens:")
print(sent_tokens)

print("\nWord Tokens:")
print(word_tokens)

tokenizer_tree = TreebankWordTokenizer()
tree_tokens = tokenizer_tree.tokenize(txt)

print("\nTreebank Tokens:")
print(tree_tokens)

tokenizer_punct = WordPunctTokenizer()
punct_tokens = tokenizer_punct.tokenize(txt)

print("\nWordPunct Tokens:")
print(punct_tokens)

tokenizer_re = RegexpTokenizer(r"[\w']+")
re_tokens = tokenizer_re.tokenize(txt)

print("\nRegexp Tokens:")
print(re_tokens)

tokenizer_white = WhitespaceTokenizer()
white_tokens = tokenizer_white.tokenize(txt)

print("\nWhitespace Tokens:")
print(white_tokens)

# PART 2 :- STOP WORDS AND POS TAGGING

stop_words = stopwords.words('english')
newStopWords = ['there', 'therefore']
stop_words.extend(newStopWords)

txt_news = """Ukraine's defence ministry says Russian forces are attempting to storm Mariupol's Azovstal steelworks. President Vladimir Putin tells a World War II Victory Day parade in Moscow's Red Square that Russian troops in eastern Ukraine are fighting for "the motherland" as the Kremlin presses on with its offensive in the Donbas. Putin also says Moscow's invasion was a preemptive move to ward off aggression from the West. President Volodymyr Zelenskyy calls for moves to open Ukrainian ports blockaded by Russia to allow for exports and prevent a global food crisis."""

wrd_lst = WhitespaceTokenizer().tokenize(txt_news)
filtered_wrd_list = []

for wrd in wrd_lst:
    if wrd.lower() not in stop_words:
        filtered_wrd_list.append(wrd)

print("\nFiltered Word List:")
print(filtered_wrd_list)

pos_dict = nltk.pos_tag(filtered_wrd_list)

print("\nPOS Tagging:")
print(pos_dict)

# PART 3 :- TF-IDF VECTORIZER

d0 = """The simplest example is provided by deterministic nodes."""
d1 = """The relationship can also be numerical: for example, if the parent node changes."""
d2 = """In fact, this is a worst-case scenario in which the relationship becomes complex."""

string_data = [d0, d1, d2]

tfidf = TfidfVectorizer(ngram_range=(1, 1))
result = tfidf.fit_transform(string_data)

feature_names = tfidf.get_feature_names_out()

df2 = pd.DataFrame(
    result.toarray().transpose(),
    index=feature_names
)

print("\nTF-IDF DataFrame:")
print(df2)

dff = df2.to_dict()
tfidf_val = dff[0]

print("\nHigh TF-IDF words in first document:")
for k, v in tfidf_val.items():
    if v > 0.1:
        print(k)