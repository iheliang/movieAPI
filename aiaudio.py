# coding=utf-8

import dashscope
from dashscope.audio.tts_v2 import *

# 将your-dashscope-api-key替换成您自己的API-KEY
dashscope.api_key = "sk-2265cd970a0740c0b7383e6731d3a472"
model = "cosyvoice-v1"
voice = "longxiaochun"


synthesizer = SpeechSynthesizer(model=model, voice=voice)
audio = synthesizer.call("今天天气怎么样？")
print('requestId: ', synthesizer.get_last_request_id())
with open('output.mp3', 'wb') as f:
    f.write(audio)
