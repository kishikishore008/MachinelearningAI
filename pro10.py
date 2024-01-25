import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import pos_tag, RegexpParser, ne_chunk
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


# Sample Text
text = "change is a contant thing "

# Tokenizing
nltk.download('punkt')
tokens = word_tokenize(text)

# Filtering Stop Words
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

# Part of Speech Tagging
pos_tags = pos_tag(tokens)

# Chunking
grammar = r"""
  NP: {<DT>?<JJ>*<NN>} # Chunk Noun Phrases
  VP: {<VB.*><DT>?<JJ>*<NN|RB|VB.*>*<RB>?} # Chunk Verb Phrases
"""
chunk_parser = RegexpParser(grammar)
chunked = chunk_parser.parse(pos_tags)

# Named Entity Recognition (NER)
ner_tags = ne_chunk(pos_tags)

# Displaying Results
print("Original Text:", text)
print("\nTokenization:")
print(tokens)
print("\nFiltered Stop Words:")
print(filtered_tokens)
print("\nStemmed Tokens:")
print(stemmed_tokens)
print("\nPart of Speech Tagging:")
print(pos_tags)
print("\nChunking:")
print(chunked)
print("\nNamed Entity Recognition:")
print(ner_tags)
