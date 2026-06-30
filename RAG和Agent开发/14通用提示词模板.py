from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi
prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname}，刚生了个{gender}，你帮我起个名字，简单回答。"
)
# # 调用.format方法注入信息
# prompt_text = prompt_template.format(lastname="胡",gender="女儿")
# model = Tongyi(model="qwen-max")
# res = model.invoke(input=prompt_text)
# print(res)
model = Tongyi(model="qwen-max")
chain = prompt_template | model
res = chain.invoke(input={"lastname":"胡","gender":"女儿"})
print(res)
# 此处是一种zero-shot思想