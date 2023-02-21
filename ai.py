import os
import openai

s = "s-K5OIbvXTJJ3lkJyUaBAzJk0K"
s1 = "kCTHGDc5SzGTBbFePNevcTWBt"
key = ""
j = h = 0
for i in range(len(s1)+len(s)):
    if i%2 == 0:
        key += s[j]
        j += 1
    else:
        key += s1[h]
        h += 1
        
openai.api_key = key

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Q: How many eyes you have\n",
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"]
) 

print(response['choices'][0]['text'])
