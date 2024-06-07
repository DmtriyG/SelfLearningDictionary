from flask import Flask, render_template, request, jsonify
from handlers import *
import json

app = Flask(__name__)

@app.route('/')
def mainPage():
    return render_template('index.html')

@app.route('/app', methods=['GET', 'POST'])
def appPage():
    if request.method == 'POST':
        model = request.form.get('model')
        action = request.form.get('action')

        if action == 'google_search':
            query = request.form.get('google_search')
            key = request.form.get('dictionary_key3').lower()
            iteration = int(request.form.get('iterations'))
            if model == 'Gemini':
                data = googleGeminiHandler(query, key, iteration)
                return render_template('result.html', data = data, key = key)
            elif model == 'Local':
                data = googleLocalHandler(query, key, iteration)
                return render_template('result.html', data = data, key = key)
            elif model == 'GPT':
                data = googleGptHandler(query, key, iteration)
                return render_template('result.html', data = data, key = key)
            else:
                return "Выберите модель"
        elif action == 'vk_post':
            url = request.form.get('vk_post')
            key = request.form.get('dictionary_key').lower()
            if model == 'Gemini':
                data = vkCommentsGeminiHandler(url, key)
                return render_template('result.html', data = data, key = key)
            elif model == 'Local':
                data = vkCommentsLocalHandler(url, key)
                return render_template('result.html', data = data, key = key)
            elif model == 'GPT':
                data = vkCommentsGptHandler(url, key)
                return render_template('result.html', data = data, key = key)
            elif model == 'Claude':
                data = vkCommentsClaudeHandler(url, key)
                return render_template('result.html', data = data, key = key)
            else:
                return "Выберите модель"
        elif action == 'youtube_video':
            url = request.form.get('youtube_video')
            key = request.form.get('dictionary_key1').lower()
            if model == 'Gemini':
                data = youtubeCommentsGeminiHandler(url, key)
                return render_template('result.html', data = data, key = key)
            elif model == 'Local':
                data = youtubeCommentsLocalHandler(url, key)
                return render_template('result.html', data = data, key = key)
            elif model == 'GPT':
                data = youtubeCommentsGptHandler(url, key)
                return render_template('result.html', data = data, key = key)
            elif model == 'Claude':
                data = youtubeCommentsClaudeHandler(url, key)
                return render_template('result.html', data = data, key = key)
            else:
                return "Выберите модель"
        elif action == 'vk_search':
            url = request.form.get('vk_search')
            key = request.form.get('dictionary_key2').lower()
            if model == 'Gemini':
                data = vkSearchGeminiHandler(query, key)
                return render_template('result.html', data = data, key = key)
            elif model == 'Local':
                data = vkSearchLocalHandler(query, key)
                return render_template('result.html', data = data, key = key)
            elif model == 'GPT':
                data = vkSearchGptHandler(query, key)
                return render_template('result.html', data = data, key = key)
            else:
                return "Выберите модель"
    
    return render_template('app.html')

@app.route('/dictionary')
def dictionaryPage():
    def getDictionary():
        try:
            with open("dictionary.json", "r") as file:
                data = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            data = {}
        return data
    
    dictionaryData = getDictionary()
    
    if not dictionaryData:
        dictionaryData = None
    
    return render_template('dictionary.html', data=dictionaryData)

@app.route('/delete_variable', methods=['POST'])
def deleteVariable():
    data = request.get_json()
    key = data['key']
    variable = data['variable']
    
    with open("dictionary.json", "r") as file:
        dictionary = json.load(file)
    
    if key in dictionary:
        if variable in dictionary[key]:
            dictionary[key].remove(variable)
            if not dictionary[key]:  
                del dictionary[key]
    
    with open("dictionary.json", "w") as file:
        json.dump(dictionary, file, ensure_ascii=False, indent=4)
    
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)