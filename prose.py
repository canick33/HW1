def getContents():
    book = open("//Users//hollyholden//Documents//GitHub//HW1//book.txt","r", encoding = "UTF-8")
    text = str(book.read())
    book.close()
    text = text.split("*** START OF THIS PROJECT GUTENBERG EBOOK THE MERRY ADVENTURES OF ROBIN HOOD ***",1)[1]
    text = text.split("*** END OF THIS PROJECT GUTENBERG EBOOK THE MERRY ADVENTURES OF ROBIN HOOD ***",1)[0]
    words = text.split(" ")
    return words

bookText = getContents()
print(bookText)

