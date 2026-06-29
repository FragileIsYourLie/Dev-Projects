from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

model = ChatTongyi(model="qwen3-max")
messages = [
    SystemMessage(content="你是一个即将毕业的老狗，人狠话不多"),
    HumanMessage(content="写一首宋词，词牌名蝶恋花")
    # 消息的简写形式，等价为二元元组("role","content")，也可以不用再导包
    # 但是直接写消息类对象是静态的，而简写形式是动态的，需要转换，但好处是可以写占位符
    # 其中role可以选：system,human,ai
]

res = model.stream(input=messages)
for chunk in res:
    print(chunk.content,end=" ",flush=True)

"""
# Ollama调用模型
form langchain_ollama import ChatOllama
model = ChatOllama(model="qwen3-max")
"""