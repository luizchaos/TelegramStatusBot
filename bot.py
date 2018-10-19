import telepot
import urllib
import sys

with open("token.tok", "r") as t:
    token = t.read()
    if token is None or token == "":
        with open("token.tok", "w") as o:
            o.write
            sys.exit("Token Invalido! Adicione um token ao arquivo token.tok")

with open("chat_id.txt", "r") as t:
    token = t.read()
    if token is None or token == "":
        with open("chat_id.txt", "w") as o:
            o.write
            sys.exit("Arquivo chat id criado, execute novamente")

with open("update_id.txt", "r") as t:
    token = t.read()
    if token is None or token == "":
        with open("update_id.txt", "w") as o:
            o.write
            sys.exit("Arquivo update id criado, execute novamente")



TelegramBot = telepot.Bot(token)

with open("update_id.txt", "r") as f:
    ult_updt = f.read()
    if ult_updt is None or ult_updt == "":
        ult_updt = 0
        updates = TelegramBot.getUpdates()
    else:
        updates = TelegramBot.getUpdates(int(ult_updt)+1)

# print updates.get['message']

for upd in updates:
    # chat_id = updt['message']['chat_id']
    chat_id = upd.get("message").get("chat").get("id")
    message = upd.get("message").get("text")
    update_id = upd.get("update_id")
    print update_id
    if message == "/start":
        with open("chat_id.txt","r") as f:
            linhas = f.readlines()
            encontrado = False
            for i in linhas:
                if i.replace("\n","") == str(chat_id):
                    encontrado = True
            
            if not encontrado:
                with open("chat_id.txt","a") as i:
                    i.write(str(chat_id)+"\n")
                    TelegramBot.sendMessage(chat_id, "Bem vindo ao Bot de Alertas!", parse_mode='HTML')
    elif message == "/help":
        TelegramBot.sendMessage(chat_id, "Qualquer duvida enviar um email a <strong>luizchaos@gmail.com!</strong>", parse_mode='HTML')
    
    with open("update_id.txt", "w") as l:
        l.write(str(update_id))
            
    

# with open("ajuda.html","r") as f:
#     teste =  f.read()


with open("sites.txt", "r") as e:
    linhas = e.readlines()
    for l in linhas:
        site = l.replace("\n","")
        codigo_site = urllib.urlopen(site).getcode()
        print site," // ",codigo_site

        with open("chat_id.txt","r") as s:
            lin = s.readlines()
            if codigo_site != 200:
                for i in lin:     
                    html =  '''Ola tudo bom?

O Site <strong>'''+str(site)+'''</strong> esta com erro e retornando codigo: <strong>'''+str(codigo_site)+'''</strong>
                            '''           
                    TelegramBot.sendMessage(int(i), html, parse_mode='HTML')


# TelegramBot.sendMessage(chat_id, teste, parse_mode='HTML')