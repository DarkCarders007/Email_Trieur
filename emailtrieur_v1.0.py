

# -*- coding: utf-8 -*-
#! /usr/bin/python3

import sys, os, time, re
import glob
import hashlib
import pyfiglet
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format
from clint.textui import colored
setcomboclean =[]
setproxiesclean =[]
setmd5clean =[]
regexmd5 = (r"([a-fA-F\d]{32})")


def banniere() :
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')
    text="DarkCarders007"
    cprint(figlet_format(text, font="standard"), "green")
    print('https://t.me/DarkCarders007')
    print(colored.blue("DarkTools : Email_Trieur"))
    print(colored.red("-- Version 1.0 --"))
    print(colored.yellow("Realease: 02/09/2021"))
    print(colored.magenta("Email Trieur Décrypteur By DarkCarders007 "))


def menubase():
    print(colored.yellow("\n"+"- Trier Des Combo/Proxies -"))
    print(colored.yellow("   - Décrypter Des MD5 -"))
    print(colored.yellow("       - Extraire - "+"\n"))
    print(colored.green("Placer Le(s) Fichier(s) .txt Dans Le Dossier Correspondant."))
    print(colored.green("Max 3 Séparateurs (:)."))
    print(colored.green("Example: Email:Pass:Dob, Email:Pass, User:Pass, Email:MD5, Email."))
    while True:
        print(colored.red("!! Trie Tous Le(s) Fichier(s) .txt Dans Le Dossier Correspondant !!"+"\n"))
        print(" 1. /ComboACheck/**.txt"+colored.blue("    Trie: Email:Pass, Email:Pass:Dob, User, etc..."))
        print(" 2. /ProxiesACheck/**.txt"+colored.yellow("  Trie Format: IP:Port"))
        print(" 3. /ComboACheck/**.txt"+colored.cyan("    Extraire: .edu Format : email:pass, email."))
        print(" 4. /ComboACheck/**.txt"+colored.green("    Décrypter: MD5."))
        print(" 5. Trier Résultats Du Email Access Cracker.")
        print(" 0. Quit ")
        try:
            choixfonctrie = int(input(colored.green("\n"+" Fait Ton Choix : ")))
            if choixfonctrie == 0:
                print(colored.magenta("\n"+"Merci D'Avoir Utilisé Le Tools !"))
                exit()
            if choixfonctrie == 1:
                loadtype = "Combo"
                extraire = "non"
                choixquoiextraire = ""
                TrieCombo(loadtype, extraire,choixquoiextraire)
                if os.name=='nt':
                    chemintools = os.getcwd()
                    chemintools2 = ("\Resultats")
                    chemintoolstotal = (chemintools +chemintools2)
                    os.popen(r"explorer " + chemintoolstotal)
                    os.popen("notepad " + r"Resultats\Combotrier.txt")
                else:
                    os.popen("thunar" + r" Resultats &")
                    os.popen("mousepad" +  r" Resultats/Combotrier.txt &")

            if choixfonctrie == 2:
                loadtype = "Proxies"
                extraire = "non"
                choixquoiextraire = ""
                TrieCombo(loadtype, extraire, choixquoiextraire)
                if os.name=='nt':
                    os.popen("notepad " + r"Resultats\Proxiestrier.txt")
                else:
                    os.popen("mousepad" +  r" Resultats/Proxiestrier.txt")
            if choixfonctrie == 3:
                try :
                    print("\n"+"Extraire Tous Les Emails De Tous Les Fichiers .txt Dans Le Dossier /00Combo/ ")
                    print("Pour Etraire Les .edu, Taper '.edu'.")
                    print("Pour Etraire Les sfr.fr Taper 'sfr.fr'.")
                    print("Pour Plusieurs, Taper '.edu,sfr.fr,etc...'.")
                    choixExtraire =  input(colored.green("\n"+"Extraire Quoi ?"))
                    loadtype = "Combo"
                    extraire = "oui"
                    choixquoiextraire = choixExtraire
                    TrieCombo(loadtype, extraire, choixquoiextraire)
                    if os.name=='nt':   # Windob
                        os.popen("notepad " + r"Resultats\Edutrier.txt")
                    else:
                        os.popen("mousepad" +  r" Resultats/Edutrier.txt")
                except ValueError :
                    print(colored.red("Je Ne Vois Ce Tools Nulle Part !?  "+"\n"))

            if choixfonctrie == 4:
                print("\n"+"Décrypter MD5 De Tous Les Fichiers .txt Dans Le Dossier /00Combo/ ")
                loadtype = "Combo"
                extraire = "non"
                choixquoiextraire = ""
                TrieCombo(loadtype, extraire,choixquoiextraire)
                decryptmd5()
                if os.name=='nt':
                    os.popen("notepad " + r"Resultats\Md5decryptertrier.txt")
                else:   # Linux
                    os.popen("mousepad" +  r" Resultats/Md5decryptertrier.txt")

            if choixfonctrie == 5:
                triemailbox()
                os.popen("notepad " + r"Resultats\MailBoxOkTrier.txt")

        except ValueError:
            print(colored.red("Je Ne Vois Cette Option Nulle Part ?!"))


