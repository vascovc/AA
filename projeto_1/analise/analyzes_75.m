clear all
close all
clc

table = readtable("all.csv");
edges = table.nodes;

%iteracoes
iter_75_exhaustive = table.x0_75_iter_exhaustive;
iter_75_greedy = table.x0_75_iter_gridy;
iter_75_faster = table.x0_75_iter_exhaustive_faster;

plot(edges,log(iter_75_exhaustive),'x')
title("Número de iterações (0.75)")
xlabel("Número de vértices")
ylabel("log(Número de iterações)")
axis tight
xlim([3 28])
hold on
plot(edges,log(iter_75_faster),'*')
plot(edges,log(iter_75_greedy)','o')
plot(edges,log( (edges.^2.*2.^(edges-3)) ),"-.")
plot(edges,log( (2.^edges) ),"-.")
plot(edges,log( (edges.^2) ),"-.")
plot(edges,log( (edges.*(log(edges))) ),"--")
legend(["Exaustiva","E. Melhorada","Greedy","n^2 2^{n-3}","2^n","n^2","nlog(n)"],'Location','northwest')
hold off
saveas(gcf,"figs/iteracoes_75.png")

% tempo
figure(2)
time_75_exhaustive = table.x0_75_time_exhaustive;
time_75_faster = table.x0_75_time_exhaustive_faster;
time_75_greedy = table.x0_75_time_gridy;

plot(edges,log(time_75_exhaustive),'x')
title("Tempo de execução (0.75)")
xlabel("Número de vértices")
ylabel("log(Tempo execução)")
axis tight
xlim([3 28])
hold on
plot(edges,log(time_75_faster)','*')
plot(edges,log(time_75_greedy),'o')
legend(["Exaustiva","E. Melhorada","Greedy"],'Location','northwest')
hold off
saveas(gcf,"figs/time_75.png")

%numero de elementos
figure(3)
num_75_exhaustive = table.x0_75_num_elementos_exhaustive;
num_75_faster = table.x0_75_num_elementos_exhaustive_faster;
num_75_greedy = table.x0_75_num_elementos_gridy;

plot(edges,num_75_exhaustive,'x')
title("Número de elementos (0.75)")
xlabel("Número de vértices")
ylabel("Tamanho do maior conjunto de vértices independentes")
axis tight
xlim([3 28])
hold on
plot(edges,num_75_faster,'*')
plot(edges,num_75_greedy,'o')
legend(["Exaustiva","E. Melhorada","Greedy"],'Location','northwest')
hold off
saveas(gcf,"figs/elementos_75.png")