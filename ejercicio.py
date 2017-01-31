#!/usr/bin/python3

fich = open('/etc/passwd', 'r')
lineas = fich.readlines()

lineas[0] # "pepepepepeppe"
lineas[:1] # ["pepepepepeppe"]

for linea in lineas:
    login = linea[:linea.find(':')]
    shell = linea[linea.rfind(':')+1:-1]
    print(login, linea.find(':'), shell, linea.rfind(':'))

for linea in lineas:
    login = linea.split(':')[0]
    shell = linea.split(':')[-1][:-1]
    print(login, shell)

print(len(lineas))
fich.close()
