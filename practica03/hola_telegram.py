#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-

#Jorge Luzón López
#jluzon

import telepot
import telepot.namedtuple
import time
from telepot.loop import MessageLoop

#def readkey():

file = open("key","r")
TOKEN = file.readline()
bot = telepot.Bot(TOKEN)
file.close()

def handle(msg):
  chat_id = msg["chat"]["id"]
  texto = msg["text"]

  print msg["from"]["first_name"] + ": " + msg["text"]

  respuesta = "Me has dicho " + texto
  bot.sendMessage(chat_id,respuesta)
  return

def main():
  id_usuario = "778702261"
  bot.sendMessage(id_usuario,"Hola")

  MessageLoop(bot, handle).run_as_thread()
  while 1:
    time.sleep(1)
  return

if __name__ == "__main__":
  main()
