import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS
def texttospeech(text,filename):
    mytext=str(text)
    language='hi'
    myobj=gTTS(text=mytext,lang='hi',slow=True)
    myobj.save(filename)
def margeAudios(audios):
    combine=AudioSegment.empty()
    for audio in audios:
        combine += AudioSegment.from_mp3(audio)
    return combine
def generateSkeleton():
    audio=AudioSegment.from_mp3("railway.mp3")
    # 1 - Generate kripya dheyan dijiye
    # 1 - Generate kripya dheyan dijiye
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # 2 is from-city

    # 3 - Generate se chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # 4 is via-city

    # 5 - Generate ke raaste
#     start = 94000
#     finish = 95000
#     audioProcessed = audio[start:finish]
#     audioProcessed.export("5_hindi.mp3", format="mp3")

    # 6 is to-city

    # 6 - Generate ko jaane wali gaadi sakhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 8 is train no and name

    # 8 - Generate kuch hi samay mei platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 9 is platform number

    # 10 - Generate par aa rahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")


def generateannouncement(filename):
    df = pd.read_csv(filename, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')

    for index, item in df.iterrows():
        texttospeech(item['Source Station Name'], '2_hindi.mp3')
        texttospeech(item['Destination Station Name'], '4_hindi.mp3')
        # texttospeech(item['Source Station Name'],'_hindi.mp3')
        texttospeech(item['Train No'] + " " + item['Train Name'], '6_hindi.mp3')
        texttospeech(item['platform number'], '8_hindi.mp3')
        audios = [f"{i}_hindi.mp3" for i in range(1, 10)]
        announcement = margeAudios(audios)
        announcement.export(f"{index + 1}.mp3", format="mp3")


if __name__ == '__main__':
    print("hello world")
    generateSkeleton()
    print("now generate announcement")
    generateannouncement("Train.csv")