import re
import os
import json
import requests
from bs4 import BeautifulSoup
from googlesearch import search

def getFile (fileName):
    with open(fileName, 'r', encoding = "utf-8") as f:
        return f.read()

def processStringGemini (string):
    string = string.lower().split(',')
    result = []
    for part in string:
        trimmedPart = part.strip()
        if trimmedPart:
            result.append(trimmedPart)

    return result

def processString (string):
    string = string.lower()
    if '\n' in string:
        string = '\n'.join(string.split('\n')[1:])
        string = re.sub(r'ключевые слова\s*:?\s*', '', string, flags=re.IGNORECASE)
        phrases = re.split(r'\n', string)
        result = [re.sub(r'^[\d\W]+', '', phrase).strip() for phrase in phrases if phrase.strip()]
    else:
        string = re.sub(r'ключевые слова\s*:?\s*', '', string, flags=re.IGNORECASE)
        string = re.sub(r'[^a-zA-Zа-яА-Я\s,]', '', string)
        result = [phrase.strip() for phrase in string.split(',') if phrase.strip()]

    return result

def getAllP (url):
    response = requests.get(url)
    htmlContent = response.content

    parser = BeautifulSoup(htmlContent, 'html.parser')
    pElements = parser.find_all('p')

    texts = '\n'.join([p.get_text() for p in pElements])

    return texts

def googleSearch (query, amount):
    results = []
    for link in search(query, tld="co.in", num = amount, stop = amount, pause=2):
        results.append(link)
    return results

def countTokens (texts):
    tokens = []
    for text in texts:
        text = text.strip()
        textTokens = re.split(r'\s+', text)
        tokens.extend(textTokens)

    return len(tokens)

def processGoogleSearch (query):
    amount = 3
    searchResult = googleSearch(query, amount)
    print (searchResult)
    texts = ""
    for page in searchResult:
        text = getAllP(page)
        texts += text + "\n"
    # print (texts)
    print (f"{countTokens(texts)} токенов")
    prompt = f"Выдели из данных текстов ключевые слова (личности, названия, события), которые имеют или могут иметь отношение к '{query}', и напиши одной строкой на русском языке: \n '{texts}'"
    return prompt

def iterativeGoogleSearch (words):
    query = words
    print (f"Поисковый запрос: {query}")
    amount = 3
    searchResult = googleSearch(query, amount)
    print (searchResult)
    texts = ""
    for page in searchResult:
        text = getAllP(page)
        texts += text + "\n"
    # print (texts)
    print (f"{countTokens(texts)} токенов")
    prompt = f"Выдели из данных текстов ключевые слова (личности, названия, события), которые имеют или могут иметь отношение к предоставленному тексту, и напиши ответ одной строкой на русском языке: \n '{texts}'"

    return prompt

def processFile ():
    file = "text.txt"
    output = getFile(file)
    prompt = f"Выдели ключевые слова из следующего текста: '{output}'"
    return prompt

def printDictionary():
    with open("dictionary.json", "r") as file:
        data = json.load(file)  
        output = ""
        for key, value in data.items():
            # print(f"{key}: {value}") 
            output += f"{key}: {value}\n"
        return output

def updateDictionary(key, array):
    if os.path.exists("dictionary.json") and os.stat("dictionary.json").st_size > 0:
        try:
            with open("dictionary.json", "r") as file:
                dictionary = json.load(file)
        except json.decoder.JSONDecodeError:
            dictionary = {}
    else:
        dictionary = {}

    if key in dictionary:
        existingValues = set(dictionary[key])
        newValues = set(array)
        updatedValues = existingValues.union(newValues)
        dictionary[key] = list(updatedValues)
    else:
        dictionary[key] = array

    with open("dictionary.json", "w") as file:
        json.dump(dictionary, file, indent=4)
