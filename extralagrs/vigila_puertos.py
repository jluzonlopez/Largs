#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

# Examen LAGRS, diciembre 2018
# NOMBRE: Jorge Luzon Lopez
# LOGIN: jluzon

import telepot
import telepot.namedtuple
import time
import subprocess,sys
import os
from telepot.loop import MessageLoop
from optparse import OptionParser

PUERTOS_TCP = [6666 , 443 , 7899]

def readkey():
  try:
    file = open("token.txt","r")
    key = file.readline()
    file.close()
    return key
  except IOError:
    sys.stderr.write("Could not read key\n")
    raise SystemExit

def iduser():
  try:
    file = open("id_usuario.txt","r")
    key = file.readline()
    file.close()
    return key
  except IOError:
    sys.stderr.write("Could not read key\n")
    raise SystemExit

TOKEN = readkey()
ID_USUARIO = iduser()
bot = telepot.Bot(TOKEN)

def checkpuerto(port):
  for p in PUERTOS_TCP:
    if int(p) == int(port):
      return True

def checkline(lines):
  r=""
  for l in lines:
    fields=l.split()
    if checkpuerto(fields[3].split(":")[-1]):
      r+=fields[3].split(":")[-1] + " " + fields[5] + "\n"
  return r

def donetstat():
  cmd = "netstat -tupan"
  try:
    out=subprocess.check_output(cmd.split())
    out=out.split("\n")
    out.pop(0)
    out.pop(0)
    out.pop()
    r=checkline(out)
    return r
  except:
    sys.stderr.write("CMD failed\n")
    raise SystemExit


def handle():
  respuesta = donetstat()
  if len(respuesta) > 0:
    respuesta += "Ports USED\n" 
    bot.sendMessage(ID_USUARIO,respuesta)
  return 

def main():

  handle()

if __name__ == '__main__':
  main()
