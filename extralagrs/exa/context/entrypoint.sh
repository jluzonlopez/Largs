#!/bin/bash
cp /tmp/romanclient.py /bin/romanclient.py
cp /tmp/romanserver.py /bin/romanserver.py
romanserver.py tcp 12008 &
/bin/bash