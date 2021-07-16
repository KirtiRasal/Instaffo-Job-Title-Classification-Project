
## Job Title Classification

This repository contains the python script, powering the cleaning on text data, as well as the research and documentation for feature extraction and choosing the accurate and high performance model for the "job title classification"

## Contents of the file

- The Input file given to cleaning pipeline for processing the data.
```
Input - data.json
```
- Other files like Abbrevations.json (To convert shortened form to abbrevations) and German_cities.json (To remove unnecessary stop words like german cities) required while cleaning the data
```
Assets - Abbrevations.json, German_cities.json
```
- The final cleaned data.
```
Output - Cleaned_text_data.csv
```
- The pipeline for cleaning the data.
```
Cleaning_Pipeline_Task_1 - Text_classification.py
```
- Document consisting of model research (.md file to read the document and .pdf file to download it)
```
Cleaning_Pipeline_Task_1 - Modelling the text data.pdf
```


## Environment

We need a python environment for executing the cleaning files. Latest python version (3.9.6) for 64 bit Windows 10 can be supportive to run these files.

## Installation

pip version 21.1.3

1. Install pandas 1.3.0 to read the input json file.
```
pip install pandas
```

2. Install beautifulsoup4 4.9.3 to convert the HTML tags.
```
pip install bs4
```
```
pip install lxml
```

3. Install deep_translator 1.4.4 to convert the language to english.
```
pip install deep_translator
```

4. Install nltk 3.6.2 to tokenize, lemmatize the tokens and remove stopwords.
```
pip install nltk
```

