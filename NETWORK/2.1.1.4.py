import sys
import requests

exit_code = 0
port_num = 80

if len(sys.argv) not in [2, 3]:
    print("Numero de argumentos incorrettos: ao menos 1 argumento é esperado, não mais que 2 argumentos são permitidos:")
    print("- Endereço HTTP do servidor (obrigatório)")
    print("- Número da porta (Caso argumento seja omitido a porta padrão será a 80)")
    print("Exit code 1")
    sys.exit(1)
    
elif len(sys.argv) == 3:
    if not sys.argv[2].isnumeric():
        print("Número de porta Inválido")
        exit_code = 2
        print("Exit code 2")
        sys.exit(2)
    else:
        port_num = int(sys.argv[2])



url= sys.argv[1][:-1] + ":" + str(port_num) + "/"
print(url) 

try:
    reply = requests.head(url, timeout=10)
except requests.RequestException:
    print("Erro de comunicação")
    sys.exit(3)

except requests.exceptions.Timeout:
    print("Servidor não responde")
    print("Exit code 4")
    sys.exit(4)

except requests.exceptions.InvalidSchema:
    print("Endereço de URL incorreto")
    print("Exit code 5")
    sys.exit(5)
else:
    if reply.status_code == requests.codes.not_found:
        print("Conteudo não encontrado")
        print("Exit code 6")
        sys.exit(6)

  
reply = str(reply)
reply = reply[1:reply.find('>')]
    
print(reply)


