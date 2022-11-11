import os,sys,requests
from translate import Translator

data = sys.argv

def fy(text):
    print('(1)' + requests.get('http://fanyi.youdao.com/translate',params={'doctype':'json',"type":'AUTO','i':text}).json()['translateResult'][0][0]['tgt'] + '\n')

def translate(text):
    try:
        print('(2)' + Translator(from_lang=data[1],to_lang=data[2]).translate(text))
    except BaseException:
        pass

if str(len(data)) == '1':
    text = str(input('>'))
    fy(text)
    exit()

del data[0]
if list(data[0])[0] == '-':
    if data[0] == '-l':
        while True:
            text = str(input('>'))
            fy(text)
            translate(text)
    elif data[0] == '-c':
        del data[0]
        text = str(os.system(' '.join(data)))
        fy(text)
        translate(text)
    elif data[0] == '-h':
        print('fy [需要翻译的内容或参数留空默认单行翻译模式]\n    -c 命令行翻译模式\n    -l 行翻译模式\n    -h 显示帮助')
else:
    text = ' '.join(data)
    fy(text)
