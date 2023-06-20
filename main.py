import a2s
import requests
import xml.etree.ElementTree as ET

steamid = input("SteamID64: ")

request = requests.get("https://steamcommunity.com/profiles/" + str(steamid) + "/?xml=1")
root = ET.fromstring(request.content)
onlineState = root.find("onlineState")
stateMessage = root.find("stateMessage")
if onlineState is not None:
    print(stateMessage.text.replace("<br/>","|"))
    if onlineState.text == "in-game":
        server = root.find('inGameServerIP')
        if server is not None and server.text is not None:
            print("connected to "+server.text+", getting info...")
            sinfo = server.text.split(":",2)
            ip = sinfo[0]
            port = int(sinfo[1])
            try:
                info1 = a2s.info((ip, port))
            except:
                print("Failed, no server info available.")
            else:
                print(info1)
                input(str((info1.stv_port or "No STV Port")) + ", " + (info1.stv_name or "No STV Name"))
        else:
            print("No server/Not connected")