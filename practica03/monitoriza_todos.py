#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

#Jorge Luzón López
#jluzon

import subprocess,sys

MAQUINAS = ["alpha01","alpha02"]
COMANDOS = ["touch /tmp/log_monitoriza_jluzon.txt","/home/alumnos/jluzon/lagrs/practica03/monitor.py -f"]

def doping(maq):
  cmd = "ping -c 1 -W 1 " + maq
  try:
    out=subprocess.check_call(cmd.split())
    return out 
  except:
    sys.stderr.write("PING failed\n")

def docomd(maq):
  for c in COMANDOS:
    cmd = "ssh "+ maq + " " + c
    try: 
      subprocess.check_call(cmd.split())
    except:
      sys.stderr.write("SSH CMD failed\n")
  return

def main():
  for pc in MAQUINAS:
    if doping(pc) == 0:
     docomd(pc)
 
if __name__ == '__main__':
  main()
