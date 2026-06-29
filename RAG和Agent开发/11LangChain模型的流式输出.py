from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-max")
res = model.stream(input="你是谁呀，能做什么？")

for chunk in res:
    print(chunk,end=" ",flush=True)
# flush为 True使得结果可以立刻显示出来，实现流式输出是因为stream方法

"""
# 本地Ollama调用模型的方法
from langchain_ollama import OllamaLLM
model = OllamaLLM(model="qwen3")
"""