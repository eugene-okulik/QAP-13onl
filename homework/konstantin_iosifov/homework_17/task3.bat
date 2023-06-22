@echo off

dir /b /s /a:-d /o:n "C:\var\log\*.log"


#!/bin/bash

find /var/log -type f -name "*.log"
