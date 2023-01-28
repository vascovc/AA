from ctypes import sizeof
import networkx as nx
import matplotlib.pyplot as plt
import time 
from itertools import combinations
import csv

def generate_graph(nodes,p_edges):
    G = nx.fast_gnp_random_graph(nodes,p_edges,seed = 97746,directed=False)
    return G

def exhaustive_no_lock(G):
    nodes = list(G.nodes())
    best_combo = []
    global iter
    iter = 0
    global number_of_solutions
    number_of_solutions = 0

    for n in range(1,len(nodes)+1): # o vazio ja e o default
        list_combinations = list(combinations(nodes,n)) #vai se fazendo as combinacoes                       
        for a in range(len(list_combinations)): #ter todas as combinacoes e ver se sao validas
            list_nodes = list_combinations[a]
            list_nodes = list(list_nodes)    #ter os vertices da combinacao                                                                                        
            lock = False 
            for i in range(len(list_nodes)-1):     #percorrer do primeiro ao penultimo vertice                                   
                for j in range(i+1,len(list_nodes)):  #do vertice a seguir ao i ate ao ultimo                                                       
                    iter += 1
                    if list_nodes[j] in G.neighbors(list_nodes[i]):    #se eles sao vizinhos entao acabou
                        lock = True 
            if not lock: 
                number_of_solutions += 1 #se e possivel ent o numero de solucoes possiveis aumenta
                if len(best_combo) < len(list_nodes): 
                    number_of_solutions = 1 #chegamos a um resultado melhor entao passou a haver so uma solucao
                    best_combo = list_nodes
    return best_combo

def exhaustive(G):
    nodes = list(G.nodes())
    best_combo = []
    global iter
    iter = 0
    for n in range(1,len(nodes)+1):
        list_combinations = list(combinations(nodes,n))
        for a in range(len(list_combinations)):
            list_nodes = list_combinations[a]
            list_nodes = list(list_nodes)                                                                         
            lock = False
            for i in range(len(list_nodes)-1):                                                          
                for j in range(i+1,len(list_nodes)):                                            
                    iter += 1
                    if list_nodes[j] in G.neighbors(list_nodes[i]):                            
                        lock = True
                        break # nao vale a pena ver o resto da combinacao
                if lock:
                    break # se ja nao vale a pena ver o resto da combinacao
            if not lock:
                if len(best_combo) < len(list_nodes):
                    best_combo = list_nodes
    return best_combo

def exhaustive_faster(G):
    nodes = list(G.nodes())
    best_combo = []
    global iter
    for n in range(len(nodes),0,-1): #comecar ao contrario
        list_combinations = list(combinations(nodes,n)) 
        for a in range(len(list_combinations)):
            if len(list_combinations[a]) > len(best_combo):       #se a combinacao for maior que o melhor conjunto ja encontrado e que vale a pena analisar                                          
                list_nodes = list_combinations[a]
                list_nodes = list(list_nodes)                                                                                      
                lock = False
                for i in range(0,len(list_nodes)-1):                                                       
                    for j in range(i+1,len(list_nodes)):                                                 
                        iter += 1
                        if list_nodes[j] in G.neighbors(list_nodes[i]):                               
                            lock = True
                            break
                    if lock:
                        break
                if not lock:
                    if len(best_combo) < len(list_nodes):
                        best_combo = list_nodes
            else:
                break
    return best_combo

def exhaustive_the_fastest(G):
    nodes = list(G.nodes())
    best_combo = []
    global iter
    iter = 0
    for n in range(len(nodes),0,-1): #comecar ao contrario
        if n >len(best_combo): #so se o tamanho da possivel combinacao for maior e que vale a pena se quer gerar-se
            list_combinations = list(combinations(nodes,n)) 
            for a in range(len(list_combinations)):
                if len(list_combinations[a]) > len(best_combo):       #se a combinacao for maior que o melhor conjunto ja encontrado e que vale a pena analisar                                          
                    list_nodes = list_combinations[a]
                    list_nodes = list(list_nodes)                                                                                      
                    lock = False
                    for i in range(0,len(list_nodes)-1):                                                       
                        for j in range(i+1,len(list_nodes)):                                                 
                            iter += 1
                            if list_nodes[j] in G.neighbors(list_nodes[i]):                               
                                lock = True
                                break
                        if lock:
                            break
                    if not lock:
                        if len(best_combo) < len(list_nodes):
                            best_combo = list_nodes
                else:
                    break
        else:
            break
    return best_combo

def greedy(G):
    global iter
    iter = 0
    result = []

    while G.number_of_nodes() > 0:#enquanto houver vertices                                                  
        nodes = list(G.nodes())
        first = nodes[0]
        for V in nodes:                                                                                    
            iter += 1
            if len(list(G.neighbors(first))) > len(list(G.neighbors(V))):                                      
                first = V
        #escolher o vertice com menor numero de vizinhos
        result.append(first)
        for i in list(G.neighbors(first)):                                                          
            iter += 1
            G.remove_node(i)#removemos os vizinhos deste vertice e ficamos com um grafo independente dele
        G.remove_node(first)
    return result

