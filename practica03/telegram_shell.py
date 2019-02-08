#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-

#Jorge Luzón López
#jluzon

import telepot
import telepot.namedtuple
import time
import subprocess,sys
from telepot.loop import MessageLoop

def readkey():
  try:
    file = open("token.txt","r")
    key = file.readline()
    file.close()
    return key
  except IOError:
    sys.stderr.write("Could not read key\n")
    raise SystemExit

TOKEN = readkey()
bot = telepot.Bot(TOKEN)

def docmd(cmd):
  cmd=cmd[:1].lower()+cmd[1:]
  try:
    comd = cmd.split()
    out=subprocess.check_output(comd)
    return out
  except subprocess.CalledProcessError:
    sys.stderr.write("CDM failed\n")
    raise SystemExit


def handle(msg):
  chat_id = msg["chat"]["id"]
  texto = msg["text"]

  print msg["from"]["first_name"] + ": " + msg["text"] 

  respuesta = docmd(texto)
  bot.sendMessage(chat_id,respuesta)
  return

def main():
  id_usuario = "778702261"
  bot.sendMessage(id_usuario,"Welcome to TelegramShell")

  MessageLoop(bot, handle).run_as_thread()
  while 1:
    time.sleep(1)
  return

if __name__ == "__main__":
  main()
