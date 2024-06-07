import openai

import google.generativeai as genai
from llama_cpp import Llama

def gptResponse (prompt):
    openai.api_key = 'вставить_ключ'
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            temperature = 0.5,
            messages=[{"role": "user", "content": prompt}])
    
    return response.choices[0]["message"]["content"].strip()

def geminiResponse (prompt):
    googleApi = "вставить_ключ"
    genai.configure(api_key=googleApi)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    response = model.generate_content(prompt)

    return response.text

def llamaResponse (prompt):
    llm = Llama(model_path="вставить_путь",
            n_gpu_layers=-1,
            n_ctx=2048,
            n_batch=128,
            use_mlock= True)

    response = llm(prompt,
             max_tokens=256,
             echo=False,
             temperature=0.6,
             top_p=0.3)

    return response.choices[0].text

def claudeResponse (prompt):
    client = anthropic.Anthropic(
    api_key="вставить_ключ",
    )

    response = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=10000,
    temperature=0.5,
    # system="Respond only in Yoda-speak.",
    messages=[
        {"role": "user", "content": prompt}
    ]
)
    return response