
"""
Cleaning the text to create normalized text representations.
"""

import html
import json
import re
from bs4 import BeautifulSoup

import pandas as pd

from deep_translator import GoogleTranslator

from spellchecker import SpellChecker
spell = SpellChecker()

import nltk
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Reading the data from the json files
text_df = pd.read_json('Input/data.json')
german_cities_df = pd.read_json('Assets/germany.json')
german_cities_df['name'] = german_cities_df['name'].apply(lambda x: x.lower())

# Reading abbreviations json file
with open('Assets/abbreviations.json') as json_file:
    abbreviations = json.load(json_file)

# Creating a list of new stop_words to remove domain specific stop words
months_stopwords = ["january", "february", "march", "april", "may", "june", "july", "august", "september",
                    "october", "november", "december", "year", "years"]
other_stopwords = ["junior", "senior", "all genders", "w", "x", "u", "f"]

# Extending custom stopwords to already existing ones
stop = stopwords.words('english')
stop.extend(months_stopwords)
stop.extend(other_stopwords)
stop.extend(german_cities_df['name'])

# drop na values
text_df.dropna(inplace=True)
text_df.reset_index(drop=True, inplace=True)

# Creating new column to store cleaned text
if 'clean_job_title' not in text_df:
    text_df['clean_job_title'] = text_df['job_title']


# converting html tags
def remove_html_tags(row):
    """
    Parameters:
        row:The row from the dataframe which is to be replaced.

    Returns:
        row:The row where html tags gets replaced by actual words .
    """

    text = row['clean_job_title']
    text = html.unescape(text)
    text = BeautifulSoup(text, "lxml").text

    return text


# Replace the abbreviations to their full form
def replace_abbreviations(row):
    """
    Parameters:
        row:The row from the dataframe which is to be replaced.

    Returns:
        row:The row which gets replace the abbreviations to their full form.
    """

    text = row['clean_job_title']
    for key, value in abbreviations[row['category']].items():
        text = text.replace(key, value)
    return text


# Remove the unnecessary punctuations
def remove_punctuations(row):
    """
    Parameters:
        row:The row from the dataframe which is to be replaced.

    Returns:
        row:The row after removing the punctuations.
    """

    text = row['clean_job_title']
    if re.findall(r"[-!?@&*\(\)/:;,|%\'\`\"\_\n]", text):
        text = re.sub(r"[-!?@&*\(\)/:;,|%\'\`\"\_\n]", '', text)

    return text


def main():
    # replace html values
    text_df['clean_job_title'] = text_df.apply(remove_html_tags, axis=1)

    # Remove unnecessary values like (m/w/d) and various combinations
    text_df['clean_job_title'] = text_df.apply(lambda row: re.sub(r'\([a-zA-Z/|]*/[a-zA-Z/|]*\)', '',
                                                                  row['clean_job_title']), axis=1)

    # Translate to english
    text_df['clean_job_title'] = text_df.apply(lambda row: GoogleTranslator(source='de', target='en')
                                               .translate(row['clean_job_title']), axis=1)

    # Replace abbreviations
    text_df['clean_job_title'] = text_df.apply(replace_abbreviations, axis=1)

    # Remove punctuations
    text_df['clean_job_title'] = text_df.apply(remove_punctuations, axis=1)

    # Remove numbers
    text_df['clean_job_title'] = text_df.apply(lambda row: re.sub(r'\d+', '', row['clean_job_title']),
                                               axis=1)

    # Remove extra space
    text_df['clean_job_title'] = text_df['clean_job_title'].apply(lambda x: re.sub(' +', ' ', x))

    # Convert to lower case
    text_df['clean_job_title'] = text_df.apply(lambda row: row['clean_job_title'].lower(), axis=1)

    # Tokenize the sentence
    text_df['clean_job_title'] = text_df.apply(lambda row: word_tokenize(row['clean_job_title']),
                                               axis=1)
    # Remove stop words
    text_df['clean_job_title'] = text_df['clean_job_title'].apply(
        lambda x: [item for item in x if item not in stop])
    
    # Spelling correction
    text_df['clean_job_title'] = text_df['clean_job_title'].apply(lambda row: [spell.correction(word) for word in row])

    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    text_df['clean_job_title'] = text_df['clean_job_title'].apply(
        lambda row: [lemmatizer.lemmatize(w) for w in row])

    print(text_df['clean_job_title'][0:20])
    # Saving the cleaned data in json file
    text_df.to_json("Output/clean_data.json", orient='records')


if __name__ == "__main__":
    main()
