#importation des modules
from pynput.mouse import Button, Controller
import os
import time
#la souris = à un controlleur
mouse = Controller()

#on ouvre le menu de windows

mouse.position = (0, 1080)
mouse.press(Button.left)
mouse.release(Button.left)

#importation des modules
from pynput.keyboard import Key, Controller
#execution de l'executeur
time.sleep(2)
keyboard = Controller()
keyboard.type('run')
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(1)
#on écris "%temp%"
keyboard.type('%temp%')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(1)
#on selectionne tout
keyboard.press(Key.ctrl)
keyboard.press('a')
keyboard.release(Key.ctrl)
keyboard.release('a')
#on supprime tout
time.sleep(1)
keyboard.press(Key.delete)
keyboard.release(Key.delete)

#importation des modules
time.sleep(2)
from pynput.mouse import Button, Controller
#fermer la fenêtre qui dis que certains fichier sont actuellement ouvert
mouse.position = (1155, 263)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(2)
#fermer le dossier
mouse.position = (1694, 207)
mouse.press(Button.left)
mouse.release(Button.left)

#on ouvre le menu de windows
from pynput.mouse import Button, Controller
time.sleep(5)
mouse.position = (0, 1080)
mouse.press(Button.left)
mouse.release(Button.left)
#execution de l'executeur
time.sleep(2)
from pynput.keyboard import Key, Controller
keyboard.type('run')
time.sleep(4)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(2)
keyboard.type('temp')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(1)
#on selectionne tout
keyboard.press(Key.ctrl)
keyboard.press('a')
keyboard.release(Key.ctrl)
keyboard.release('a')
#on supprime tout
keyboard.press(Key.delete)
keyboard.release(Key.delete)
#fermer la fenêtre qui dis que certains fichier sont actuellement ouvert
time.sleep(2)
mouse.position = (1155, 263)
mouse.press(Button.left)
mouse.release(Button.left)
#fermer le dossier
time.sleep(2)
mouse.position = (1694, 207)
mouse.press(Button.left)
mouse.release(Button.left)