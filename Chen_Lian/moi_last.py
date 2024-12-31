import requests
from bs4 import BeautifulSoup
import re

# 请求页面
response = requests.get(
    url="https://en.wikipedia.org/wiki/Climate_change"
)

# 解析页面内容
soup = BeautifulSoup(response.content, 'html.parser')

# 获取所有段落、无序列表和有序列表
allParagraphs = soup.find(id="bodyContent").find_all(["p", "ul", "ol"])

text = ''

for item in allParagraphs:
    # 清除标签中可能存在的数字标记
    clnItem = re.sub(r'\[\d+\]', '', item.get_text())
    text += clnItem + '\n'  # 每个条目后加换行符

#print(text)

# 将结果写入文本文件
with open("wiki_theme_en3.txt", "w", encoding='utf-8') as file:
    file.write(text)
