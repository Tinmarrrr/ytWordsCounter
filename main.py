from youtube_transcript_api import YouTubeTranscriptApi
import sys

def main(argv):
    if len(argv) < 1:
        print("Usage: main.py <youtube-link>")
        sys.exit(2)
    if argv[0] == "help" or argv[0] == "-h":
        print("Usage: main.py <youtube-link>")
        sys.exit(2)
    if len(argv) > 1:
        print("Usage: main.py <youtube-link>")
        sys.exit(2)
    checkArgs(argv[0])

def checkArgs(ytLink):
    if 'youtube' in ytLink:
        print('Link is valid.')
        getId(ytLink)
    else:
        print("Not a valid input file. Should be a youtube link.")

def getId(ytLink):
    videoId = ytLink.split('v=')[1].split('&')[0]
    downloadYtSub(videoId)

def downloadYtSub(videoId):
    print("Downloading data...")
    ytSub = YouTubeTranscriptApi.get_transcript(videoId, languages=['fr'])
    keepTextOnly(ytSub)

def keepTextOnly(ytSub):
    print("Keeping text only...")
    textOnly = []
    for i in range(len(ytSub)):
        textOnly.append(ytSub[i]['text'])
    countEachWord(textOnly)

def countEachWord(textOnly):
    print("Counting words...")
    wordCount = {}
    for i in range(len(textOnly)):
        for word in textOnly[i].split():
            if word not in wordCount:
                wordCount[word] = 1
            else:
                wordCount[word] += 1
    sortArray(wordCount)

def sortArray(wordCount):
    print("Sorting words...")
    sortedArray = sorted(wordCount.items(), key=lambda x: x[1], reverse=True)
    excluseSounds(sortedArray)

def excluseSounds(sortedArray):
    print("Excluding sounds...")
    finalArray = []
    for i in range(len(sortedArray)):
        if not sortedArray[i][0].startswith('['):
            finalArray.append(sortedArray[i])
    print("Your array:")
    print(finalArray)

if __name__ == "__main__":
   main(sys.argv[1:])