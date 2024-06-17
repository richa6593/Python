import urllib.request, urllib.parse, urllib.error
fhand=urllib.request.urlopen('https://en.wikipedia.org/wiki/List_of_districts_of_Jharkhand')
for line in fhand:
    print(line.decode().strip())