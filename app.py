from flask import Flask
import translators as ts
import json
from flask import render_template
from flask import request

app = Flask(__name__) #creating the Flask class object   

@app.route('/') #decorator drfines the   
def home():
    return "Hello, world!"

@app.route('/translator/') #decorator drfines the   
def translator():  
    try:
        wyw_text = request.args.get('q')
        translator = request.args.get('translator')
        output = "017551c71e8b2869f85a2fa2c560dcc3"
        if translator == "deepl":
            output = ts.deepl(wyw_text, from_language='auto',to_language='en')
        elif translator == "bing":
            output = ts.bing(wyw_text, from_language='zh',to_language='en')
        elif translator == "google":
            output = ts.google(wyw_text, from_language='zh',to_language='en')
        # elif translator == "sogou":
        #     output = ts.sogou(wyw_text, from_language='zh',to_language='en')
        elif translator == "iciba":
            output = ts.iciba(wyw_text)
        elif translator == "lingvanex":
            output = ts.lingvanex(wyw_text, from_language='zh',to_language='en')
        elif translator == "reverso":
            output = ts.reverso(wyw_text)
        elif translator == "itranslate":
            output = ts.itranslate(wyw_text)
        elif translator == "baidu":
            output = ts.baidu(wyw_text)
        elif translator == "caiyun":
            output = ts.caiyun(wyw_text)
        elif translator == "tencent":
            output = ts.tencent(wyw_text)
        elif translator == "argos":
            output = ts.argos(wyw_text, from_language='zh',to_language='en')
        elif translator == "translateCom":
            output = ts.translateCom(wyw_text, from_language='zh',to_language='en')
        return output
    except:
        return "017551c71e8b2869f85a2fa2c560dcc3"


if __name__ =='__main__':
    app.run(host="0.0.0.0")
