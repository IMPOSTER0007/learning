#coding=utf-8
#!/usr/bin/python2
#This Script Write By Tech Baba
#Do Not Copy This Script :)
try:
    import os
    import sys
    import time
    import urllib
    import platform
    import requests
except ImportError:
    os.system('pip2 install requests') #Module Not found Eror :(

#Loding Funcation :)
def baba(word):
    lix = ["[\033[1;92m■\033[1;97m□□□□□□□□□□□□□]","[\033[1;93m■■\033[1;97m□□□□□□□□□□□□]", "[\033[1;94m■■■\033[1;97m□□□□□□□□□□□]", "[\033[1;96m■■■■\033[1;97m□□□□□□□□□□]", "[\033[1;95m■■■■■\033[1;97m□□□□□□□□□]", "[\033[1;97m■■■■■■\033[1;97m□□□□□□□□]", "[\033[1;93m■■■■■■■\033[1;97m□□□□□□□]", "[\033[1;91m■■■■■■■■\033[1;97m□□□□□□]", "[\033[1;96m■■■■■■■■■\033[1;97m□□□□□]", "[\033[1;92m■■■■■■■■■■\033[1;97m□□□□]", "[\033[1;94m■■■■■■■■■■■\033[1;97m□□□]", "[\033[1;95m■■■■■■■■■■■■\033[1;97m□□]", "[\033[1;93m■■■■■■■■■■■■■\033[1;97m□]", "[\033[1;92m■■■■■■■■■■■■■■\033[1;97m]"]
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.09)
            sys.stdout.flush()

logo = """
\033[1;93m┈███▄┈▄███▓┈▄▄▄┈┈┈┈┈┈┈██▀███┈┈┈███▄┈▄███▓┈█┈┈┈┈██┈ 　 
\033[1;93m▓██▒▀█▀┈██▒▒████▄┈┈┈┈▓██┈▒┈██▒▓██▒▀█▀┈██▒┈██┈┈▓██▒ 　 
\033[1;92m▓██┈┈┈┈▓██░▒██┈┈▀█▄┈┈▓██┈░▄█┈▒▓██┈┈┈┈▓██░▓██┈┈▒██░
\033[1;92m▒██┈┈┈┈▒██┈░██▄▄▄▄██┈▒██▀▀█▄┈┈▒██┈┈┈┈▒██┈▓▓█┈┈░██░
\033[1;92m▒██▒┈┈┈░██▒┈▓█┈┈┈▓██▒░██▓┈▒██▒▒██▒┈┈┈░██▒▒▒█████▓┈
\033[1;91m░┈▒░┈┈┈░┈┈░┈▒▒┈┈┈▓▒█░░┈▒▓┈░▒▓░░┈▒░┈┈┈░┈┈░░▒▓▒┈▒┈▒┈
\033[1;91m░┈┈░┈┈┈┈┈┈░┈┈▒┈┈┈▒▒┈░┈┈░▒┈░┈▒░░┈┈░┈┈┈┈┈┈░░░▒░┈░┈░┈
\033[1;91m
\033[1;95m ================================================================      
\033[1;97m ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ B4BY-DR4G0N ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
\033[1;95m===================================================================      
\033[1;96mCreation : M4RMU
                 
\033[1;94mGithub.  : B4BY DR4GON
                     
\033[1;95mTermux   : KO HTeT
                     
\033[1;92mFacebook : TECHNOLOGY BY M4RMU

-----------------------------------------------"""

def home(): #main menu
    os.system("clear")
    arm = platform.architecture()[0] #Checking arm
    print logo #raw
    print 47*("-")
    print('Your Device Is \033[0;92m'+arm).center(45)  #Show Raw
    print 47*("\033[0;97m-")
    baba("   Bypass Processing => ")
    os.system("clear")
    print logo
    device = platform.architecture()[0]
    if device == '64bit':
        from libtm import main
        main()
    elif device == '32bit':
        os.system("clear")
        os.system("exit")
        os.system("cd $HOME") #Home 
        os.system("cat /data/data/com.termux/files/usr/etc/motd") # Show Termux Info Text 
        print("$ Your Device Has Been No Support :( ")
    else:
        os.system("clear")
        os.system("cat /data/data/com.termux/files/usr/etc/motd") # Show Termux Info Text 
        os.system("exit")

if __name__ == '__main__':
    home()
