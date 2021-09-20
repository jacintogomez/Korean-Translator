from konlpy.tag import Okt,Hannanum,Kkma,Komoran
from konlpy.utils import pprint
from googletrans import Translator
from pandas import DataFrame

"""
Insert text in korean
"""
# given='''multiline text'''
given=str(input('Enter text in Korean: '))
okt=Okt()
hannanum=Hannanum()
kkma=Kkma()
komoran=Komoran()
translator=Translator()
processed=given.split('\n')

def oktmethod(text):
    """Word classification"""
    ttrans=(okt.pos(text,norm=True,stem=True,join=True))
    korean=[]
    pos=[]
    for x in ttrans:
        separate=x.split('/')
        korean.append(separate[0])
        pos.append(separate[1])
    """Translate Korean words to English"""
    english=[]
    counter=0
    for word in korean:
        if pos[counter]=="Josa":
            english.append("--")
        else:
            toeng=translator.translate(word)
            eng=f'{toeng.text}'
            english.append(eng)
        counter+=1
    """Make master list to be used for data frame"""
    data=[]
    for num in range(0,len(ttrans)):
        options=[korean,pos,english]
        temp=[]
        for o in options:
            temp.append(o[num])
        data.append(temp)
    """Final execution"""
    print(DataFrame(data,columns=['Korean','PoS','English']))

# def hannamethod(text):
#     print(hannanum.analyze(u'웃으면 더 행복합니다'))
#
# def kkmethod(text):
#     pass

"""Calling all methods"""
for line in processed:
    oktmethod(line)
    print('Original text: '+line)




"""Code not used"""
# generic translation
# print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
# koreanlist=DataFrame(ttrans,columns=['Korean'])
