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

import nltk
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Path of all the files
input_file_path = 'Input/data.json'
assets_german_cities = 'Assets/german_cities.json'
assets_abbreviations = 'Assets/abbreviations.json'
output_file_path = 'Output/clean_text_data.json'

# Reading abbreviations json file
with open(assets_abbreviations) as json_file:
    abbreviations = json.load(json_file)


# Load the input json file to read the data and store in dataframe
def load_data():
    """ Load the json file and return a Dataframe. """
    dataframe = pd.read_json(input_file_path)
    return dataframe


# drop null values
def drop_null_values(dataframe):
    """ Drop null values, reset the index by dropping it and return a Dataframe. """
    dataframe.dropna(inplace=True)
    dataframe.reset_index(drop=True, inplace=True)
    return dataframe


# Creating a new column to store clean text
def create_new_column(dataframe):
    """
    Function to create a new column to store the clean text.

    Parameters:
        dataframe: The dataframe in which we have to create a new column.

    Returns:
        dataframe:The dataframe with the new column .

     """
    if 'clean_job_title' not in dataframe:
        dataframe['clean_job_title'] = dataframe['job_title']
    return dataframe


# Creating custom stop words
def custom_stop_words():
    """
    Function to create a custom stop words and extend it with original stop words.

    Returns:
        dataframe: The list of original and new stop words .

     """
    # Reading the data of german_cities from the json files
    german_cities_df = pd.read_json(assets_german_cities)

    # Converting the name column from german_cities_df to lowercase
    german_cities_df['name'] = german_cities_df['name'].apply(lambda x: x.lower())

    # Creating a list of new stop_words to remove domain specific stop words
    months_stopwords = ["january", "february", "march", "april", "may", "june", "july", "august", "september",
                        "october", "november", "december", "year", "years"]
    other_stopwords = ["junior", "senior", "all genders", "w", "x", "u", "f"]

    # Extending custom stopwords to already existing ones
    stop = stopwords.words('english')
    stop.extend(months_stopwords)
    stop.extend(other_stopwords)
    stop.extend(german_cities_df['name'])

    return stop


# converting html tags
def remove_html_tags(row):
    """
    Function to replace the abbreviations to their full form
    Example: IT - Information Technology

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
    Function to replace the abbreviations to their full form
    Example: IT - Information Technology

    Parameters:
        row:The row from the dataframe which is to be replaced.

    Returns:
        row:The row which replace the abbreviations to their full form.
    """

    text = row['clean_job_title']
    for key, value in abbreviations[row['category']].items():
        text = text.replace(key, value)
    return text


# Remove the unnecessary punctuations
def remove_punctuations(row):
    """
    Function to remove punctuations which are not required and keep the one which are required
    Example of few words (C++, C#, .Net)

    Parameters:
        row: The row from the dataframe

    Returns:
        row: row having the text without specific punctuations
    """

    text = row['clean_job_title']
    if re.findall(r"[-!?@&*\(\)/:;,|%\'\`\"\_\n]", text):
        text = re.sub(r"[-!?@&*\(\)/:;,|%\'\`\"\_\n]", '', text)
    return text


def main():
    # Load the data
    text_df = load_data()

    # Function call to drop null values
    text_df = drop_null_values(text_df)

    # Function call to create a new column
    text_df = create_new_column(text_df)

    # replace html values
    text_df['clean_job_title'] = text_df.apply(remove_html_tags, axis=1)

    # Remove unnecessary values like (m/w/d) and various combinations
    text_df['clean_job_title'] = text_df.apply(lambda row: re.sub(r'\([a-zA-Z/|]*/[a-zA-Z/|]*\)', '',
                                                                  row['clean_job_title']), axis=1)

    # Translate all german language to english
    text_df['clean_job_title'] = text_df.apply(lambda row: GoogleTranslator(source='de', target='en')
                                               .translate(row['clean_job_title']), axis=1)

    # Replace abbreviations
    text_df['clean_job_title'] = text_df.apply(replace_abbreviations, axis=1)

    # Remove punctuations
    text_df['clean_job_title'] = text_df.apply(remove_punctuations, axis=1)

    # Remove numeric values [0-9]
    text_df['clean_job_title'] = text_df.apply(lambda row: re.sub(r'\d+', '', row['clean_job_title']),
                                               axis=1)

    # Remove extra space
    text_df['clean_job_title'] = text_df['clean_job_title'].apply(lambda x: re.sub(' +', ' ', x))

    # Convert the sentences to lower case
    text_df['clean_job_title'] = text_df.apply(lambda row: row['clean_job_title'].lower(), axis=1)

    # Tokenize the sentence
    text_df['clean_job_title'] = text_df.apply(lambda row: word_tokenize(row['clean_job_title']),
                                               axis=1)

    # Remove stop words along with custom stop words
    stop = custom_stop_words()
    text_df['clean_job_title'] = text_df['clean_job_title'].apply(
        lambda x: [item for item in x if item not in stop])

    # Spelling correction
    spell = SpellChecker()
    text_df['clean_job_title'] = text_df['clean_job_title'].apply(lambda row: [spell.correction(word) for word in row])

    # Lemmatize the words (As we don't want to loose the adverbs of few tokens, we will only apply lemmatization)
    lemmatizer = WordNetLemmatizer()
    text_df['clean_job_title'] = text_df['clean_job_title'].apply(
        lambda row: [lemmatizer.lemmatize(w) for w in row])

    print(text_df['clean_job_title'][0:20])
    # Saving the cleaned data in json file
    text_df.to_json(output_file_path, orient='records')


if __name__ == "__main__":
    main()
