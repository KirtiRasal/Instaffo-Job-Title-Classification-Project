
## Job Title Classification

This repository contains the python script, powering the cleaning on text data, as well as the research and documentation for feature extraction along with choosing the accurate and high performance model for the "job title classification" task

## Contents of the file

- The Input file given to cleaning pipeline for processing the data.
```
Input - data.json
```
- Other files like abbreviations.json (To convert shortened form to long form) and german_cities.json (To remove german city names from the job description) required while cleaning the data
```
Assets - abbreviations.json, german_cities.json
```
- The final cleaned text data.
```
Output - clean_text_data.json
```
- The pipeline for cleaning the data.
```
Cleaning_Pipeline_Task_1 - Text_classification.py
```
- The document consisting of model research
```
Model_Research_Task_2 - Model the text data.pdf
```


## Environment

We need a python environment for executing the cleaning files. Latest python version (3.9.6) for 64 bit Windows 10 can be supportive to run these files.

## Installation

pip version 21.1.3

Install packages with pip: -r requirements.txt

The following command will install the packages according to the configuration file requirements.txt. 
Run the following command where requirements.txt file is located.
```
$ pip install -r requirements.txt
```

Description of the python packages used in the text cleaning pipeline.

1. pandas is used to read the input json file.

2. html, beautifulsoup4 and lxml is used to convert the HTML tags.

3. deep_translator is used to convert the language to english.

4. nltk is used to tokenize, lemmatize the tokens and remove stopwords.


