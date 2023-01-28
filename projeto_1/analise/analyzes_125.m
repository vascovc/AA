clear all
close all
clc

table = readtable("all.csv");
edges = table.nodes;

%iteracoes
iter_125_exhaustive = table.x0_125_iter_exhaustive;
iter_125_greedy = table.x0_125_iter_gridy;
iter_125_faster = table.x0_125_iter_exhaustive_faster;

plot(edges,log(iter_125_exhaustive),'x')
title("Número de iterações (0.125)")
xlabel("Número de vértices")
ylabel("log(Número de iterações)")
axis tight
xlim([3 28])
hold on
plot(edges,log(iter_125_faster),'*')
plot(edges,log(iter_125_greedy)','o')
plot(edges,log( (edges.^2.*2.^(edges-3)) ),"-.")
plot(edges,log( (2.^edges) ),"-.")
plot(edges,log( (edges.^2) ),"-.")
plot(edges,log( (edges.*(log(edges))) ),"--")
legend(["Exaustiva","E. Melhorada","Greedy","n^2 2^{n-3}","2^n","n^2","nlog(n)"],'Location','northwest')
hold off
saveas(gcf,"figs/iteracoes_125.png")

% tempo
figure(2)
time_125_exhaustive = table.x0_125_time_exhaustive;
time_125_faster = table.x0_125_time_exhaustive_faster;
time_125_greedy = table.x0_125_time_gridy;

plot(edges,log(time_125_exhaustive),'x')
title("Tempo de execução (0.125)")
xlabel("Número de vértices")
ylabel("log(Tempo execução)")
axis tight
xlim([3 28])
hold on
plot(edges,log(time_125_faster)','*')
plot(edges,log(time_125_greedy),'o')
legend(["Exaustiva","E. Melhorada","Greedy"],'Location','northwest')
hold off
saveas(gcf,"figs/time_125.png")

%numero de elementos
figure(3)
num_125_exhaustive = table.x0_125_num_elementos_exhaustive;
num_125_faster = table.x0_125_num_elementos_exhaustive_faster;
num_125_greedy = table.x0_125_num_elementos_gridy;

plot(edges,num_125_exhaustive,'x')
title("Número de elementos (0.125)")
xlabel("Número de vértices")
ylabel("Tamanho do maior conjunto de vértices independentes")
axis tight
xlim([3 28])
hold on
plot(edges,num_125_faster,'*')
plot(edges,num_125_greedy,'o')
legend(["Exaustiva","E. Melhorada","Greedy"],'Location','northwest')
hold off
saveas(gcf,"figs/elementos_125.png")