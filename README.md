
## Job Title Classification

This repository contains the python script, powering the cleaning on text data, as well as the research and documentation for feature extraction along with choosing the accurate and high performance model for the "job title classification" task

## Contents of the file

- The Input file 'data.json' given to cleaning pipeline for processing the data is stored inside Input folder.
```
Input/data.json
```
- Other files like 'abbreviations.json' (To convert shortened form to long form) and 'german_cities.json' (To remove german city names from the job description) required while cleaning the data are stored inside Assets folder.
```
Assets/abbreviations.json, Assets/german_cities.json
```
- The final cleaned text data 'clean_text_data.json' is stored inside Output folder
```
Output/clean_text_data.json
```
- The pipeline for cleaning the data 'text_classification.py' is stored inside Cleaning_Pipeline_Task_1 folder.
```
Cleaning_Pipeline_Task_1/text_classification.py
```
- The document consisting of model research 'Model the text data.pdf' is stored inside Model_Research_Task_2 folder
```
Model_Research_Task_2/ Model the text data.pdf
```
- To install Python packages with pip and requirements.txt
```
requirements.txt
```

## Steps followed while cleaning the text data

![alt text](https://github.com/KirtiRasal/Instaffo-Job-Title-Classification-Project/blob/main/Images/cleaning%20pipeline%20image.png?raw=true)

## Environment

We need a python environment for executing the cleaning files. Latest python version (3.9.6) for 64 bit Windows 10 can be supportive to run these files.

## Installation

pip version 21.1.3

Install packages with pip: -r requirements.txt

The following command will install the packages according to the configuration file requirements.txt. 
Run the following command where requirements.txt file is located.
```
pip install -r requirements.txt
```

Description of the python packages used in the text cleaning pipeline.

1. pandas is used to read the input json file.

2. html, beautifulsoup4 and lxml is used to convert the HTML tags.

3. deep_translator is used to convert the language to english.

4. pyspellchecker to correct the spelling of tokens.

5. nltk is used to tokenize, lemmatize the tokens and remove stopwords.

## Execution

Change the directory of the file where project is located.
Run the text_classification.py python file using below command

``` python Cleaning_Pipeline_Task_1/text_classification.py ```

After the command is executed, output will be stored in ``` Output/clean_text_data.json ``` folder


