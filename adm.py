import sqlite3

banco = sqlite3.connect('spam.db')
cursor = banco.cursor()
while True:
        senha = input("Digite a senha: ")
        if senha == 'Passalha':
                print("Senha correta")
                break
        else:
                print("Senha errada")


cursor.execute("SELECT * FROM tokens")


ze = cursor.fetchall()

for p in ze:
        print(p)
