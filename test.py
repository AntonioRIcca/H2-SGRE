# import pymysql as msq
import sqlite3
import time

from faker import Faker

conn = sqlite3.connect('dati.db')

c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS utente(nome, indirizzo, numero, ip)')
conn.commit()

faker = Faker()
nome = faker.name()

c.execute('INSERT INTO utente VALUES (?, ?, ?, ?)', (nome, faker.address(), faker.phone_number(), faker.ipv4_public()))
conn.commit()

c.execute('SELECT * FROM utente WHERE nome = ?', (nome, ))
utente = c.fetchone()
print(utente)

# c.execute('SELECT nome FROM utente')
# names = c.fetchall()
names = [n[0] for n in c.execute('SELECT nome FROM utente')]
numbers = [float(n[0]) for n in c.execute('SELECT numero FROM utente')]
print(names)
print(numbers)
print(float(numbers[1]))