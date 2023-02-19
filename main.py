import requests

def saveFile(url):
    request = requests.get(url=url).content
    open('shakespeare.txt', 'wb').write(request)

def main():
    saveFile('https://www.gutenberg.org/cache/epub/100/pg100.txt')

    with open('shakespeare.txt', 'r') as f:
        text = f.read().lower().split()

    # n = len(text)

    wordDict = {}

    for word in text:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    topTen = sorted(wordDict.items(), key=lambda x:x[1], reverse=True)[:10]

    print("Top 10 Words Found in Shakespeare")

    for i in range(0, 10):
        print("{0}. {1} : {2}".format(i+1,topTen[i][0],topTen[i][1]))

if __name__ == '__main__':
    main()
