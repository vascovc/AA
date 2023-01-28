clear all
close all
clc

table = readtable("all_bad_exhaustive.csv");
edges = table.nodes;

%iteracoes
iter_0 = table.x0_iter_exhaustive;
iter_125 = table.x0_125_iter_exhaustive;
iter_25 = table.x0_25_iter_exhaustive;
iter_5 = table.x0_5_iter_exhaustive;
iter_75 = table.x0_75_iter_exhaustive;
iter_1 = table.x1_iter_exhaustive;

plot(edges,log(iter_0),'o')
title("Número de iterações ")
xlabel("Número de vértices")
ylabel("log(Número de iterações)")
axis tight
xlim([3 25])
hold on
plot(edges,log(iter_125),'+')
plot(edges,log(iter_25)','*')
plot(edges,log(iter_5)','square')
plot(edges,log(iter_75)','diamond')
plot(edges,log(iter_1)','x')

plot(edges,log( (edges.^2.*2.^(edges-3)) ),"-.")
plot(edges,log( (2.^edges) ),"-.")
plot(edges,log( (edges.^2) ),"-.")
plot(edges,log( (edges.*(log(edges))) ),"--")
legend(["k=0","k=0.125","k=0.25","k=0.5","k=0.75","k=1","n^2 2^{n-3}","2^n","n^2","nlog(n)"],'Location','northwest')
hold off
saveas(gcf,"figs/iteracoes_extra.png")

% tempo
figure(2)
time_0 = table.x0_time_exhaustive;
time_125 = table.x0_125_time_exhaustive;
time_25 = table.x0_25_time_exhaustive;
time_5 = table.x0_5_time_exhaustive;
time_75 = table.x0_75_time_exhaustive;
time_1 = table.x1_time_exhaustive;

plot(edges,log(time_0),'o')
title("Tempo de execução ")
xlabel("Número de vértices")
ylabel("log(Tempo execução)")
axis tight
xlim([3 25])
hold on
plot(edges,log(time_125)','+')
plot(edges,log(time_25),'*')
plot(edges,log(time_5)','square')
plot(edges,log(time_75),'diamond')
plot(edges,log(time_1)','x')
legend(["k=0","k=0.125","k=0.25","k=0.5","k=0.75","k=1"],'Location','northwest')
hold off
saveas(gcf,"figs/time_extra.png")

figure(3)
n_soluntions_0 = table.x0_number_of_solutions;
n_soluntions_125 = table.x0_125_number_of_solutions;
n_soluntions_25 = table.x0_25_number_of_solutions;
n_soluntions_5 = table.x0_5_number_of_solutions;
n_soluntions_75 = table.x0_75_number_of_solutions;
n_soluntions_1 = table.x1_number_of_solutions;

plot(edges,n_soluntions_0,'o')
title("Número de soluções")
xlabel("Número de vértices")
ylabel("Número de soluções possíveis")
axis tight
xlim([3 25])
hold on
plot(edges,n_soluntions_125','+')
plot(edges,n_soluntions_25,'*')
plot(edges,n_soluntions_5','square')
plot(edges,n_soluntions_75,'diamond')
plot(edges,n_soluntions_1','x')
legend(["k=0","k=0.125","k=0.25","k=0.5","k=0.75","k=1"],'Location','northwest')
hold off
saveas(gcf,"figs/n_solutions.png")