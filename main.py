import random

def rint(a, b):
    return random.randint(a, b)

class member:

    def __init__(self, id, init_genome):
        self.id = id
        self.genome = init_genome
        self.fitness = 0

class population:
    def __init__(self, member_count, gene_size, gene_scale, mutate_r):
        self.mutate_r = mutate_r

        self.member_count = member_count
        self.gene_size = gene_size
        self.gene_scale = gene_scale

        self.members = []
        for i in range(member_count):
            self.members.append(member(i, [rint(0, gene_scale) for i in range(gene_size)]))

    def debug(self):
        for m in self.members:
            print(f"{m.genome} score: {m.fitness}")

    def select(self):
        for m in self.members:
            m.fitness = sum(m.genome)
        self.members.sort(key=lambda m: m.fitness)

    def crossover(self):
        for i in range(0, len(self.members), 2):
            if i+1 < len(self.members):
                m1 = self.members[i].genome
                m2 = self.members[i+1].genome
                parent_pool = [m1, m2]
                #print(parent_pool)
                ch1 = []
                ch2 = []
                for j, gene in enumerate(m1):
                    choice1 = rint(0,1)
                    choice2 = abs(choice1-1)
                    ch1.append(parent_pool[choice1][j])
                    ch2.append(parent_pool[choice2][j])
                #print([ch1, ch2])
                self.members[i].genome = ch1
                #print(f"length: {len(self.members)}")
                self.members[i+1].genome = ch2
                
    def mutate(self):
        for i, m in enumerate(self.members):
            for j, g in enumerate(m.genome):
                if random.uniform(0, 1) <= self.mutate_r:
                    self.members[i].genome[j] = rint(0, self.gene_scale)
                    #print("zap")



p1 = population(20, 4, 9, 0.2)

print("init")
p1.debug()

'''
print("select")
p1.select()
p1.debug()

print("crossover")
p1.crossover()
p1.debug()

print("mutate")
p1.mutate()
p1.debug()
'''

def step_pop(pop):
    print("select")
    pop.select()
    print("crossover")
    pop.crossover()
    print("mutate")
    pop.mutate()
    p1.debug()

def silent_step_pop(pop):
    pop.select()
    pop.crossover()
    pop.mutate()

while True:
    x=input("step")
    if x == " ":
        step_pop(p1)
    elif x == "":
        silent_step_pop(p1)
    else:
        break
