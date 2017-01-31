#!/usr/bin/python3

fich = open('/etc/passwd', 'r')
lineas = fich.readlines ()
fich.close()

for linea in lineas:
    login = linea.split(':')[0]
    shell = linea.split(':')[-1][:-1]
    print(login + ' ' + shell)
