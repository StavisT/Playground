from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

query="big data banking firm company telekom telecom"
querywords=word_tokenize(query) #list of words in query

filtered_sentence = [w for w in words if not w in stop_words]
