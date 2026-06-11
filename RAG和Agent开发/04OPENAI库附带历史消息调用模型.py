from openai import OpenAI

# 1、获取client对象
client = OpenAI(base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")

# 2、调用模型
response = client.chat.completions.create(
    model = "qwen3-max",
    messages = [
        {"role":"system","content":"你是一个AI助理，回答很简洁"},
        {"role":"user","content":"小明有两条宠物狗"},
        {"role":"assistant","content":"好的"},
        {"role":"user","content":"小红有三只宠物猫"},
        {"role":"assistant","content":"好的"},
        {"role":"user","content":"总共有几个宠物？"}
    ],
    stream = True # 开启流式输出
)

# 3、处理结果
# print(response.choices[0].message.content)
for chunck in response:
    print(chunck.choices[0].delta.content,end=" ",flush=True) #flush=True立刻刷新缓冲区显示结果