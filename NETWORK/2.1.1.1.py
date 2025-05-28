"""
Obrigatorio - escrever uma interface de comando, para diagnosticar o status de um http sever apenas para saber se o servidor esta dead ou alive.

Opcioonal - o numero da porta do server qualquer ausencia supõe que é porta 80

Use o metodo head ao inves de get - forçando ao server enviar resposta completa mas sem nenhum conteudo, é o suficiente para saber se esta funcionando


A ferramenta checa se foi invocado corretamente, e se falta algum argumento, imprimindo mensagem de erro e returna exit code 1
Se tem 2 argumentos e o segundo nao for integer imprimir mensagem de erro e exit code 2
se for timeout exit code 3
se conexao falhar exit code 4
se estiver tudo ok a primeira linha da resposta é mostada na tela

dicas:
    
para acessar command line arguments usar abrv, o tamanho 
"""

import sys
import socket

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



url= sys.argv[1]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(15)

try:
    sock.connect((url, port_num))
    sock.send(b"HEAD / HTTP/1.1\r\nHost: " +
            bytes(url, "utf8") + 
            b"\r\nConnection: close\r\n\r\n")
    

except TimeoutError:
    print("Sevidor não responde")
    print("Exit code 3")
    sys.exit(3)

except socket.gaierror:
    print("Falha na Conexão")
    print("Exit code 4")
    sys.exit(4)
else:
    
    reply = str(sock.recv(50))
    reply = reply[2:reply.find('\\')]
    
    print(reply)


sock.shutdown(socket.SHUT_RDWR)
sock.close()


