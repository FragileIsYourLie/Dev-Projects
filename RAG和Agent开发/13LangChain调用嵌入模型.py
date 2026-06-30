from langchain_community.embeddings import DashScopeEmbeddings

# DashscopeEmbeddings是阿里云上的一个类对象
embed = DashScopeEmbeddings()
# 不设置模型，默认调用：text-embedding-v1
# embed_query方法是单次文字转向量
# embed_documents方法是批量单次转向量
print(embed.embed_query("我喜欢你"))
print(embed.embed_documents(["我喜欢你","今晚月亮真美","我稀饭你"]))

"""
#调用本地Ollama模型
from langchain_ollama import OllamaEmbeddings
embed = OllamaEmbeddings()
"""