def plot_graphs(G,result):
    color_map = []
    for node in G:
        if node in result:
            color_map.append("red")
        else:
            color_map.append("c")
    nx.draw_circular(G,with_labels=True,node_color=color_map,node_size=600)
    plt.savefig("c:/Users/Vasco Costa/Documents/MEGAsync/4-1/AA/projeto_1/Figure_1.png",format="png")
    plt.show()
    return

def make_all():
    prob = [0,0.125,0.25,0.50,0.75,1]
    header = [ [str(a)+"_time_exhaustive",str(a)+"_iter_exhaustive",str(a)+"_num_elementos_exhaustive",
                str(a)+"_time_exhaustive_faster",str(a)+"_iter_exhaustive_faster",str(a)+"_num_elementos_exhaustive_faster",
                str(a)+"_time_gridy",str(a)+"_iter_gridy",str(a)+"_num_elementos_gridy"] for a in prob]
    header = ['nodes']+[item for sublist in header for item in sublist]
    
    print(header)
    funct = "c:/Users/Vasco/Documents/MEGAsync/4-1/AA/projeto_1/all_faster_c.csv"
    with open(funct,'w',encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)

    for nodes in range(4,21):
        edges_result = [nodes]
        print(nodes)
        for p_edges in prob:
            G = generate_graph(nodes,p_edges)
            global iter
            global calls

            iter = 0
            tic = time.perf_counter()
            result = exhaustive(G.copy())
            toc = time.perf_counter()
            edges_result.append(toc-tic)
            edges_result.append(iter)
            edges_result.append(len(result))

            iter = 0
            tic = time.perf_counter()
            result = exhaustive_the_fastest(G.copy())
            toc = time.perf_counter()
            edges_result.append(toc-tic)
            edges_result.append(iter)
            edges_result.append(len(result))
            
            iter = 0
            tic = time.perf_counter()
            result_1 = greedy(G.copy())
            toc = time.perf_counter()
            edges_result.append(toc-tic)
            edges_result.append(iter)
            edges_result.append(len(result_1))

        with open(funct,"a",encoding='UTF8',newline='\n') as f:
            writer = csv.writer(f)
            writer.writerow(edges_result)

def make_bad_exhaustive():
    prob = [0,0.125,0.25,0.50,0.75,1]
    header = [ [str(a)+"_time_exhaustive",str(a)+"_iter_exhaustive",str(a)+"_num_elementos_exhaustive",
                str(a)+"_number_of_solutions"] for a in prob]
    header = ['nodes']+[item for sublist in header for item in sublist]
    
    print(header)
    #fixo
    funct = "c:/Users/Vasco Costa/Documents/MEGAsync/4-1/AA/projeto_1/all_bad_exhaustive_2.csv"
    #asus
    #funct = "c:/Users/Vasco/Documents/MEGAsync/4-1/AA/projeto_1/all_2.csv"
    with open(funct,'w',encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)

    for nodes in range(4,27):
        edges_result = [nodes]
        print(nodes)
        for p_edges in prob:
            G = generate_graph(nodes,p_edges)
            global iter
            global number_of_solutions

            iter = 0
            number_of_solutions = 0
            tic = time.perf_counter()
            result = exhaustive_no_lock(G.copy())
            toc = time.perf_counter()
            nx.maximal_independent_set(G,result)
            edges_result.append(toc-tic)
            edges_result.append(iter)
            edges_result.append(len(result))
            edges_result.append(number_of_solutions)

        with open(funct,"a",encoding='UTF8',newline='\n') as f:
            writer = csv.writer(f)
            writer.writerow(edges_result)


def main():
    #make_bad_exhaustive() #quando foi para correr a funcao que nao faz o lock
    make_all() #tirar os valores todos para o metodo euxaustivo, melhorado e greedy
    nodes = 10
    p_edges = 0.4

    G = generate_graph(nodes,p_edges)

    print("greedy")
    tic = time.perf_counter()
    result = greedy(G.copy())
    toc = time.perf_counter()
    print(toc-tic)
    print(len(result))
    print(result)
    nx.maximal_independent_set(G,result) # para verificar se o resultado e independente
    print()

    print("normal")
    tic = time.perf_counter()
    result = exhaustive(G.copy())
    toc = time.perf_counter()
    print(toc-tic)
    print(len(result))
    print(result)
    nx.maximal_independent_set(G,result)
    print()

    print("exhaustive_faster")
    tic = time.perf_counter()
    result = exhaustive_faster(G.copy())
    toc = time.perf_counter()
    print(toc-tic)
    print(len(result))
    print(result)
    nx.maximal_independent_set(G,result)
    print()

    print("exhaustive_the_fastest")
    tic = time.perf_counter()
    result = exhaustive_the_fastest(G.copy())
    toc = time.perf_counter()
    print(toc-tic)
    print(len(result))
    print(result)
    nx.maximal_independent_set(G,result)
    print()

    plot_graphs(G,result)
    """
    #G.add_edge(1,3) # nodes 4, p 0.7 da erro como se esperava
    nx.maximal_independent_set(G,result) # para verificar se o resultado e independente
    plot_graphs(G,result)
    """

if __name__ == "__main__":
   main()