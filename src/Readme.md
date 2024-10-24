

NECESSÁRIO:
MYSQL INSTALADO
Python 3.x
Bibliotecas mysql-connector-python (mysql.connector) e pandas

Acesse o site: https://github.com/VinnySou/prj_Campeonato_Futebol e clique no botão verde <> Code e vá em Download ZIP
![image](https://github.com/user-attachments/assets/84a3e392-d900-4a74-855c-71a7893f37e9)

Abra a pasta Downloads e descompacte o arquivo prj_Camponato_Futebol-main.zip para a pasta Downloads
Após descompactar a pasta, abra o terminal do Linux
E execute o seguinte comando: 
    mysql -u root -p
Digite a senha: lab@Database2022

Feito isso, execute o seguinte comando:
CREATE DATABASE campeonato_de_futebol;
USE campeonato_de_futebol;
Após apresentar que a query foi efetuada, execute o seguinte comando:
source /home/labdatabase/Downloads/prj_Campeonato_Futebol-main/sql/create_tables_campeonato.sql (Ou se o caminho do projeto descompactado for diferente, coloque o caminho direcionando para o arquivo create_tables_campeonato.sql)


Feito isso, digite SHOW TABLES para verificar se criou as tabelas corretamente, se criadas basta fechar o terminal. 

![image](https://github.com/user-attachments/assets/0af1d231-c66e-41ea-ac86-e414d8e26511)


Agora, abra o terminal Linux novamente e execute os comandos:

pip install mysql-connector-python pandas
 Após a instalação, execute o programa - ainda no terminal - com o comando: 
 python /home/labdatabase/Downloads/prj_Campeonato_Futebol-main/src/principal.py
 
