# 1、获取client对象
# 2、调用模型
# 3、处理结果
from openai import OpenAI
client = OpenAI(base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")
response = client.chat.completions.create(
    model = "qwen3-max",
    messages = [
        {"role":"system","content":"你是一个python编程专家，不说废话简单回答"},
        {"role":"assistant","content":"我是编程专家，且话不多"},
        {"role":"user","content":"输出1-19，用Python代码"}
    ]
)
print(response.choices[0].message.content)