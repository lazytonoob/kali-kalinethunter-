import os,sys,requests

data = sys.argv

def translate(text):
    print(requests.get('http://fanyi.youdao.com/translate',params={'doctype':'json',"type":'AUTO','i':text}).json()['translateResult'][0][0]['tgt'])

if str(len(data)) == '1':
    text = str(input('>'))
    translate(text)
    exit()

del data[0]
if list(data[0])[0] == '-':
    if data[0] == '-l':
        while True:
            text = str(input('>'))
            translate(text)
    elif data[0] == '-c':
        del data[0]
        text = str(os.system(' '.join(data)))
        translate(text)
    elif data[0] == '-h':
        print('fy [需要翻译的内容或参数留空默认单行翻译模式]\n    -c 命令行翻译模式\n    -l 行翻译模式\n    -h 显示帮助')
else:
    text = ' '.join(data)
    translate(text)
