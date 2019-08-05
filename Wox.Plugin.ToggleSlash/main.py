# -*- coding: utf-8 -*-
# Toggle \ And /
from wox import Wox
import pyperclip

class ToggleSlash(Wox):

    def query(self, query):
        query = (query)
        if not query:
            return []
        strList = list(query)
        for x in range(len(strList)):
            if strList[x] == "\\":
                strList[x] = "/"
            elif strList[x] == "/" :
                strList[x] = "\\"

        resStr = "".join(strList)
        resStr = self.convert(resStr)
        return [{
                "Title": "Toggle \\ and /",
                "SubTitle": "Result: {}".format(resStr),
                "IcoPath":"Images/app.ico",
                "ContextData": "ctxData",
                "JsonRPCAction": {
                    "method": "copyText",
                    "parameters": [resStr]
                }
            }]
    def convert(self, s):
        return str(s).replace('//', '/').replace("\\\\", '\\')

    def copyText(self, word):
        word = self.convert(word)
        pyperclip.copy(word)
        # self.debug(word)

if __name__ == "__main__":
    ToggleSlash()