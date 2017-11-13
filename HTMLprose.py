import urllib.request

def getURLString():
    url = "http://www.gutenberg.org/cache/epub/10148/pg10148.txt"
    resource = urllib.request.urlopen(url)
    content =  resource.read().decode()
    return content

def getContents():
    book = open("//Users//hollyholden//Documents//GitHub//HW1//book.txt","r", encoding = "UTF-8")
    text = str(book.read())
    book.close()
    
    text = getURLString()
    text = text.split("*** START OF THIS PROJECT GUTENBERG EBOOK THE MERRY ADVENTURES OF ROBIN HOOD ***",1)[1]
    text = text.split("*** END OF THIS PROJECT GUTENBERG EBOOK THE MERRY ADVENTURES OF ROBIN HOOD ***",1)[0]
    text = text.replace("\n"," ")
    text = text.replace("\r"," ")
    text = text.lower()
    words = text.split(" ")
    
    return words

def splitChapterTitles(chapterText):
    chapterList = []
    lastBreak =0
    for j in range (0,23):
        chapter = []
        for i in range (lastBreak,len(chapterText)-1):
            if chapterText[i] == "1":
                lastBreak =i+1
                break
            else:
                chapter.append(chapterText[i])              
        chapterList.append(chapter)
    return chapterList
            
def getChapterTitles():
    bookText = getContents()
    chapterStart = bookText.index("preface")
    chapterEnd = bookText.index("epilogue")
    chapters = bookText[chapterStart:chapterEnd+9]
    chapters = splitChapterTitles(chapters)
    return chapters

def indexChapterStarts():
    bookText = getContents() 
    chapters = getChapterTitles()
    chapterStarts =[]
    for j in range(0,len(chapters)):
        count = 1
        for i in range(0,len(bookText)):
            if bookText[i] == chapters[j][0]:
                ifChapter = True
                for l in range(0,len(chapters[j])):
                    if chapters[j][l] == bookText[i+l]:
                        ifChapter = True
                    else:
                        ifChapter = False
                        break
                if ifChapter:
                    if count ==2:
                        chapterTitle = [i,i+len(chapters[j])]
                        chapterStarts.append(chapterTitle)
                    else:
                        count = count+1
    return chapterStarts
                    
def getChapterText():
    bookText = getContents()
    #chapterDomain = indexChapterStarts()
    #the index chapter starts works with utf-8 so I just copied its output when i run it with that.
    chapterDomain= [[183, 184], [683, 691], [5232, 5237], [7818, 7823], [9804, 9810], [14084, 14090], [18006, 18010], [22288, 22294], [24921, 24928], [29625, 29632], [33462, 33467], [37133, 37140], [42252, 42258], [47257, 47263], [52969, 52974], [57317, 57323], [63256, 63265], [68963, 68968], [74501, 74505], [81628, 81634], [89000, 89005], [96456, 96462], [103409, 103415], [109981, 109982]]
    textByChapter = []
    for i in range(0,len(chapterDomain)-1):
        textByChapter.append(bookText[chapterDomain[i][1]:chapterDomain[i+1][0]])
    return textByChapter

def checkUsed(word,usedWords):
    for i in range(0,len(usedWords)):
        if usedWords[i] == word:
            return True
        elif word == "":
            return True
    return False
                          
def countCommonWords(text):
    commonWords = [["x",1],["x",1],["x",1],["x",1],["x",1],["x",1],["x",1],["x",1],["x",1],["x",1],["x",1],["x",1],["x",1],["x",1],["x",1],["x",1],["x",1],["x",1],["x",1],["x",1]]
    usedWords = ["the","and","or","his","of", "for","a", "that","to","he","i","in",","," "]
    #i included those words in the used words array because they cluttered everything up as they are used often
    for j in range(0,len(text)):
        if (not checkUsed(text[j],usedWords)):
                usedWords.append(text[j])
                score = 0
                for i in range(0,len(text)):
                    if text[i] ==text[j]:
                        score+=1
                if score > commonWords[0][1]:
                    commonWords[0] = [text[j],score]
                    commonWords = sorted(commonWords,key=lambda l:l[1])

    commonWords = sorted(commonWords,key=lambda l:l[1], reverse = True)
    return commonWords

def commonWordsByChapter():
    text = getChapterText()
    wordsByChapter = []
    for i in range(0,len(text)):
        wordsByChapter.append(countCommonWords(text[i]))
        print("chapter",i, "of", len(text)-1)
    
    return wordsByChapter
        
def printCommonWords():
 #   titles = getChapterTitles() <-- same thing as index chapter starts
    titles = [['preface'], ['how', 'robin', 'hood', 'came', 'to', 'be', 'an', 'outlaw'], ['robin', 'hood', 'and', 'the', 'tinker'], ['the', 'shooting', 'match', 'at', 'nottingham', 'town'], ['will', 'stutely', 'rescued', 'by', 'his', 'companions'], ['robin', 'hood', 'turns', 'butcher'], ['little', 'john', 'goes', 'to', 'nottingham', 'fair'], ['how', 'little', 'john', 'lived', 'at', 'the', "sheriff's"], ['little', 'john', 'and', 'the', 'tanner', 'of', 'blyth'], ['robin', 'hood', 'and', 'will', 'scarlet'], ['the', 'adventure', 'with', 'midge', 'the', "miller's", 'son'], ['robin', 'hood', 'and', 'allan', 'o', 'dale'], ['robin', 'hood', 'seeks', 'the', 'curtal', 'friar'], ['robin', 'hood', 'compasses', 'a', 'marriage'], ['robin', 'hood', 'aids', 'a', 'sorrowful', 'knight'], ['how', 'sir', 'richard', 'of', 'the', 'lea', 'paid', 'his', 'debts'], ['little', 'john', 'turns', 'barefoot', 'friar'], ['robin', 'hood', 'turns', 'beggar'], ['robin', 'hood', 'shoots', 'before', 'queen', 'eleanor'], ['the', 'chase', 'of', 'robin', 'hood'], ['robin', 'hood', 'and', 'guy', 'of', 'gisbourne'], ['king', 'richard', 'comes', 'to', 'sherwood', 'forest'], ['epilogue']]
    wordsByChapter = commonWordsByChapter()
    for i in range(0,len(wordsByChapter)):
        chapterTitle = " ".join(titles[i])
        chapterTitle = chapterTitle.upper()
        print("Common words in chapter",i,",",chapterTitle,":", "\n")
        for j in range(0,len(wordsByChapter[i])):
            print(wordsByChapter[i][j][0],"|", wordsByChapter[i][j][1])
        print("\n","********************************")
            

printCommonWords()


