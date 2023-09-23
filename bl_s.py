from da_s import *
dbm = dbmnge('database.studnt')

class student:
    def __init__(self,id,name,family):
        self.id = id
        self.name = name
        self.family = family


    def show(self):
        return (self.id, self.name, self.family)


    def insert(self):
        Q = "insert into student values(?,?,?)"
        P = self.show()
        dbm.insert(Q,P)


    @staticmethod
    def select():
        Q = "select * from student "
        L = dbm.select(Q)
        return L


    @staticmethod
    def select1():
        Q = "select id,name,family from student"
        L = dbm.select(Q)
        return (L)



class professor:
    def __init__(self,id,name,family):
        self.id = id
        self.name = name
        self.family = family


    def show(self):
        return (self.id,self.name,self.family)


    def insert(self):
        Q = "insert into professor values(?,?,?)"
        P = self.show()
        dbm.insert(Q,P)


    @staticmethod
    def select():
        Q = "select * from professor "
        L = dbm.select(Q)
        return L


    @staticmethod
    def search3(c):
        Q = "select name,family from professor where id in(select pid from lesson where id="+ str(c)+")"
        L = dbm.select(Q)
        return L



class lesson:
    def __init__(self,id,pid,name,vahed):
        self.id = id
        self.pid = pid
        self.name = name
        self.vahed = vahed


    def show(self):
        return (self.id,self.pid,self.name,self.vahed)


    def insert(self):
        Q = "insert into lesson values(?,?,?,?)"
        P = self.show()
        dbm.insert(Q, P)


    @staticmethod
    def select():
        Q = "select * from lesson "
        L = dbm.select(Q)
        return L


    @staticmethod
    def search1(c):
        Q = "select name from lesson where id ="+str(c)
        L = dbm.select(Q)
        return L


    def avg(self):

        st = '____________________report card___________________________'
        st += "\nStudent ID\tstudent Name\tstudent Family\taverage"
        Q = "select * from student"
        L = dbm.select(Q)
        o = 0
        for i in L:
            s = scor.average_s()
            st += '\n'
            st += '\t' + str(i[0]) + '\t\t' + i[1] + '\t\t' + i[2] + '\t' + str(s[o])
            o += 1
        st += '\n__________________________________________________________\n'
        f = open('average.txt', 'w')
        f.write(st)



class scor:
    def __init__(self,sid,score,lid):
        self.sid = sid
        self.score = score
        self.lid = lid


    def show(self):
        return (self.sid,self.score,self.lid)


    def insert(self):
        Q = "insert into scor values(?,?,?)"
        P = self.show()
        dbm.insert(Q, P)


    @staticmethod
    def select():
        Q = "select * from scor "
        L = dbm.select(Q)
        return L


    @staticmethod
    def average_s():

        avg_list = []
        sorat = 0
        makhraj = 0

        Q1 = "select * from student"
        L1 = dbm.select(Q1)
        k = len(L1)
        for i in range(k):
            Q2 = "select score,(select vahed from lesson where id=lid) from scor where sid=" + str(L1[i][0])
            L2 = dbm.select(Q2)
            for o in L2:
                sorat += (o[0] * o[1])
                makhraj += o[1]

            averaj = round(sorat/makhraj, 2)
            avg_list.append(averaj)

        return avg_list
