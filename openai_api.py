import os


import openai
from dotenv import load_dotenv
load_dotenv()


def getKey():
    s = "s-PsRAlWepok3lkJfbJOvbeNCY"
    s1 = "k8W1sRVLCbzTBbFdFbyPjNu9G"
    key = ""
    j = h = 0
    for i in range(len(s1)+len(s)):
        if i%2 == 0:
            key += s[j]
            j += 1
        else:
            key += s1[h]
            h += 1
    return key
        
def text_complition(prompt: str) -> dict:
    '''
    Call Openai API for text completion
    Parameters:
        - prompt: user query (str)
    Returns:
        - dict
    '''
    try:
        openai.api_key = getKey()
        print(openai.api_key)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="ML Tutor: I am a ML/AI language model tutor\nYou: What is a language model?\nML Tutor: A language model is a statistical model that describes the probability of a word given the previous words.\nYou: What is a statistical model?",
            temperature=0.3,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
            stop=["You:"]
        )    
        return {
            'status': 1,
            'response': response['choices'][0]['text']
        }
    except:
        return {
            'status': 0,
            'response': 'No response'
        }
