from unidecode import unidecode

def clean_text(file,dirty,clean):
    input = dirty+file
    output = clean+file
    dic = {}
    with open(input,"r", encoding='utf8') as inp:
        with open(output,"w") as out:
            line = inp.readline()
            begin = False # para se tentar limpar ao maximo aquela parte inicial
            while "End of the Project Gutenberg" not in line:
                line = inp.readline()
                if "End of the Project Gutenberg" in line:
                    begin = False
                if begin: #ja se pode ler tudo
                    for i in [*line.strip()]:
                        character = unidecode(i).upper()
                        if character.isalpha():
                            out.write(character)
                            if character in dic.keys():
                                dic[character] += 1
                            else:
                                dic[character] = 1
                if "*** START OF THIS PROJECT GUTENBERG EBOOK" in line:
                    begin = True
    print("done - "+file)
    for key, value in sorted(dic.items(), key=lambda x: x[0]): 
        print("{} : {}".format(key, value))
    print("letras - ",len(dic),'\n')
    return 0

def join_files(all_files,folder_clean,name):
    with open(folder_clean+name,'w') as outfile:
        for file in all_files:
            input = folder_clean + file
            with open(input) as infile:
                outfile.write(infile.read())
    return 0

def main():
    #fixo
    folder = "c:/Users/Vasco Costa/Documents/MEGAsync/4-1/AA/projeto_3/"
    #portatil
    #folder = "c:/Users/Vasco/Documents/MEGAsync/4-1/AA/projeto_3/"
    folder_dirty = folder+"original_txt/"
    folder_clean = folder+"clean_txt/"
    
    file_1 = "frei_luis.txt"
    clean_text(file_1,folder_dirty,folder_clean)
    file_2 = "camoes_lusiadas.txt"
    clean_text(file_2,folder_dirty,folder_clean)
    file_3 = "camoes_morte_d_ignez.txt"
    clean_text(file_3,folder_dirty,folder_clean)
    file_4 = "camoes_obras_completas_II.txt"
    clean_text(file_4,folder_dirty,folder_clean)
    file_5 = "camoes_obras_completas_III.txt"
    clean_text(file_5,folder_dirty,folder_clean)

    all_files = [file_2, file_3, file_4, file_5]
    join_files(all_files,folder_clean,"camoes_all.txt")

    file_a = "maias.txt"
    clean_text(file_a,folder_dirty,folder_clean)
    file_b = "reliquia.txt"
    clean_text(file_b,folder_dirty,folder_clean)
    all_files = ["camoes_all.txt",file_a,file_b]
    join_files(all_files,folder_clean,"all.txt")
    return 0


if __name__ == "__main__":
   main()


