import PyPDF2
import nltk
import string
import operator
import sys
import os
import glob

from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')

# Read stopwords
with open('stopwords.txt') as f:
    stopwords = f.readlines()

stopwords = [x.strip() for x in stopwords]

# Initialize stemmer
stemmer = nltk.stem.snowball.GermanStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)


def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]


def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words=stopwords)


def cosine_sim(text1, text2):
    try:
        tfidf = vectorizer.fit_transform([text1, text2])
        return ((tfidf * tfidf.T).A)[0, 1]
    except Exception:
        return 0.0


def processPDF(f, fout):
    pdf = PyPDF2.PdfFileReader(f, strict=False)
    fname = os.path.basename(f)

    pages = [[0]]

    for x in range(0, pdf.getNumPages() - 1):

        page1 = ""
        page1 += pdf.getPage(x).extractText() + "\n"

        page2 = ""
        page2 += pdf.getPage(x + 1).extractText() + "\n"

        if cosine_sim(page1, page2) < 0.1:
            pages.append([x + 1])
        else:
            pages[len(pages) - 1].append(x + 1)

    for cluster in pages:
        output = PyPDF2.PdfFileWriter()
        content = ''
        filename = ''

        for single_page in cluster:
            output.addPage(pdf.getPage(single_page))
            content += pdf.getPage(single_page).extractText() + "\n"
            filename += str(single_page) + '-'

        outputStream = open(fout + '/' + fname + "-" +
                            filename + ".pdf", "wb")

        output.write(outputStream)
        outputStream.close()
