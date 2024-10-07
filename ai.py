import os
import dashscope
from openai import OpenAI
from dashscope.audio.tts_v2 import *

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
completion = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': 'ai什么时候出现的？'}
    ]
)

print(completion.choices[0].message.content)
aicontent = completion.choices[0].message.content

# 将your-dashscope-api-key替换成您自己的API-KEY
dashscope.api_key = os.getenv("DASHSCOPE_API_KEY")
model = "cosyvoice-v1"
voice = "longxiaochun"


synthesizer = SpeechSynthesizer(model=model, voice=voice)
audio = synthesizer.call(aicontent)
print('requestId: ', synthesizer.get_last_request_id())
with open('output.mp3', 'wb') as f:
    f.write(audio)
