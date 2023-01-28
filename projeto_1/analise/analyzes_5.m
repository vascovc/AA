clear all
close all
clc

table = readtable("all.csv");
edges = table.nodes;

%iteracoes
iter_5_exhaustive = table.x0_5_iter_exhaustive;
iter_5_greedy = table.x0_5_iter_gridy;
iter_5_faster = table.x0_5_iter_exhaustive_faster;

plot(edges,log(iter_5_exhaustive),'x')
title("Número de iterações (0.5)")
xlabel("Número de vértices")
ylabel("log(Número de iterações)")
axis tight
xlim([3 28])
hold on
plot(edges,log(iter_5_faster),'*')
plot(edges,log(iter_5_greedy)','o')
plot(edges,log( (edges.^2.*2.^(edges-3)) ),"-.")
plot(edges,log( (2.^edges) ),"-.")
plot(edges,log( (edges.^2) ),"-.")
plot(edges,log( (edges.*(log(edges))) ),"--")
legend(["Exaustiva","E. Melhorada","Greedy","n^2 2^{n-3}","2^n","n^2","nlog(n)"],'Location','northwest')
hold off
saveas(gcf,"figs/iteracoes_5.png")

% tempo
figure(2)
time_5_exhaustive = table.x0_5_time_exhaustive;
time_5_faster = table.x0_5_time_exhaustive_faster;
time_5_greedy = table.x0_5_time_gridy;

plot(edges,log(time_5_exhaustive),'x')
title("Tempo de execução (0.5)")
xlabel("Número de vértices")
ylabel("log(Tempo execução)")
axis tight
xlim([3 28])
hold on
plot(edges,log(time_5_faster)','*')
plot(edges,log(time_5_greedy),'o')
legend(["Exaustiva","E. Melhorada","Greedy"],'Location','northwest')
hold off
saveas(gcf,"figs/time_5.png")

%numero de elementos
figure(3)
num_5_exhaustive = table.x0_5_num_elementos_exhaustive;
num_5_faster = table.x0_5_num_elementos_exhaustive_faster;
num_5_greedy = table.x0_5_num_elementos_gridy;


plot(edges,num_5_exhaustive,'x')
title("Número de elementos (0.5)")
xlabel("Número de vértices")
ylabel("Tamanho do maior conjunto de vértices independentes")
axis tight
xlim([3 28])
hold on
plot(edges,num_5_faster,'*')
plot(edges,num_5_greedy,'o')

legend(["Exaustiva","E. Melhorada","Greedy"],'Location','northwest')
hold off
saveas(gcf,"figs/elementos_5.png")