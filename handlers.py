from socialNetworks import *
from processing import *
from models import *
import time

def googleGeminiHandler(query, key, iteration):
    # iteration = int (input ("Количество поисковых итераций:"))
    prompt = processGoogleSearch(query)
    response = geminiResponse(prompt)
    allWords = processStringGemini(response)
    print(response)
    print(allWords)
    updateDictionary(key, allWords)
    if iteration > 1:
        for _ in range(iteration - 1):
            stringWords = ' '.join(str(item) for item in allWords)
            prompt = iterativeGoogleSearch(stringWords)
            response = geminiResponse(prompt)
            words = processStringGemini(response)
            allWords.extend(words)
            updateDictionary(key, words)
            time.sleep(10)
        printDictionary()
    return allWords

def googleLocalHandler(query, key, iteration):
    # iteration = int (input ("Количество поисковых итераций:"))
    prompt = processGoogleSearch()
    response = llamaResponse(prompt)
    allWords = processString(response)
    print(response)
    print(allWords)
    key = input("Введите ключ: ")
    updateDictionary(key, allWords)
    if iteration > 1:
        for _ in range(iteration - 1):
            stringWords = ' '.join(str(item) for item in allWords)
            prompt = iterativeGoogleSearch(stringWords)
            response = llamaResponse(prompt)
            words = processString(response)
            allWords.extend(words)
            updateDictionary(key, words)
            time.sleep(10)
            printDictionary()
    return allWords

def googleGptHandler(query, key, iteration):
    # iteration = int (input ("Количество поисковых итераций:"))
    prompt = processGoogleSearch()
    response = gptResponse(prompt)
    allWords = processString(response)
    print(response)
    print(allWords)
    key = input("Введите ключ: ")
    updateDictionary(key, allWords)
    if iteration > 1:
        for _ in range(iteration - 1):
            stringWords = ' '.join(str(item) for item in allWords)
            prompt = iterativeGoogleSearch(stringWords)
            response = gptResponse(prompt)
            words = processString(response)
            allWords.extend(words)
            updateDictionary(key, words)
            time.sleep(10)
            printDictionary()
    return allWords


def vkCommentsGeminiHandler(url, key):
    prompt = processVk(url)
    response = geminiResponse(prompt)
    words = processStringGemini(response)
    print(words)
    updateDictionary(key, words)
    printDictionary()
    return words

def vkCommentsLocalHandler(url, key):
    prompt = processVk(url)
    response = llamaResponse(prompt)
    words = processString(response)
    print(words)
    updateDictionary(key, words)
    printDictionary()
    return words

def vkCommentsGptHandler(url, key):
    prompt = processVk(url)
    response = gptResponse(prompt)
    words = processString(response)
    print(words)
    updateDictionary(key, words)
    printDictionary()
    return words

def vkCommentsClaudeHandler(url, key):
    prompt = processVk(url)
    response = claudeResponse(prompt)
    words = processString(response)
    print(words)
    updateDictionary(key, words)
    printDictionary()
    return words


def youtubeCommentsGeminiHandler(url, key):
    prompt = processVideo(url)
    response = geminiResponse(prompt)
    words = processStringGemini(response)
    print(words)
    updateDictionary(key, words)
    printDictionary()
    return words

def youtubeCommentsLocalHandler(url, key):
    prompt = processVideo(url)
    response = llamaResponse(prompt)
    words = processString(response)
    print(words)
    updateDictionary(key, words)
    printDictionary()
    return words

def youtubeCommentsGptHandler(url, key):
    prompt = processVideo(url)
    response = gptResponse(prompt)
    words = processString(response)
    print(words)
    updateDictionary(key, words)
    printDictionary()
    return words

def youtubeCommentsClaudeHandler(url, key):
    prompt = processVideo(url)
    response = claudeResponse(prompt)
    words = processString(response)
    print(words)
    updateDictionary(key, words)
    printDictionary()
    return words


def vkSearchGeminiHandler(query, key):
    prompt = processSearchVk(query)
    response = geminiResponse(prompt)
    words = processStringGemini(response)
    print(words)
    updateDictionary(key, words)
    printDictionary()
    return words

def vkSearchLocalHandler(query, key):
    prompt = processSearchVk(query)
    response = llamaResponse(prompt)
    words = processString(response)
    print(words)
    updateDictionary(key, words)
    printDictionary()
    return words

def vkSearchGptHandler(query, key):
    prompt = processSearchVk(query)
    response = gptResponse(prompt)
    words = processString(response)
    print(words)
    updateDictionary(key, words)
    printDictionary()
    return words