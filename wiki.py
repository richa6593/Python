import wikipedia
wiki=wikipedia.page('https://en.wikipedia.org/wiki/List_of_districts_of_Jharkhand')
text=wiki.content
print(text)