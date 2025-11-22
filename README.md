# Servidor Web HTTP

Este projeto implementa um servidor HTTP básico utilizando sockets em Python. O servidor consegue receber requisições HTTP e enviar arquivos HTML que estejam no mesmo diretório do script. O objetivo é demonstrar o funcionamento essencial de um servidor web simples para fins de aprendizado.

Como testar no navegador:
Digite no navegador o endereço: http://127.0.0.1:6789/HelloWorld.html

Se quiser acessar de outro dispositivo na mesma rede, substitua 127.0.0.1 pelo IP da máquina onde o servidor está em execução.

Funcionalidades implementadas:

Criação e uso de socket TCP.

Tratamento de requisições HTTP enviadas pelo navegador.

Envio de arquivos HTML como resposta ao cliente.

Envio de cabeçalhos HTTP básicos.

Retorno de erro 404 quando o arquivo solicitado não é encontrado.

Ignora requisições inválidas e automáticas, como /favicon.ico.

Objetivo educacional:
Projeto utilizado para aprender conceitos de Redes de Computadores, comunicação via sockets e funcionamento básico do protocolo HTTP.