clear all
close all
clc

table = readtable("projeto_2_all.csv");
table_p1 = readtable("all_projeto_1.csv");
nodes = table.nodes;
%iteracoes
iter_normal = table.x0_75_iter_generate;
iter_limit = table.x0_75_iter_generate_limit;
iter_2k = table.x0_75_iter_generate_2k;
iter_2n = table.x0_75_iter_generate_2n;
iter_greedy = table.x0_75_iter_greedy;

plot(nodes,log(iter_normal),'x',"Color",[0.9290 0.6940 0.750])
title("Número de iterações (0.75)")
xlabel("Número de vértices")
ylabel("log(Número de iterações)")
axis tight
xlim([3 30])
hold on
plot(nodes,log(iter_limit),'square',"Color",[0.8500 0.3250 0.0980])
plot(nodes,log(iter_2k),'*',"Color",[0.4660 0.6740 0.1880])
plot(nodes,log(iter_2n)','o',"Color",[0 0.4470 0.7410])
plot(nodes,log(iter_greedy)','+',"Color",[0.4940 0.1840 0.5560])

plot(nodes,log(2.^(nodes-3).*nodes.^2),"--","Color",[0.9290 0.6940 0.750])
plot(nodes,log((3/2).^nodes.*nodes.^2),"--","Color",[0.4660 0.6740 0.1880])
plot(nodes,log(nodes.^3),"--","Color",[0 0.4470 0.7410])
legend(["$p=0.15$","$\min{({n\choose k},1000)}$","$p=\frac{1}{2^k}$","$p=\frac{1}{2^n}$","\textit{Greedy}","$2^{n-3}n^2$","$\frac{3}{2}^{n}n^2$","$n^3$"],'Location','northwest',Interpreter='latex')
hold off
saveas(gcf,"figs/iteracoes_75.png")

%%%%%%%%%%%%%%%% tempo
time_normal = table.x0_75_time_generate;
time_limit = table.x0_75_time_generate_limit;
time_2k = table.x0_75_time_generate_2k;
time_2n = table.x0_75_time_generate_2n;
time_greedy = table.x0_75_time_greedy;
figure(2)
plot(nodes,log(time_normal),'x',"Color",[0.9290 0.6940 0.750])
title("Tempo de Execução (0.75)")
xlabel("Número de vértices")
ylabel("log(Tempo de Execução(s))")
axis tight
xlim([3 30])
hold on
plot(nodes,log(time_limit),'square',"Color",[0.8500 0.3250 0.0980])
plot(nodes,log(time_2k),'*',"Color",[0.4660 0.6740 0.1880])
plot(nodes,log(time_2n)','o',"Color",[0 0.4470 0.7410])
plot(nodes,log(time_greedy),'+',"Color",[0.4940 0.1840 0.5560])

legend(["$p=0.15$","$\min{({n\choose k},1000)}$","$p=\frac{1}{2^k}$","$p=\frac{1}{2^n}$","\textit{Greedy}"],'Location','northwest',Interpreter='latex')
hold off
saveas(gcf,"figs/time_75.png")
%%%%%%%%%%%%%%%% elementos descobertos
num_normal = table.x0_75_num_elementos_generate;
num_limit = table.x0_75_num_elementos_generate_limit;
num_2k = table.x0_75_num_elementos_generate_2k;
num_2n = table.x0_75_num_elementos_generate_2n;
num_greedy = table.x0_75_num_elementos_greedy;

num_exhaustive = table_p1.x0_75_num_elementos_exhaustive;
figure(3)
plot(nodes,num_normal,'x',"Color",[0.9290 0.6940 0.750])
title("Número de elementos (0.75)")
xlabel("Número de vértices")
ylabel("Tamanho do maior conjunto independente")
axis tight
xlim([3 28])
hold on
plot(nodes,num_limit,'square',"Color",[0.8500 0.3250 0.0980])
plot(nodes,num_2k,'*',"Color",[0.4660 0.6740 0.1880])
plot(nodes,num_2n,'o',"Color",[0 0.4470 0.7410])
plot(nodes,num_greedy,'+',"Color",[0.4940 0.1840 0.5560])
plot(table_p1.nodes,num_exhaustive,'diamond')

legend(["$p=0.15$","$\min{({n\choose k},1000)}$","$p=\frac{1}{2^k}$","$p=\frac{1}{2^n}$","\textit{Greedy}","Exaustivo"],'Location','northwest',Interpreter='latex')
hold off
saveas(gcf,"figs/elementos_75.png")
%%%%%%%%%%%%%%%% configuracoes testadas
confs_normal = table.x0_75_confs_tested_generate;
confs_limit = table.x0_75_confs_tested_generate_limit;
confs_2k = table.x0_75_confs_tested_generate_2k;
confs_2n = table.x0_75_confs_tested_generate_2n;
confs_greedy = table.x0_75_tries_greedy;
figure(4)
plot(nodes,log(confs_normal),'x',"Color",[0.9290 0.6940 0.750])
title("Número de Configurações testadas (0.75)")
xlabel("Número de vértices")
ylabel("log(Número de Conf.)")
axis tight
xlim([3 30])
hold on
plot(nodes,log(confs_limit),'square',"Color",[0.8500 0.3250 0.0980])
plot(nodes,log(confs_2k),'*',"Color",[0.4660 0.6740 0.1880])
plot(nodes,log(confs_2n),'o',"Color",[0 0.4470 0.7410])
plot(nodes,log(confs_greedy),'+',"Color",[0.4940 0.1840 0.5560])

legend(["$p=0.15$","$\min{({n\choose k},1000)}$","$p=\frac{1}{2^k}$","$p=\frac{1}{2^n}$","\textit{Greedy}"],'Location','northwest',Interpreter='latex')
hold off
saveas(gcf,"figs/confs_75.png")

%%%%%%%%%%%%%%%% basic operations
operations_normal = iter_normal+table.x0_75_tries_generate;
operations_limit = iter_limit+table.x0_75_tries_generate_limit;
operations_2k = iter_2k+table.x0_75_tries_generate_2k;
operations_2n = iter_2n+table.x0_75_tries_generate_2n;
operations_greedy = iter_greedy;
figure(5)
plot(nodes,log(operations_normal),'x',"Color",[0.9290 0.6940 0.750])
title("Operações básicas (0.75)")
xlabel("Número de vértices")
ylabel("log(Número de Ops.)")
axis tight
xlim([3 30])
hold on
plot(nodes,log(operations_limit),'square',"Color",[0.8500 0.3250 0.0980])
plot(nodes,log(operations_2k),'*',"Color",[0.4660 0.6740 0.1880])
plot(nodes,log(operations_2n),'o',"Color",[0 0.4470 0.7410])
plot(nodes,log(operations_greedy),'+',"Color",[0.4940 0.1840 0.5560])

legend(["$p=0.15$","$\min{({n\choose k},1000)}$","$p=\frac{1}{2^k}$","$p=\frac{1}{2^n}$","\textit{Greedy}"],'Location','northwest',Interpreter='latex')
hold off
saveas(gcf,"figs/tries_75.png")
