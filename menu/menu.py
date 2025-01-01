#!menu/bin/python3
import json
import glob
from cursesmenu import CursesMenu
from cursesmenu.items import CommandItem
import socket


hostname = socket.gethostname()
ip_addr = socket.gethostbyname(hostname)

dosbox_path="dosbox-x"
game_glob_path="./*/*.json"

m_items =  [ ]
m_conf = { }

for filename in glob.glob(game_glob_path):
    with open(filename, "r") as file:
        content = file.read()
    item = json.loads(content)
    m_items.append(item['title'])
    m_conf[item['title']] = item['conf']

m_items.sort()

menu = CursesMenu("Computer: " + hostname + " (" + ip_addr + ")")
for item in m_items:
    menu.items.append(CommandItem(item, "set -x;" + dosbox_path + " -conf " + m_conf[item] + " ; sleep 2"))
menu.start()
_ = menu.join()
