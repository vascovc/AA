import string
import math
import random 
import csv
import matplotlib.pyplot as plt

def exact_counter(file):
    dic = {}
    with open(file,"r") as f:
        while True:
            char = f.read(1)
            if not char:
                break
            if char in dic.keys():
                dic[char] += 1
            else:
                dic[char] = 1   
    return dic

def exact_counter_2(file): # como sabemos que letras vao estar disponiveis pode-se iniciar logo as letras e poupa-se com as comparacoes
    dic = {}
    for letter in list(string.ascii_uppercase):
        dic[letter] = 0
    with open(file,"r") as f:
        while True:
            char = f.read(1)
            if not char:
                break
            dic[char] += 1
    return dic

def toss_coin():
    return random.randint(0, 1)

def csuros(file,d=0):
    dic = {}
    t = {}
    M = 2**d
    for letter in list(string.ascii_uppercase):
        dic[letter] = 0
    with open(file,"r") as f:
        while True:
            char = f.read(1)
            if not char:
                break
            
            increase = True
            t[char] = math.floor(dic[char]/M)
            while t[char] > 0:
                if toss_coin():
                    increase = False
                    break
                t[char] -= 1
            if increase:
                dic[char] += 1

    real_aproxim = {}
    for key in dic.keys():
        u = dic[key]-(2**d)*t[key]
        real_aproxim[key] = (M+u)*2**t[key]-M
    return dic,t,real_aproxim

def space_saving(file,k=3):
    n = 0
    T = {}
    with open(file,"r") as f:
        while True:
            i = f.read(1)
            if not i:
                break

            n += 1
            if i in T.keys():
                T[i] += 1
            elif len(T) < k:
                T[i] = 1
            else:
                j = min(T,key=T.get)
                T[i] = T[j] + 1
                T.pop(j)
    return T,n

def bar_plot(result,folder,c,name):
    soma = sum(result.values())
    features_sorted = []
    importance_sorted = []
    unsorted_list = [(importance, feature) for feature, importance in 
                zip(result.keys(), result.values())]
    sorted_list = sorted(unsorted_list,reverse=True)
    for i in sorted_list:
        features_sorted += [i[1]]
        importance_sorted += [i[0]]
    
    plt.bar(features_sorted, [i/soma*100 for i in importance_sorted])
    plt.title("Percentage of ocurrences for the "+name+" counter")
    plt.xlabel('Letter')
    plt.ylabel('Percentage of ocurrences (%)')
    plt.savefig(folder+c[-1].split(".")[0]+"_"+name+".png",format="png")
    #plt.show()

def tester(folder,file,d_csuros=0,n_rep_csuros=1,k_space_saving=3):
    c = file.split("/")
    output = folder+c[-1].split(".")[0]+"_d"+str(d_csuros)+"_"+"n"+str(n_rep_csuros)+"_k"+str(k_space_saving)+".csv"
    with open(output, 'w', newline='') as f:
        writer = csv.writer(f)
        header = ["method"] + list(string.ascii_uppercase)
        writer.writerow(header)
        
        result = exact_counter_2(file)
        bar_plot(result,folder,c,"exact")
        result = [result[key] for key in result.keys()]
        result.insert(0,"Exato")
        writer.writerow(result)
        writer.writerow([])

        for i in range(1,n_rep_csuros+1):
            dic, t, result = csuros(file,d_csuros)
            result = [result[key] for key in result.keys()]
            result.insert(0,"Csuros_"+str(i))
            writer.writerow(result)
        writer.writerow([])
        
        result_1 = {}
        result, num = space_saving(file,k_space_saving)
        for letter in list(string.ascii_uppercase):
            result_1[letter] = 0
        for key in result.keys():
            result_1[key] = result[key]
        result_1 = [result_1[key] for key in result_1.keys()]
        result_1.insert(0,"space_saving")
        writer.writerow(result_1)

    return 0

def main():
    d = 3 # d do csuros
    n = 1 # repetições do csuros
    k = 5 # os maiores
    bit = 1 #True False
    #fixo
    folder = "c:/Users/Vasco Costa/Documents/MEGAsync/4-1/AA/projeto_3/"
    #portatil
    #folder = "c:/Users/Vasco/Documents/MEGAsync/4-1/AA/projeto_3/"
    
    folder_clean = folder+"clean_txt/"
    files = ["frei_luis.txt","camoes_all.txt","all.txt"]
    file_use = files[1]

    if not bit:
        for d in range(13):
            n=50
            tester(folder,folder_clean+file_use,d,n,k)
        for k in [3,5,10]:
            d=0
            n=0
            tester(folder,folder_clean+file_use,d,n,k)
    
    if bit:
        #exact 
        print("exact ")
        result = exact_counter(folder_clean+file_use) # pode dar jeito para verificar se existem caracteres estranhos
        result = sorted(result.items(),key=lambda x:x[1],reverse=True)
        print(result)
        print()
        #exact sem os if
        print("exact melhorada")
        result = exact_counter_2(folder_clean+file_use)
        result = sorted(result.items(),key=lambda x:x[1],reverse=True)
        print(result)
        print()

        
        #csuros
        # d = 0 temos Morris counter
        print("csuros valor do contador d=",d)
        dic,t,result = csuros(folder_clean+file_use,d)
        dic = sorted(dic.items(),key=lambda x:x[1],reverse=True)
        t = sorted(t.items(),key=lambda x:x[1],reverse=True)
        result = sorted(result.items(),key=lambda x:x[1],reverse=True)
        print(dic)
        print(t)
        print("estimativa com as contas d=",d)
        print(result)
        print()

        #space_saving 
        # k para dar o numero de elementos a ver
        print("space saving k=",k)
        result,num = space_saving(folder_clean+file_use,k)
        result = sorted(result.items(),key=lambda x:x[1],reverse=True)
        print(result)
        print(num)
        print()

    return 0


if __name__ == "__main__":
   main()


