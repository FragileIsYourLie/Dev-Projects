import json

d = {
    "name" : "周杰伦",
    "age" : 20,
    "gender" : "男"
}
print(d)
# 字典转json（注意json是双引号）,生成一个json对象
s = json.dumps(d, ensure_ascii=False)
print(s)

l = [
{
    "name" : "周杰伦",
    "age" : 20,
    "gender" : "男"
},
{
    "name" : "蔡依林",
    "age" : 23,
    "gender" : "女"
},
{
    "name" : "小明",
    "age" : 18,
    "gender" : "男"
}
]
# 列表转json，生成一个json数组
print(json.dumps(l, ensure_ascii=False))

json_str = '{"name": "周杰伦", "age": 20, "gender": "男"}'
json_array = '[{"name": "周杰伦", "age": 20, "gender": "男"}, {"name": "蔡依林", "age": 23, "gender": "女"}, {"name": "小明", "age": 18, "gender": "男"}]'

print(json.loads(json_str),type(json.loads(json_str)))
print(json.loads(json_array),type(json.loads(json_array)))