def TrieCombo(loadtype, extraire, choixquoiextraire):
    ligneaextraires = choixquoiextraire.split(",")
    if loadtype == "Combo":
        setcomboclean =[]
        files = sorted(glob.glob('./ComboACheck/*'))
        for file in files:
            print(colored.green("Fichier Trouvé: "+colored.blue(file)))
            with open(file, 'r',errors='ignore') as inf:
                lines = inf.readlines()
                for line in lines :
                    lignepropre = line.strip()
                    setcomboclean.append(lignepropre)
        #print(setcomboclean)
        nbcombo = len(setcomboclean)
        print(colored.green("Total Combos Trouvé: ")+str(nbcombo))
        try:
            dobtrier = open("Resultats/DOBtrier.txt", "w+", encoding='utf-8', errors='ignore')
            combotrier = open("Resultats/Combotrier.txt", "w+", encoding='utf-8', errors='ignore')
            combousertrier = open("Resultats/ComboUsertrier.txt", "w+", encoding='utf-8', errors='ignore')
            emailtrier = open("Resultats/Emailtrier.txt", "w+", encoding='utf-8', errors='ignore')
            userpasstrier = open("Resultats/Userpasstrier.txt", "w+", encoding='utf-8', errors='ignore')
            edutrier = open("Resultats/Edutrier.txt", "w+", encoding='utf-8', errors='ignore')
            md5crypttrier = open("Resultats/Md5trier.txt", "w+", encoding='utf-8', errors='ignore')
            usertrier = open("Resultats/Usertrier.txt", "w+", encoding='utf-8', errors='ignore')
            HashMd5 = open("Decrypt/PassMd5trier.txt", "a+", encoding='utf-8', errors='ignore')
        except FileNotFoundError:
                print("fichier non trouvés, creation...")
                os.mkdir("Resultats/")
                os.mkdir("Decrypt/")
                dobtrier = open("Resultats/DOBtrier.txt", "w+", encoding='utf-8', errors='ignore')
                combotrier = open("Resultats/Combotrier.txt", "w+", encoding='utf-8', errors='ignore')
                combousertrier = open("Resultats/ComboUsertrier.txt", "w+", encoding='utf-8', errors='ignore')
                emailtrier = open("Resultats/Emailtrier.txt", "w+", encoding='utf-8', errors='ignore')
                userpasstrier = open("Resultats/Userpasstrier.txt", "w+", encoding='utf-8', errors='ignore')
                edutrier = open("Resultats/Edutrier.txt", "w+", encoding='utf-8', errors='ignore')
                md5crypttrier = open("Resultats/Md5trier.txt", "w+", encoding='utf-8', errors='ignore')
                usertrier = open("Resultats/Usertrier.txt", "w+", encoding='utf-8', errors='ignore')
                HashMd5 = open("Decrypt/PassMd5trier.txt", "a+", encoding='utf-8', errors='ignore')
        resultantList = []
        setdicomd5 = []
        for element in sorted(setcomboclean):
            if element not in resultantList:
                resultantList.append(element)
        for combo in sorted(resultantList) :
            md5crypt = re.findall(r"([a-fA-F\d]{32})", combo)
            try :
                if md5crypt :
                    md5crypttrier.write(combo+"\n")
                else :
                    mallo, passo, dob = combo.split(":",3)
                    dobtrier.write(combo+"\n")
                    hashmd5 = hashlib.md5(passo.encode('utf8')).hexdigest()
                    HashMd5.write(passo+":"+hashmd5+"\n")
                if extraire == "oui":
                    for ligneaextraire in ligneaextraires :
                        if ligneaextraire in combo :
                            edutrier.write(combo+"\n")
            except ValueError :
                try :
                    mallo, passo = combo.split(":",2)
                    if "@" in combo:
                        if not "�" in combo :
                            if not "!~!" in combo  :
                                combotrier.write(combo+"\n")
                                hashmd5 = hashlib.md5(passo.encode('utf8')).hexdigest()
                                HashMd5.write(passo+":"+hashmd5+"\n")
                    if "@" not in combo:
                        userpasstrier.write(combo+"\n")
                        hashmd5 = hashlib.md5(passo.encode('utf8')).hexdigest()
                        HashMd5.write(passo+":"+hashmd5+"\n")

                    if extraire == "oui":
                        for ligneaextraire in ligneaextraires :
                            if ligneaextraire in combo :
                                edutrier.write(combo+"\n")

                except ValueError :
                    try :   ## Si Email
                        if "@" in combo:
                            if not "�" in combo :
                                if not "!~!" in combo  :
                                    emailtrier.write(combo+"\n")

                        if "@" not in combo:
                            usertrier.write(combo+"\n")

                        if extraire == "oui":
                            for ligneaextraire in ligneaextraires :
                                if ligneaextraire in combo :
                                    edutrier.write(combo+"\n")
                    except ValueError :
                        print('hs')

        dobtrier.close()
        combotrier.close()
        combousertrier.close()
        emailtrier.close()
        userpasstrier.close()
        edutrier.close()
        md5crypttrier.close()
        usertrier.close()
        HashMd5.close()


    if loadtype == "Proxies":
        setproxiesclean =[]
        files = sorted(glob.glob('./ProxiesACheck/*'))
        for file in files:
            print(colored.green("Fichier Trouvé : "+colored.blue(file)))
            with open(file, 'r',errors='ignore') as inf:
                lines = inf.readlines()
                for line in lines :
                    lignepropre = line.strip()
                    setproxiesclean.append(lignepropre)
        nbproxies = len(setproxiesclean)
        proxiestrier = open("Resultats/Proxiestrier.txt", "w+", encoding='utf-8', errors='ignore')
        for proxies in sorted(setproxiesclean) :
            foundip = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):[0-9]+',proxies)
            if foundip :
                proxiestrier.write(proxies+"\n")
        proxiestrier.close()
        print(colored.green("Trie De Proxies Terminé !!"+"\n"))
        print(colored.green("Total Proxies Trouvé : ")+str(nbproxies))

    if loadtype == "Combo":
        if extraire == "oui":
            print("Tous Les Email Ont Etaient Extrait !")
            print(colored.green("Trie De Combo Terminé !!"+"\n"))


