#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author: Eitenne

import os
import urllib, urllib2
import sys
import time
import socket
import whois

os.system('clear')

subdomains = ["ftp", "cpanel", "webmail", "forum", "driect-connect", "vb", "forums", "home", "direct", "mail", "access", "admin", "administrator", "email", "downloads", "ssh", "webmin", "paralel", "parallels", "www0", "www", "www1", "www2", "www3", "www4", "www5"]

def banner():
    print """
         _ _,---._ 
       ,-','       `-.___ 
      /-;'               `._ 
     /\/          ._   _,'o \ 
    ( /\       _,--'\,','"`. ) 
     |\      ,'o     \'    //\ 
     |      \        /   ,--'""`-. 
     :       \_    _/ ,-'         `-._ 
      \        `--'  /                ) 
       `.  \`._    ,'     ________,',' 
         .--`     ,'  ,--` __\___,;' 
          \`.,-- ,' ,`_)--'  /`.,' 
           \( ;  | | )      (`-/ 
             `--'| |)       |-/ 
               | | |        | | 
               | | |,.,-.   | |_ 
               | `./ /   )---`  ) 
              _|  /    ,',   ,-' 
             ,'|_(    /-<._,' |--, 
             |    `--'---.     \/ \ 
             |          / \    /\  \ 
           ,-^---._     |  \  /  \  \ 
        ,-'        \----'   \/    \--`. 
       /            \              \   \ 

"""

def main():
 if len(sys.argv) == 2:
    url = sys.argv[1]
    print "[!] Getting whois"
    lol = whois.whois(url)
    print "[!] Getting reverse dns"
    reversed_dns = urllib.urlopen('http://api.hackertarget.com/reverseiplookup/?q=' + url).read()
    print "[!] Getting geoip"
    geoip = urllib.urlopen('http://api.hackertarget.com/geoip/?q=' + url).read()
    print "[!] Scanning ports"
    nmap = urllib.urlopen('http://api.hackertarget.com/nmap/?q=' + url).read()
    print "[!] Getting httpheaders"
    httpheaders = urllib.urlopen('http://api.hackertarget.com/httpheaders/?q=' + url).read()
    print "[!] Getting tracert"
    tracert = urllib.urlopen('http://api.hackertarget.com/mtr/?q=' + url).read()
    print "[*] Whois Information:"
    print lol
    print "[*] Reverse dns information:"
    print reversed_dns
    print "[*] Geoip information:"
    print geoip
    print "[*] Port scan information:"
    print nmap
    print "[*] httpheader information:"
    print httpheaders
    print "[*] tracert information:"
    print tracert
    time.sleep(0.7)
    print "[*] Starting cloudflare resolver"
    time.sleep(2)
 else:
    print """
   ╭─────────────────────────────────────╮
   │ Usage: python garth.py <url/ip>     │
   ╰─────────────────────────────────────╯"""

def cf():
    link = sys.argv[1]
    for sbdm in subdomains:
      try:
         hosts = str(sbdm) + "." + str(link)
         trueip = socket.gethostbyname(str(hosts))
         print "[!] Discovered >> " + str(trueip)
      except:
             pass

banner()
main()
cf()
