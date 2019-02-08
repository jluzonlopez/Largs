#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

#Jorge Luzón López
#jluzon

import subprocess,sys

def printout(out):
  lines=out.split("\n")
  lines.pop(0)
  lines.pop()
  print lines
  for line in lines:
    field=line.split()
    if field[0][0] == '-':
      print field[8] + " " + field[4]

if __name__ == '__main__':
  cmd="ls -l"
  try:
    out=subprocess.check_output(cmd.split())
  except subprocess.CalledProcessError:
    sys.stderr.write("CMD failed\n")
    raise SystemExit

  printout(out)
                                                                                                                                 