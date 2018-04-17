# -*- coding: utf-8 -*-

import requests

from time import sleep

ip = '10.1.1.64'
port = 80

url = 'http://' + ip + ':' + str(port)
apiPath = 'index.htm'
checkPath = 'reg.html'

authUser = "admin"
authPass = "e2r2e8k3"

headers = {'Content-Type': 'application/x-www-form-urlencoded'}
data = {'RESET':'NORMAL'}

connErr = False

# Faz o reboot do aparelho...
try:
    response = requests.post(url + '/' + apiPath,data=data,auth=(authUser,authPass),headers=headers,timeout=2)
except requests.exceptions.ReadTimeout:
    print('INFO: TIP 100 reiniciado!')
except requests.exceptions.ConnectionError:
    print('ERRO: Falha ao conectar no TIP 100!')

    connErr = True

if not connErr:
    print('INFO: Verificando se o telefone já reiniciou...')
    sleep(7)

    # Checa se o aparelho foi reiniciado com sucesso
    try:
        response = requests.get(url + '/' + checkPath,auth=(authUser,authPass),timeout=5)
        if response.status_code == requests.codes.ok:
            print('INFO: Telefone IP TIP 100 reiniciado com SUCESSO!')
    except requests.exceptions.ReadTimeout:
        print('ERRO: Falha ao reiniciar o TIP 100')
