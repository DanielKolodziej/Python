from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<div id="section-1">
<h3 data-hello="hi">Once upon a time....</h3>
</div
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<div id="plot">
<p class="story">...</p>
</div>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# direct
# print(soup.body)

# find()
el = soup.find('div')
# print(el)

#find_all() or findAll()
divs = soup.find_all('div')
# print(divs)

# target specific
div1 = soup.find(id='section-1')
divs2 = soup.find_all('div')[1]
story = soup.find(class_='story')
dataAttr = soup.find(attrs={"data-hello": "hi"})
'''
print(div1)
print(divs2)
print(story)
print(dataAttr)
'''

# select by css selectors
ex = soup.select('#section-1')
ex1 = soup.select('#section-1')[0]
ex2 = soup.select('.story')
'''
print(ex)
print(ex1)
print(ex2)
'''

# get text without the tags
text = soup.find(class_='story').get_text()
# print(text)

for item in soup.select('.sister'):
    print(item.get_text())


# navigation
el = soup.body.contents[1].find_next_sibling()
el2 = soup.find(id='section-1').find_previous_sibling()
el3 = soup.find(class_='sister').find_parent()
el4 = soup.find('h3').find_next_sibling('p')
'''
print(el)
print(el2)
print(el3)
print(el4)
'''
