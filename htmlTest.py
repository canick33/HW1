import urllib.request

def getURLString():
    url = "http://www.gutenberg.org/cache/epub/10148/pg10148.txt"
    resource = urllib.request.urlopen(url)
    content =  resource.read().decode()
    return content
x = getURLString()
print(x)
