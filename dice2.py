import random
import sys
import numpy as np

class DND_die_roller:
    d = 2
    rr = 0 
    c = 100000
    ac = 0
    mod = 0
    dmgMod = 0
    adv = 0
    target = 0
    dmg = 0
    gwm = 0 
    
    def roll_dmg(self):
        rd1 = np.random.random_integers(1,self.d)
        rd2 = np.random.random_integers(1,self.d)
        if(rd1 <= self.rr) :
            return rd2
        else:
            return rd1
    
    def exec_test(self):
        tdmg = 0.0
    
        for i in range(0, self.c):
            r1 = np.random.random_integers(1,20)
            r2 = np.random.random_integers(1,20)
            if(r1 >= self.target or (self.adv == 1 and r2 >= self.target)):
                tdmg += self.roll_dmg() + self.dmgMod
                if(r1 == 20 or (self.adv == 1 and r2 == 20)):
                    tdmg += self.roll_dmg()
        return tdmg / self.c
    def load_list(self, data_list):
        self.d = int(data_list[0])
        self.ac = int(data_list[1])
        self.mod = int(data_list[2])
        self.dmgMod = int(data_list[3])
        if(len(data_list) >= 5):
            self.rr = int(data_list[4])
        if(len(data_list) >= 6):
            self.adv = int(data_list[5])
        if(len(data_list) >= 7):
            self.c = int(data_list[6])
        self.target = self.ac - self.mod
        self.dmg = (((self.d+1) / 2.0) + self.dmgMod)
    def load_many(self, filename):
        f_in = open(filename, 'r')
        data = f_in.readlines()
        f_in.close()
        f_out = open(filename + '.output', 'w')
        for line in data:
            data_list = line.split(",")
            if(len(data_list) >= 4):
                self.load_list(data_list)
                f_out.write(str(self.exec_test()) + '\n')
        f_out.close()

    def start(self):
        o = 99 
        while(o != 0):
            o = int(raw_input('3 exec, 4 show setting, 99 set settings, 0 exit: '))
            if(o == 1):
                    hits = 0.0
                    tdmg = 0.0
                    for i in range(0, c):
                        r1 = np.random.random_integers(1,20)
                        r2 = np.random.random_integers(1,20)
                        if(r1 >= target or (adv == 1 and r2 >= target)):
                            hits += 1
                            tdmg += dmg
                            if(r1 == 20 or (adv == 1 and r2 == 20)):
                                tdmg += ((d+1)/2.0)
                    print hits / c
                    print tdmg / c
            if(o == 2):
                    dmgtotal = 0.0
                    for i in range(0, c):
                        r1 = np.random.random_integers(1,d)
                        r2 = np.random.random_integers(1,d)
                        if(r1 <= rr):
                            dmgtotal += r2
                        else:
                            dmgtotal += r1
                    print dmgtotal / c
            if(o == 3):
                    print self.exec_test()
            if(o == 4):
                    print self.d
                    print self.rr
                    print self.c
                    print self.ac
                    print self.mod
                    print self.dmgMod
                    print self.adv
                    print self.target
                    print self.dmg
            if(o == 99):
                method = 'h'
                while(method != 'q'):
                    method = raw_input('(f)ill,(q)uit,(h)elp or other? ')
                    if(method == 'h'):
                        print 'Commands:'
                        print '(f)ill, (d)amage, (hi)t, (a)dvantages'
                        print 'gwm for great weapon master buff'
                        print 'load, load_many'
                        print '(q)uit, (h)elp'
                    if(method == 'f'):
                        self.d = int(raw_input('Dmg die size? '))
                        self.rr = int(raw_input('Reroll less than? '))
                        self.c = int(raw_input('Iterations? '))
                        self.ac = int(raw_input('AC? '))
                        self.mod = int(raw_input('To hit mod? '))
                        self.dmgMod = int(raw_input('dmg mod? '))
                        self.adv = int(raw_input('advantage? '))
                        self.target = self.ac - self.mod
                        self.dmg = (((self.d+1) / 2.0) + self.dmgMod)
                        method = 'q'
                    if(method == 'd'):
                        self.d = int(raw_input('Dmg die size? '))
                        self.dmgMod = int(raw_input('dmg mod? '))
                        self.dmg = (((self.d+1) / 2.0) + self.dmgMod)
                    if(method == 'hi'):
                        self.ac = int(raw_input('AC? '))
                        self.mod = int(raw_input('To hit mod? '))
                        self.target = self.ac - self.mod
                    if(method == 'a'):
                        self.rr = int(raw_input('Reroll less than? '))
                        self.adv = int(raw_input('advantage? '))
                    if(method == 'gwm'):
                        if(gwm == 0):
                            self.gwm = 1
                            self.mod -= 5
                            self.target += 5
                            self.dmgMod += 10
                            self.dmg += 10
                        else:
                            self.gwm = 0
                            self.mod += 5
                            self.target -= 5
                            self.dmgMod -= 10
                            self.dmg -= 10
                    if(method == 'load'):
                        fname = raw_input('Filename: ')
                        f_obj = open(fname, 'r')
                        data_str = f_obj.readline()
                        f_obj.close()
                        data_list = data_str.split(",")
                        if(len(data_list) >= 4):
                            print 'loading data'
                            self.load_list(data_list)
                        method = 'q'
                    if(method == 'load_many'):
                        fname = raw_input('Filename: ')
                        self.load_many(fname)

my_dnd_roller = DND_die_roller()
if(len(sys.argv) > 1):
    my_dnd_roller.load_many(sys.argv[1])
else:
    my_dnd_roller.start()
