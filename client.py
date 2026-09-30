import requests

def encode(chaine):
    nb = ""
    for c in chaine:
        val = str(ord(c))
        nb += (3-len(val))*"0"+val
    return nb

print("\033[1;37mWelcome to U_Search !\n")
print("Tapez \033[1;34mhelp\033[1;37m pour consulter la documentation")
cmd = ""
name_serv = None

'''
Liste Commandes
help 
connect
disconnect
goto
quit
'''

while cmd != "quit":
    cmd = input("\033[1;37m>>\033[1;34m ")
    print("\033[1;37m", end="")
    if cmd == "connect":
        if name_serv == None:
            name_serv = input("\033[1;37mEntrez l'URL de votre serveur : ")
            print("\033[1;37mVérification...")
            reponse = requests.get(name_serv)
            if reponse.status_code == 200 :
                if reponse.text == "[\"Welcome to U_Web !\"]":
                    print("\033[1;32mURL correcte ! Bon voyage !\033[1;37m")
                else :
                    print("\033[1;31mSomething went wrong... Veuillez recommencer\n/!\\ Il est nécessaire d'inclure https:// ou http://\033[1;37m")
                    name_serv = None
        else :
            print("\033[1;37mVous êtes déjà connecté. Tapez disconnect pour vous déconnecter")
    elif cmd == "disconnect":
        name_serv = None
        print("\033[1;32mVous avez été déconnecté avec succés\033[1;37m")
    elif cmd == "goto":
        if name_serv == None:
            print("\033[1;31mVous n'êtes pas connecté. Tapez \033[1;34mconnect\033[1;37m pour vous connecter")
        else :
            address = input("\033[1;37mOù souhaitez vous aller ? ")
            print("\033[1;37mEncodage...")
            address = encode(address)
            print("\033[1;32mURL encodé avec succés")
            print(f"\033[1;37mContinuez votre voyage ici : {name_serv}/get/{address}")
    elif cmd == "quit":
        print("\033[1;37mMerci d'avoir utilisé U_Web ! Bonne journée !")
    elif cmd == "help":
        print("\033[1;37mListes des commandes d'U_Search : ")
        print("\033[1;34mconnect : \033[1;37mpermet de renseigner le serveur à utiliser (/!\\ Il est nécessaire d'inclure https:// ou http:// dans l'URL)")
        print("\033[1;34mdisconnect : \033[1;37mpremet de de retirer le serveur actuel")
        print("\033[1;34mgoto : \033[1;37mpermet d'obtenir l'URL d'un lien (/!\\ Il est nécessaire d'inclure https:// ou http:// dans l'URL)")
        print("\033[1;34mquit : \033[1;37mquitte U_Search")
        print()
    else :
        print("\033[1;31mCommande non reconnue ! Tapez help pour consulter la liste des commandes\033[1;37m")