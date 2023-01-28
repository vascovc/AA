clear all
close all
clc

table = readtable("all_faster_c.csv");
edges = table.nodes;

%iteracoes
iter_exhaustive = table.x0_iter_exhaustive;
iter_greedy = table.x0_iter_gridy;
iter_faster = table.x0_iter_exhaustive_faster;
iter_1_exhaustive = table.x1_iter_exhaustive;
iter_1_greedy = table.x1_iter_gridy;
iter_1_faster = table.x1_iter_exhaustive_faster;

plot(edges,log(iter_exhaustive),'x')
title("Número de iterações k=0 e k=1")
xlabel("Número de vértices")
ylabel("log(Número de iterações)")
axis tight
xlim([3 28])
hold on
plot(edges,log(iter_faster),'*')
plot(edges,log(iter_greedy)','o')
plot(edges,log(iter_1_exhaustive),'square')
plot(edges,log(iter_1_faster),'*')
plot(edges,log(iter_1_greedy)','o')
plot(edges,log( (edges.^2.*2.^(edges-3)) ),"-.")
plot(edges,log( (2.^edges) ),"-.")
plot(edges,log( (edges.^2) ),"-.")
plot(edges,log( (edges.*(log(edges))) ),"--")
legend(["Exaustiva(k=0)","E. Melhorada(k=0)","Greedy(k=0)","Exaustiva(k=1)","E. Melhorada(k=1)","Greedy(k=1)","n^2 2^{n-3}","2^n","n^2","nlog(n)"],'Location','northwest')
hold off
saveas(gcf,"figs/iteracoes.png")

% tempo
figure(2)
time_exhaustive = table.x0_time_exhaustive;
time_faster = table.x0_time_exhaustive_faster;
time_greedy = table.x0_time_gridy;
time_1_exhaustive = table.x1_time_exhaustive;
time_1_faster = table.x1_time_exhaustive_faster;
time_1_greedy = table.x1_time_gridy;

plot(edges,log(time_exhaustive),'x')
title("Tempo de execução k=0 e k=1")
xlabel("Número de vértices")
ylabel("log(Tempo execução)")
axis tight
xlim([3 28])
hold on
plot(edges,log(time_faster)','*')
plot(edges,log(time_greedy),'o')
plot(edges,log(time_1_exhaustive),'square')
plot(edges,log(time_1_faster)','*')
plot(edges,log(time_1_greedy),'o')
legend(["Exaustiva(k=0)","E. Melhorada(k=0)","Greedy(k=0)","Exaustiva(k=1)","E. Melhorada(k=1)","Greedy(k=1)"],'Location','northwest')
hold off
saveas(gcf,"figs/time.png")

%numero de elementos
figure(3)
num_exhaustive = table.x0_num_elementos_exhaustive;
num_faster = table.x0_num_elementos_exhaustive_faster;
num_greedy = table.x0_num_elementos_gridy;
num_1_exhaustive = table.x1_num_elementos_exhaustive;
num_1_faster = table.x1_num_elementos_exhaustive_faster;
num_1_greedy = table.x1_num_elementos_gridy;

plot(edges,num_exhaustive,'x')
title("Número de elementos k=0 e k=1")
xlabel("Número de vértices")
ylabel("Tamanho do maior conjunto de vértices independentes")
axis tight
xlim([3 28])
hold on
plot(edges,num_faster,'*')
plot(edges,num_greedy,'o')
plot(edges,num_1_exhaustive,'square')
plot(edges,num_1_faster,'*')
plot(edges,num_1_greedy,'o')
legend(["Exaustiva(k=0)","E. Melhorada(k=0)","Greedy(k=0)","Exaustiva(k=1)","E. Melhorada(k=1)","Greedy(k=1)"],'Location','northwest')
hold off
saveas(gcf,"figs/elementos.png")