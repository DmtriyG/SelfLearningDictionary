import vk_api
import re
from googleapiclient.discovery import build

def cleanText(text):
    pattern = r"[^a-zA-Zа-яА-Я0-9\s]"
    cleanedText = re.sub(pattern, '', text)
    return cleanedText

def extractVkId(url):
    pattern = r"wall-(\d+)_(\d+)"
    match = re.search(pattern, url)

    if match:
        ownerId = -int(match.group(1))  
        postId = int(match.group(2))
        return ownerId, postId
    else:
        return None, None
    
def extractVideoUrl(url):
    if "youtu.be/" in url:
        parts = url.split("youtu.be/")
        videoId = parts[1].split("?")[0] if "?" in parts[1] else parts[1]
    else:
        parts = url.split("?v=")
        videoId = parts[1] if len(parts) > 1 else ""
    
    return videoId

def getCommentsYoutube(videoId):
    apiGoogle = 'вставить_ключ'
    youtube = build('youtube', 'v3', developerKey=apiGoogle)
    allComments = []

    try:
        nextPageToken = None
        
        while True:
            comments = youtube.commentThreads().list(
                part='snippet',
                videoId=videoId,
                maxResults=100,
                pageToken=nextPageToken,
                textFormat='plainText'
            ).execute()
            
            for item in comments['items']:
                comment = item['snippet']['topLevelComment']['snippet']
                text = comment['textDisplay']
                if re.search(r'[\w]', text):
                    cleanedText = cleanText(text)
                    allComments.append(cleanedText)
            
            if 'nextPageToken' in comments:
                nextPageToken = comments['nextPageToken']
            else:
                break
        
        return '\n'.join(allComments)
    
    except Exception as e:
        print(f'Ошибка:: {e}')
        return ''

def getCommentsVk(postId, ownerId):
    token = 'вставить_ключ'
    vkSession = vk_api.VkApi(token=token) 
    vk = vkSession.get_api()
    allComments = []
    offset = 0

    while True:
        response = vk.wall.getComments(owner_id=ownerId, post_id=postId, count=100, offset=offset)
        comments = response['items']
        if not comments:
            break
        
        allComments.extend(comments)
        offset += 100
    commentsText = [comment['text'] for comment in allComments]
    allCommentsText = '\n'.join(commentsText)

    return allCommentsText

def searchVk (query):
    vkSession = vk_api.VkApi(token='вставить_ключ')
    vk = vkSession.get_api()
    amount = 100
    postsText = ""
    offset = 0

    while len(postsText.split('\n')) < amount:
        response = vk.newsfeed.search(q=query, count=amount, offset=offset)
        
        for post in response['items']:
            postsText += post['text'] + '\n'
        
        offset += amount
        
        if len(response['items']) == 0:
            break

    return '\n'.join(postsText.split('\n')[:amount])

def processVideo (url):
    # url = input ("Ссылка на видео YouTube: ")
    videoId = extractVideoUrl(url)
    output = getCommentsYoutube(videoId)
    print (output)
    prompt = f"Напиши только ключевые слова из следующего текста и напиши одной строкой на русском языке:: '{output}'"
    return prompt

def processVk (url):
    # url = input("Ссылка на пост ВК: ")
    ownerID, postID = extractVkId(url)
    output = getCommentsVk(postID, ownerID)
    print (output)
    prompt = f"Напиши только ключевые слова из следующего текста и напиши одной строкой на русском языке:: '{output}'"
    return prompt

def processSearchVk (query):
    # query = input("Поисковый запрос ВК: ")
    output = searchVk(query)
    print (output)
    prompt = f"Выдели из данных текстов ключевые слова (личности, названия, события), которые имеют или могут иметь отношение к {query}, и напиши одной строкой на русском языке: \n '{output}'"
    return prompt
