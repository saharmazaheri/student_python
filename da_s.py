import sqlite3

connection = sqlite3.connect('database.studnt')
cursor = connection.cursor()

class dbmnge:

    def __init__(self, add):

        self.connection = sqlite3.connect(add)
        self.cursor=self.connection.cursor()


    def insert(self, Q, P):

        self.cursor.execute(Q,P)
        self.connection.commit()


    def select(self,Q):

        self.cursor.execute(Q)
        L=self.cursor.fetchall()
        return L

#cursor.execute('create table student(id int primary key,name nvarchar(20),family nvarchar(20))')
#connection.commit()

#cursor.execute('create table professor(id int primary key,name nvarchar(20),family nvarchar(20))')
#connection.commit()

#cursor.execute('create table lesson(id int primary key,pid int,name nvarchar(20),vahed int)')
#connection.commit()

#cursor.execute('create table scor(sid int ,score float,lid int)')
#connection.commit()