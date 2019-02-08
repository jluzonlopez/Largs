#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

#Jorge Luzón López
#jluzon

import telepot
import telepot.namedtuple
import time
import subprocess,sys
import os
from telepot.loop import MessageLoop
from optparse import OptionParser

DIRECTORIOS = ["~/lagrs/caa", "~/lagrs/cab"]
MAX_TAMANIO = 1  
MAX_FICHEROS = 5
ID_USUARIO = 778702261

def readkey():
  try:
    file = open("/home/alumnos/jluzon/lagrs/practica03/token.txt","r")
    key = file.readline()
    file.close()
    return key
  except IOError:
    sys.stderr.write("Could not read key\n")
    raise SystemExit

TOKEN = readkey()
bot = telepot.Bot(TOKEN)

usage = "%prog [-f --force-telegram]"
parser = OptionParser(usage)
parser.add_option("-f","--force-telegram",
action="store_true",dest="force",
help="Force to send message")

options,args = parser.parse_args()


def replacedi():
  dirs = []
  for d in DIRECTORIOS:
    if "~" in d:
      d = d.replace("~",os.path.expanduser("~"))
      dirs.append(d)

  return dirs


def listdir(d):
  cmd = "ls -lh "+d
  try:
    out=subprocess.check_output(cmd.split())
    out=out.split("\n")
    out.pop()
    return out
  except:
    sys.stderr.write("CMD failed\n")
    raise SystemExit

def checknumdir(dirs):
  r = ""
  for d in dirs:
    lines=listdir(d)
    lines.pop(0)
    if len(lines) > MAX_FICHEROS:
      r += d+"\n"
  
  return r

def checksizedir(dirs):
  r = ""
  for d in dirs:
    lines=listdir(d)
    size=lines[0].split()[1]
    unity=size[-1]
    size=size[:-1]
    if unity == "K":
      size = float(size) / float(10**3)
    elif unity == "G":
      size = float(size) * float(10**3)
    elif unity == "T":
      size = float(size) * float(10**6)

    if size > MAX_TAMANIO:
      r += d+"\n"

  return r


def handle():
  newd = replacedi()
  respuesta = ""

  nd = checknumdir(newd)
  sz = checksizedir(newd)

  if len(nd) > 0:
    respuesta += "Problems with number of fichs in:\n" + nd

  if len(sz) > 0:
    respuesta += "Problems with size in fichs:\n" + sz
  
  if options.force:
    if len(respuesta) == 0:
      respuesta += "Everything OK"

  if len(respuesta) > 0:
    respuesta += "Send from: " + os.uname()[1]
    bot.sendMessage(ID_USUARIO,respuesta)
  return 

def main():

  handle()

if __name__ == '__main__':
  main()