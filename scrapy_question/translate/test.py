__author__ = 'xue'
from py4js import Py4Js
from translate import open_url,translate1

def main():
    js = Py4Js()

    while 1:
        content = input("输入待翻译内容：")

        if content == 'q!':
            break

        tk = js.getTk(content)
        translate1(content)

if __name__ == "__main__":
    main()