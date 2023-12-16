import numpy as np;
import random;
import math;

class Articial_Bee_Colony():

    def __init__(self, 
                 objetive_function, 
                 num_variables, 
                 num_employed_bees, 
                 num_onlooker_bees,
                 max_iterations,
                 upper_limit,
                 lower_limit,
                 mobility):
    
        # Armazenando dados básicos de execução
        self.objetive_function = objetive_function;
        self.num_variables = num_variables;
        self.num_employed_bees = num_employed_bees;
        self.num_onlooker_bees = num_onlooker_bees;
        self.max_iterations = max_iterations;
        self.upper_limit = upper_limit;
        self.lower_limit = lower_limit;
        self.mobility = mobility;

    def run_algorithm(self):
        self.inicialization_phase();

        for iteration in range(self.max_iterations):
            self.employed_bees_phase();
            self.onlooker_bees_phase();
            self.scout_bees_phase();
    
    def inicialization_phase(self):
        # Fase de Inicialização
        self.population = np.random.uniform(low=self.lower_limit, high=self.upper_limit, size=self.num_employed_bees);
        print(self.population);
        self.best_solution = None;
        self.best_fitness = float('inf');
    
    # Fase das Abelhas Empregadas
    # Cada abelha se move a partir de sua posição atual até um novo ponto. Ao chegar nele, compara
    # o ponto inicial com o novo, e decide ficar no que tiver melhor nota pela função de desempenho;
    # Se a qualidade do novo ponto for melhor do que a melhor encontrada GLOBALMENTE até o momento, 
    # atualiza o valor da melhor solução
    def employed_bees_phase(self):

        # Ciclo que acessa a posição atual de cada abelha
        for i in range(self.num_employed_bees):
            # Seleciona a abelha (solução)
            solution = self.population[i]; 

            # Move a abelha a partir do seu ponto inicial até uma nova posição
            new_solution = solution + np.random.uniform(low=-self.mobility, high=self.mobility, size=None);
            print(new_solution);

            # Calcula o valor da função nessa nova solução encontrada (quanto menor, melhor - Problema de Minimização)
            fitness = self.objetive_function(new_solution);

            # Se o novo ponto possui um f(x) menor (maior qualidade), então ...
            if ((fitness < self.objetive_function(solution))
                and (new_solution >= self.lower_limit)
                and (new_solution <= self.upper_limit)):
                # ... atualiza a posição da abelha para esse novo local
                self.population[i] = new_solution;

                # Agora, se o f(x) for melhor (menor) que a melhor opção encontrada até então, atualiza o valor
                # dessa melhor opção com o valor encontrado
                if (fitness < self.best_fitness):
                    self.best_solution = new_solution;
                    self.best_fitness = fitness;

    # Fase das Abelhas Observadoras
    # São sorteadas N abelhas novas aleatórias
    # Cada abelha irá se mover a partir de sua posição original, encontrar um novo
    # ponto, ficar no melhor dos dois e, se esse ponto for melhor que a melhor 
    # solução encontrada até então, essa será atualizada (igual as abelhas empregadas), com a excessão do movimento se aleatório
    def onlooker_bees_phase(self):
        for i in range(self.num_onlooker_bees):
            # Escolhe um elemento aleatório da população
            solution = random.choice(self.population);

            # Move a Abelha até uma nova posição
            new_solution = solution + np.random.uniform(low = -self.mobility, high = self.mobility, size=None);

            # Calcula a qualidade dessa nova solução
            fitness = self.objetive_function(new_solution);

            # Se o valor f(x) do ponto novo for melhor do que a solução inicial,
            # reposiciona a abelha nesse novo ponto
            if ((fitness < self.objetive_function(solution))
                and (new_solution >= self.lower_limit)
                and (new_solution <= self.upper_limit)):

                index = np.where(self.population == solution)[0][0];
                self.population[index] = new_solution;

                # Caso o valor de f(x) nesse ponto for melhor (menor) que o melhor 
                # de todos já obtido, atualiza o valor do melhor de todos
                if (fitness < self.best_fitness):
                    self.best_solution = new_solution;
                    self.best_fitness = fitness;

    # Fase das Abelhas Batedoras
    # Se alguma abelha possui uma solução inadequada, ela será reposicionada aleatóriamente. Nesse caso, o reposicionamento acontece para todas as abelhas cujo f(x) é pior que a melhor solução encontrada até o momento
    def scout_bees_phase(self):

        for i in range(self.num_employed_bees):
            # Se o f(x) da abelha for maior que a melhor resposta encontrada até
            # agora, então ela é reposicionada de modo aleatório
            if (self.objetive_function(self.population[i]) >= self.best_fitness):
                self.population[i] = np.random.uniform(low=self.lower_limit, high=self.upper_limit, size=None);

def function1(x):
    return pow(x, 4) + pow(x, 3) - 2 * pow(x, 2);

def function2(x):
    return pow(x, 5) + pow(x, 4) - 3*pow(x, 3) -4*pow(x,2);

def function3(x):
    return pow(2, x) - pow(x, 5);

def function4(x):
    return math.sin(x);

ABC = Articial_Bee_Colony(max_iterations=100,
                          num_employed_bees=20,
                          num_onlooker_bees=20,
                          num_variables=20,
                          objetive_function=function3,
                          upper_limit=2*3.14159265,
                          lower_limit=0,
                          mobility=0.1);
ABC.run_algorithm();
print("O valor mínimo da função vale: \n" + 
      "f( " + str(ABC.best_solution) + " ) = " + str(ABC.best_fitness));