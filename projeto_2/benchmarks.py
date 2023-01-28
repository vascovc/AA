import networkx as nx
import code as methods
import time
import pandas as pd

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

def read_graph_sw(size = "SWtinyG"):
    file = "c:/Users/Vasco Costa/Documents/MEGAsync/4-1/AA/projeto_2/SW_ALGUNS_GRAFOS/"+ size + ".txt"
    G = nx.Graph()
    with open(file,'r') as f:
        for i in range(4):# as primeiras linhas nao interessam
            [int(x) for x in next(f).split()] # read first line
        for line in f: # read rest of lines
            array = [int(x) for x in line.split()]
            e1 = array[0]
            e2 = array[1]
            G.add_edge(e1, e2)
    return G
def read_graph_snap(name):
    file = "c:/Users/Vasco Costa/Documents/MEGAsync/4-1/AA/projeto_2/SW_ALGUNS_GRAFOS/"+ name + ".txt"
    G = nx.Graph()
    with open(file,'r') as f:
        for line in f: # read rest of lines
            array = [int(x) for x in line.split()]
            e1 = array[0]
            e2 = array[1]
            G.add_edge(e1, e2)
    return G

def read_graph_csv(name):
    file = "c:/Users/Vasco Costa/Documents/MEGAsync/4-1/AA/projeto_2/SW_ALGUNS_GRAFOS/"+ name + ".csv"
    G = nx.Graph()
    df = pd.read_csv(file)
    for l in df.values:
        G.add_edge(l[0], l[1])
    return G

def main():
    files_size = ["SWtinyG","SWmediumG"]
    files_snap = ["facebook_combined"]
    files_csv = ["deezer_clean_data/RO_edges","deezer_clean_data/HU_edges","deezer_clean_data/HR_edges"]

    files = files_size + files_snap + files_csv

    for name in files[3:]:
        
        if name in files_size:
            G = read_graph_sw(name)
        elif name in files_snap:
            G = read_graph_snap(name)
        else:
            G = read_graph_csv(name)
            name = name.split("/")[-1]
        
        funct = "c:/Users/Vasco Costa/Documents/MEGAsync/4-1/AA/projeto_2/benchmarks_"+name+".txt"
        with open(funct,'w') as f:
            print("benchmarks",file=f)
        
        time_wanted = 10
        limit = 50
        with open(funct,'a') as f:
            print(name,file=f)
            print(name)
            print("greedy project 1",file=f)
            print("greedy project 1")
            tic = time.perf_counter()
            result = greedy(G.copy())
            toc = time.perf_counter()
            print("\t time: ",toc-tic,file=f)
            print("\t len_elementos: ",len(result),file=f)
        with open(funct,'a') as f:
            print("greedy random -> time_wanted = ",time_wanted,file=f)
            print("greedy random -> time_wanted = ",time_wanted)
            tic = time.perf_counter()
            result = methods.greedy_random(G.copy(),time_wanted)
            toc = time.perf_counter()
            print("\t time: ",toc-tic,file=f)
            print("\t len_elementos: ",len(result),file=f)    
        with open(funct,'a') as f:
            print("random reversed generate combination 1/2^n",file=f)
            print("random reversed generate combination 1/2^n")
            tic = time.perf_counter()
            result = methods.random_method_generate_combination_2n(G.copy())
            toc = time.perf_counter()
            print("\t time: ",toc-tic,file=f)
            print("\t len_elementos: ",len(result),file=f)   
        with open(funct,'a') as f:
            print("random reversed generate combination 1/2^k",file=f)
            print("random reversed generate combination 1/2^k")
            tic = time.perf_counter()
            result = methods.random_method_generate_combination_limit(G.copy(),limit)
            toc = time.perf_counter()
            print("\t time: ",toc-tic,file=f)
            print("\t len_elementos: ",len(result),file=f)
        with open(funct,'a') as f:
            print("random reversed generate combination limit -> limit = ",limit,file=f)
            print("random reversed generate combination limit -> limit = ",limit)
            tic = time.perf_counter()
            result = methods.random_method_generate_combination_limit(G.copy(),limit)
            toc = time.perf_counter()
            print("\t time: ",toc-tic,file=f)
            print("\t len_elementos: ",len(result),file=f)
            print("",file=f)
            print()


if __name__ == "__main__":
   main()


