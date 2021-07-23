# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
#banco
import pymysql
cusrorType= pymysql.cursors.DictCursor
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='jarvis',cursorclass=cusrorType)
cur = conn.cursor()
           
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)

bot = ChatBot('Test')

convI = ['oi', 'olá', 'olá, bom dia', 'bom dia', 'como vai', 'estou bem','legal','joia','nada','nada?','sim','Tá','ok','então é isso','entendeu','entendi sim','filme','gosto daquele filme que os robôs se viram contra a humanidade']
convF = ['qual tipo de música você gosta','eu gosto de música clássica','fale comigo','sim claro','responde','seja paciente estou aprendendo','diga alguma coisa','alguma coisa!','qual o seu nome','meu nome é robô voice','seu nome','robô voice']
convA = ['não','não o que?','certo','então tá','você é chato','igual quem me criou!','cala a boca','o autofalante?','você é um robô','sou apenas um programa','robô','sim humano','google','meu primo','piada','não sei nenhuma']
bot.set_trainer(ListTrainer)

bot.train(convI)
bot.train(convF)
bot.train(convA)
print('=======================================')
with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)
    while True:
        audio = r.listen(s)
        quest = r.recognize_google(audio, language='pt')
        #quest = input()
        print('Voce:', r.recognize_google(audio, language='pt'))
        response = bot.get_response(quest)
        if float(response.confidence) > 0.5:
            print('Bot:', response)
        else:
            try:
                # Cursor object creation
                cursorObject    = conn.cursor()
                #deixar primeira letra maiuscula
                quest = quest.lower().capitalize()
                cursorObject.execute('call consulta("'+quest+'")')                      
                            # Print the result of the executed stored procedure
                for result in cursorObject.fetchall():
                    print(result)
            except Exception as e:
                print("Exeception occured:{}".format(e))        
            finally:
                    conn.close()

                                    
                                    

                                    

