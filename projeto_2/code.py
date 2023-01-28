from ctypes import sizeof
import networkx as nx
import matplotlib.pyplot as plt
import time 
import random
import math
import csv

random.seed(97746)

def generate_graph(nodes,p_edges):
    G = nx.fast_gnp_random_graph(nodes,p_edges,seed = 97746,directed=False)
    return G

def random_method_generate_combination(G,percent):
    nodes = list(G.nodes())
    best_combo = []
    global iter
    global confs_tested
    global tries
    iter = 0
    confs_tested = 0
    tries = 0

    for n in range(len(nodes),0,-1): #comecar ao contrario
        k = math.ceil( math.factorial(len(nodes))//( math.factorial(n)*math.factorial( len(nodes)-n ) ) * percent)
        #print(n,":",k)
        testing = 0
        combinations_seen = {}
        while testing < k:
            count = 0
            list_nodes = []  
            while(count < n): #ate se terem os n vertices de uma combinacao
                r = random.randint(0,len(nodes)-1)
                if nodes[r] not in list_nodes:
                    list_nodes.append(nodes[r])
                    count += 1
            sorted_list = tuple(sorted(list_nodes))
            tries += 1
            if sorted_list not in combinations_seen: #se nao tiver sido uma combinacao vista analisa-se
                confs_tested += 1
                lock = False
                testing += 1
                combinations_seen[sorted_list] = True
                for i in range(0,len(list_nodes)-1):                                                       
                    for j in range(i+1,len(list_nodes)):                                                 
                        iter += 1
                        if list_nodes[j] in G.neighbors(list_nodes[i]):                               
                            lock = True
                            break #nao e combinacao possivel
                    if lock:
                        break #nao e combinacao possivel
                if not lock:
                    if len(best_combo) < len(list_nodes):
                        best_combo = list_nodes
                        return best_combo # ja se encontrou um independente deste tamanho, entao esta feito porque nao vai aparecer maior
    return best_combo

def random_method_generate_combination_limit(G,limit):
    nodes = list(G.nodes())
    best_combo = []
    global iter
    global confs_tested
    global tries
    iter = 0
    confs_tested = 0
    tries = 0

    for n in range(len(nodes),0,-1): #comecar ao contrario
        k = math.factorial(len(nodes))//( math.factorial(n)*math.factorial( len(nodes)-n ) )
        if k > limit:
            k = limit
        #print(n,":",k)
        testing = 0
        combinations_seen = {}
        while testing < k:
            count = 0
            list_nodes = []  
            while(count < n): #ate se terem os n vertices de uma combinacao
                r = random.randint(0,len(nodes)-1)
                tries += 1
                if nodes[r] not in list_nodes:
                    list_nodes.append(nodes[r])
                    count += 1
            sorted_list = tuple(sorted(list_nodes))

            if sorted_list not in combinations_seen: #se nao tiver sido uma combinacao vista analisa-se
                confs_tested += 1
                lock = False
                testing += 1
                combinations_seen[sorted_list] = True
                for i in range(0,len(list_nodes)-1):                                                       
                    for j in range(i+1,len(list_nodes)):                                                 
                        iter += 1
                        if list_nodes[j] in G.neighbors(list_nodes[i]):                               
                            lock = True
                            break #nao e combinacao possivel
                    if lock:
                        break #nao e combinacao possivel
                if not lock:
                    if len(best_combo) < len(list_nodes):
                        best_combo = list_nodes
                        return best_combo # ja se encontrou um independente deste tamanho, entao esta feito porque nao vai aparecer maior
    return best_combo

def random_method_generate_combination_2k(G):
    nodes = list(G.nodes())
    best_combo = []
    global iter
    global confs_tested
    global tries
    iter = 0
    confs_tested = 0
    tries = 0

    for n in range(len(nodes),0,-1): #comecar ao contrario
        k = math.ceil(math.factorial(len(nodes))//( math.factorial(n)*math.factorial( len(nodes)-n ) ) // 2**n)
        #print(n,":",k)
        testing = 0
        combinations_seen = {}
        while testing < k:
            count = 0
            list_nodes = []  
            while(count < n): #ate se terem os n vertices de uma combinacao
                r = random.randint(0,len(nodes)-1)
                tries += 1
                if nodes[r] not in list_nodes:
                    list_nodes.append(nodes[r])
                    count += 1
            sorted_list = tuple(sorted(list_nodes))

            if sorted_list not in combinations_seen: #se nao tiver sido uma combinacao vista analisa-se
                confs_tested += 1
                lock = False
                testing += 1
                combinations_seen[sorted_list] = True
                for i in range(0,len(list_nodes)-1):                                                       
                    for j in range(i+1,len(list_nodes)):                                                 
                        iter += 1
                        if list_nodes[j] in G.neighbors(list_nodes[i]):                               
                            lock = True
                            break #nao e combinacao possivel
                    if lock:
                        break #nao e combinacao possivel
                if not lock:
                    if len(best_combo) < len(list_nodes):
                        best_combo = list_nodes
                        return best_combo # ja se encontrou um independente deste tamanho, entao esta feito porque nao vai aparecer maior
    return best_combo

def random_method_generate_combination_2n(G):
    nodes = list(G.nodes())
    best_combo = []
    global iter
    global confs_tested
    global tries
    iter = 0
    confs_tested = 0
    tries = 0

    for n in range(len(nodes),0,-1): #comecar ao contrario
        #k = math.ceil( math.factorial(len(nodes))//( math.factorial(n)*math.factorial( len(nodes)-n ) ) // 2**len(nodes) )
        k=1
        #print(n,":",k)
        testing = 0
        combinations_seen = {}
        while testing < k:
            count = 0
            list_nodes = []  
            while(count < n): #ate se terem os n vertices de uma combinacao
                tries += 1
                r = random.randint(0,len(nodes)-1)
                if nodes[r] not in list_nodes:
                    list_nodes.append(nodes[r])
                    count += 1
            sorted_list = tuple(sorted(list_nodes))

            if sorted_list not in combinations_seen: #se nao tiver sido uma combinacao vista analisa-se
                confs_tested += 1
                lock = False
                testing += 1
                combinations_seen[sorted_list] = True
                for i in range(0,len(list_nodes)-1):                                                       
                    for j in range(i+1,len(list_nodes)):                                                 
                        iter += 1
                        if list_nodes[j] in G.neighbors(list_nodes[i]):                               
                            lock = True
                            break #nao e combinacao possivel
                    if lock:
                        break #nao e combinacao possivel
                if not lock:
                    if len(best_combo) < len(list_nodes):
                        best_combo = list_nodes
                        return best_combo # ja se encontrou um independente deste tamanho, entao esta feito porque nao vai aparecer maior
    return best_combo

def greedy_random(G,time_wanted):
    global iter
    global confs_tested
    global tries
    iter = 0
    confs_tested = 0
    tries = 0

    confs = {}
    result = []
    tic = time.perf_counter()
    while time.perf_counter() - tic < time_wanted:
        result_1 = []
        F = G.copy()
        while F.number_of_nodes() > 0: #enquanto houver vertices                                                  
            nodes = list(F.nodes())
            vert = random.choice(nodes)
            result_1.append(vert)
            for i in list(F.neighbors(vert)):                                                          
                iter += 1
                F.remove_node(i)#removemos os vizinhos deste vertice e ficamos com um grafo independente dele
            F.remove_node(vert)
        if len(result_1) > len(result):
            result = result_1
        sorted_conf = tuple(sorted(result_1))
        tries += 1 # quantas combinacoes no total mesmo podendo ser iguais
        if sorted_conf not in confs:
            confs[sorted_conf] = True # len(confs) # dava o numero de combinacoes diferentes
    confs_tested = tries # quantas combinacoes foram vistas
    return result

def plot_graphs(G,result):
    color_map = []
    for node in G:
        if node in result:
            color_map.append("red")
        else:
            color_map.append("c")
    nx.draw_circular(G,with_labels=True,node_color=color_map,node_size=600)
    plt.savefig("c:/Users/Vasco Costa/Documents/MEGAsync/4-1/AA/projeto_2/Figure_1.png",format="png")
    plt.show()
    return

def make_all(percent = 0.2,time_wanted = 3,limit=1000):
    prob = [0.0,0.125,0.25,0.50,0.75,1.0]

    names = ["generate","generate_limit","generate_2k","generate_2n","greedy"]
    header = [ [str(a)+"_time_"+name,str(a)+"_iter_"+name,str(a)+"_num_elementos_"+name,str(a)+"_confs_tested_"+name,str(a)+"_tries_"+name] for a in prob for name in names ]
    
    header = ['nodes']+[item for sublist in header for item in sublist]
    
    print(header)
    funct = "c:/Users/Vasco Costa/Documents/MEGAsync/4-1/AA/projeto_2/projeto_2_all.csv"
    #funct = "c:/Users/Vasco/Documents/MEGAsync/4-1/AA/projeto_2/projeto_2_all.csv"
    with open(funct,'w',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
    
    for nodes in range(4,50):
        edges_result = [nodes]
        print(nodes)
        for p_edges in prob:
            G = generate_graph(nodes,p_edges)
            global iter
            global confs_tested
            global tries

            iter = 0
            confs_tested = 0
            tries = 0
            tic = time.perf_counter()
            result = random_method_generate_combination(G.copy(), percent)
            toc = time.perf_counter()
            edges_result.append(toc-tic)
            edges_result.append(iter)
            edges_result.append(len(result))
            edges_result.append(confs_tested)
            edges_result.append(tries)

            iter = 0
            confs_tested = 0
            tries = 0
            tic = time.perf_counter()
            result = random_method_generate_combination_limit(G.copy(), limit)
            toc = time.perf_counter()
            edges_result.append(toc-tic)
            edges_result.append(iter)
            edges_result.append(len(result))
            edges_result.append(confs_tested)
            edges_result.append(tries)

            iter = 0
            confs_tested = 0
            tries = 0
            tic = time.perf_counter()
            result = random_method_generate_combination_2k(G.copy())
            toc = time.perf_counter()
            edges_result.append(toc-tic)
            edges_result.append(iter)
            edges_result.append(len(result))
            edges_result.append(confs_tested)
            edges_result.append(tries)

            iter = 0
            confs_tested = 0
            tries = 0
            tic = time.perf_counter()
            result = random_method_generate_combination_2n(G.copy())
            toc = time.perf_counter()
            edges_result.append(toc-tic)
            edges_result.append(iter)
            edges_result.append(len(result))
            edges_result.append(confs_tested)
            edges_result.append(tries)
            
            iter = 0
            confs_tested = 0
            tries = 0
            tic = time.perf_counter()
            result_1 = greedy_random(G.copy(),time_wanted)
            toc = time.perf_counter()
            edges_result.append(toc-tic)
            edges_result.append(iter)
            edges_result.append(len(result_1))
            edges_result.append(confs_tested)
            edges_result.append(tries)

        with open(funct,"a",newline='') as f:
            writer = csv.writer(f)
            writer.writerow(edges_result)


def main():
    make_all(percent = 0.15, time_wanted = 3, limit = 1000) #tirar os valores todos para o metodo euxaustivo, melhorado e greedy

    nodes = 10
    p_edges = 0.5

    percent = 0.1
    time_wanted = 3
    limit = 500

    G = generate_graph(nodes,p_edges)

    print("greedy random -> time_wanted = ",time_wanted)
    tic = time.perf_counter()
    result = greedy_random(G.copy(),time_wanted)
    toc = time.perf_counter()
    print(toc-tic)
    print(len(result))
    print(confs_tested)
    #print(result)
    print()

    print("random reversed generate combination -> percent = ",percent)
    tic = time.perf_counter()
    result = random_method_generate_combination(G.copy(),percent)
    toc = time.perf_counter()
    print(toc-tic)
    print(len(result))
    print(confs_tested)
    #print(result)
    print()

    print("random reversed generate combination limit -> limit = ",limit)
    tic = time.perf_counter()
    result = random_method_generate_combination_limit(G.copy(),limit)
    toc = time.perf_counter()
    print(toc-tic)
    print(len(result))
    print(confs_tested)
    #print(result)
    print()

    print("random reversed generate combination 1/2^k")
    tic = time.perf_counter()
    result = random_method_generate_combination_2k(G.copy())
    toc = time.perf_counter()
    print(toc-tic)
    print(len(result))
    print(confs_tested)
    #print(result)
    print()

    print("random reversed generate combination 1/2^n")
    tic = time.perf_counter()
    result = random_method_generate_combination_2n(G.copy())
    toc = time.perf_counter()
    print(toc-tic)
    print(len(result))
    print(confs_tested)
    #print(result)
    print()

if __name__ == "__main__":
   main()