def triemailbox():
    capturecheque ="imap."
    obj_fichier = open("Resultats/MailBoxOk.txt", 'r', encoding='utf-8', errors='ignore')
    mailboxtrier = open("Resultats/MailBoxOkTrier.txt", "w+", encoding='utf-8', errors='ignore')
    for ligneobj_fichier in set(obj_fichier):
        if  capturecheque in ligneobj_fichier :
            ligneobj_fichierclean = ligneobj_fichier.strip()
            map, login =ligneobj_fichierclean.split(" : ",2)
            loginclean = login.strip()
            mailboxtrier.write(loginclean+"\n")
    obj_fichier.close()
    mailboxtrier.close()
    print(colored.green("Trie De MailboxOk Terminé !!"+"\n"))


def decryptmd5():
    md5trier = open("Resultats/Md5trier.txt", "r", encoding='utf-8', errors='ignore')
    dbmd5 = open("Decrypt/PassMd5trier.txt", "r", encoding='utf-8', errors='ignore')
    setallmd5 = sorted(dbmd5)
    md5decrypter = open("Resultats/Md5decryptertrier.txt", "w+", encoding='utf-8', errors='ignore')
    for lignemd5 in sorted(md5trier):
        try :
            mallo, passo, dob = lignemd5.split(":",3)
            if re.findall(r"([a-fA-F\d]{32})", mallo):
                totalclean = passo+mallo+dob
                print(totalclean)
                setmd5clean.append(totalclean)
                print("md5 trouvé dans le mail :3")
            if re.findall(r"([a-fA-F\d]{32})", dob):
                totalclean = str(mallo+dob+passo)
                setmd5clean.append(totalclean)
                print("md5 trouvé dans le dob :3")
            else :
                print(passo)
                for lignemd50 in setallmd5:
                    if passo in lignemd50:
                        cleanmd5 = lignemd5.strip("\n")
                        totaldecrypt = cleanmd5+" Decrypter = " +lignemd50
                        md5decrypter.write(totaldecrypt+"\n")
                setmd5clean.append(lignemd5)
        except ValueError :
            try :
                mallo, passo = lignemd5.split(":",2)
                if re.findall(r"([a-fA-F\d]{32})", mallo):
                    print("md5 trouvé dans le mail :2")
                    totalclean = passo+mallo
                    setmd5clean.append(totalclean)
                else :
                    setmd5clean.append(lignemd5)
            except ValueError :
                print("")
    md5decrypter.close()
    print("MD5 Decrypt Terminé ")


banniere()
menubase()


