from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate
from langchain_community.llms.tongyi import Tongyi

# 示例模板
example_template = PromptTemplate.from_template("单词：{word}，反义词：{antonym}")
# 示例数据
example_data = [
    {"word":"大","antonym":"小"},
    {"word":"上","antonym":"下"}
]
few_shot_template=FewShotPromptTemplate(
    example_prompt=example_template,
    examples=example_data,
    prefix="给我反义词，下面是示例",
    suffix="基于以上示例，给我{input_word}的反义词",
    input_variables=['input_word']
)

text_template = few_shot_template.invoke(input={"input_word":"美好"}).to_string()
print(text_template)

model = Tongyi(model="qwen-max")
print(model.invoke(input=text_template))