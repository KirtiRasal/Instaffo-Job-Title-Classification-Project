#!/usr/bin/env python
# coding: utf-8

"""
Clean your text to create normalized text represenations.
"""

import re
import html
import json

import pandas as pd

from deep_translator import GoogleTranslator

import nltk
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Reading the data from json files

text_df = pd.read_json('data.json')
german_cities_df = pd.read_json('germany.json')

# Reading abbreviations json file
with open('abbreviations.json') as json_file:
    data = json.load(json_file)

# Check the data
text_df.head()

# drop na values

text_df.dropna(inplace=True)
text_df.reset_index(drop=True, inplace=True)

print(text_df.head())

# Creating new column to store cleaned text 
if 'clean_job_title' not in text_df:
    text_df['clean_job_title'] = text_df['job_title']

text_df.head()


# converting html tags

def remove_html_tags(row):
    """
    Returns the String after replacing html tags.

    Parameters:
        row:The row which is to be replaced.

    Returns:
        replace(row):The row where html tags gets replaced by actual words .
    """

    text = row['clean_job_title']
    if text != html.unescape(text):
        text = html.unescape(text)

    return text


# Removing unnecessary values like (m/w/d) and various combinations

def remove_unnecessary_values(row):
    """
    Returns the abbreviated String.

    Parameters:
        row:The row which is to be replaced.

    Returns:
        replace(row):The row which gets replaced by abbreviations.
    """

    return re.sub(r'\([a-zA-Z/|]*/[a-zA-Z/|]*\)', '', row['clean_job_title'])


# Translation from german to english

def translate_language(row):
    """
    Returns the String which is translated to english.

    Parameters:
        row:A a single row of a dataframe which is to be replaced.

    Returns:
        replace(row):The row which gets translated to english.
    """

    return GoogleTranslator(source='de', target='en').translate(row['clean_job_title'])


# Saving the translated data in csv file

text_df.to_csv("clean_text_data.csv", index=False)

translated_text = pd.read_csv('../Downloads/clean_text_data.csv')


# Convert the abbreviations to their full form
def replace_strings(row):
    """
    Returns the abbreviated String.

    Parameters:
        row:The row which is to be replaced.

    Returns:
        replace(row):The row which gets replaced by abbreviations.
    """

    text = row['clean_job_title']
    for key, value in data[row['category']].items():
        text = text.replace(key, value)
    return text


# translated_text['clean_job_title'].str.contains('Business').any()


# Remove the unnecessary punctuations

def remove_punctuations(row):
    """
    Replace punctuations from ``text`` with whitespaces.

    Parameters:
        row:The row which is to be replaced.

    Returns:
        replace(row):The row which gets replaced by abbreviations.
    """

    text = row['clean_job_title']
    if re.findall(r"[-!?@&*\(\)/:;,\'\`\"\_\n]", text):
        text = re.sub(r"[-!?@&*\(\)/:;,\'\`\"\_\n]", '', text)

    return text


# Remove numbers

def remove_numbers(row):
    """
    Returns the String after removing the numbers.

    Parameters:
        row:The row of the dataframe for removing the numbers.

    Returns:
        replace(row):The row which gets String after removing the numbers.
    """

    return re.sub(r'\d+', '', row['clean_job_title'])


# Convert to lower case

def convert_to_lowercase(row):
    """
    Returns the lowercase String.

    Parameters:
        row:The row which is to be converted to lowercase.

    Returns:
        replace(row):The row which gets converted to lowercase.
    """

    return row['clean_job_title'].lower()


# Word tokenize

def tokenizing_words(row):
    """
    Returns the tokens.

    Parameters:
        row:The row which is to be tokenized.

    Returns:
        replace(row):The row which gets tokens from the sentences.
    """

    return row['clean_job_title'].apply(word_tokenize)


# Removing stop words

def stop_words(row):
    """
    Returns the tokens which does not have stop words.

    Parameters:
        row:The row which is to be used for removing stop words.

    Returns:
        replace(row):The row which does not have any stop words.
    """
    # Creating a list of new stop_words
    months_stopwords = ["january", "february", "march", "april", "may", "june", "july", "august", "september",
                        "october", "november", "december", "year", "years"]
    other_stopwords = ["junior", "senior", "all genders", "w", "x", "u", "f"]

    # Extending custom stopwords to already existing ones
    stop = stopwords.words('english')
    stop.extend(months_stopwords)
    stop.extend(other_stopwords)
    stop.extend(german_cities_df['district'])

    return row['clean_job_title'].apply(lambda words: [word for word in words if word not in stop])


def create_tokens(text):
    """
    Returns the root forms of tokens.

    Parameters:
        text:The row on which summarization is to be performed.

    Returns:
        lemmatize_text(row):The row where the tokens are converted into its root form.
    """
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(w) for w in text]


# Saving the cleaned data in csv file

translated_text.to_csv("clean_data.csv", index=False)


def main():
    text_df['clean_job_title'] = text_df.apply(remove_html_tags, axis=1)
    # text_df['clean_job_title'] = text_df.apply(remove_unnecessary_values, axis=1)
    # text_df['clean_job_title'] = text_df.apply(translate_language, axis=1)
    # translated_text['clean_job_title'] = translated_text.apply(replace_strings, axis=1)
    # translated_text['clean_job_title'] = translated_text.apply(remove_punctuations, axis=1)
    # translated_text['clean_job_title'] = translated_text.apply(remove_numbers, axis=1)
    # translated_text['clean_job_title'] = translated_text.apply(convert_to_lowercase, axis=1)
    # translated_text['clean_job_title'] = translated_text.apply(tokenizing_words, axis=1)
    # translated_text['clean_job_title'] = translated_text.apply(stop_words, axis=1)
    # translated_text['clean_job_title'] = translated_text['clean_job_title'].apply(create_tokens)


if __name__ == "__main__":
    main()
