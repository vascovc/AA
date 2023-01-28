clear all
close all
clc

table = readtable("projeto_2_all.csv");
nodes = table.nodes;

time_normal_125 = table.x0_125_time_generate;
time_limit_125 = table.x0_125_time_generate_limit;
time_2k_125 = table.x0_125_time_generate_2k;
time_2n_125 = table.x0_125_time_generate_2n;
time_greedy_125 = table.x0_125_time_greedy;

time_normal_5 = table.x0_5_time_generate;
time_limit_5 = table.x0_5_time_generate_limit;
time_2k_5 = table.x0_5_time_generate_2k;
time_2n_5 = table.x0_5_time_generate_2n;
time_greedy_5 = table.x0_5_time_greedy;

time_normal_25 = table.x0_25_time_generate;
time_limit_25 = table.x0_25_time_generate_limit;
time_2k_25 = table.x0_25_time_generate_2k;
time_2n_25 = table.x0_25_time_generate_2n;
time_greedy_25 = table.x0_25_time_greedy;

time_normal_75 = table.x0_75_time_generate;
time_limit_75 = table.x0_75_time_generate_limit;
time_2k_75 = table.x0_75_time_generate_2k;
time_2n_75 = table.x0_75_time_generate_2n;
time_greedy_75 = table.x0_75_time_greedy;

time_normal_1 = table.x1_0_time_generate;
time_limit_1 = table.x1_0_time_generate_limit;
time_2k_1 = table.x1_0_time_generate_2k;
time_2n_1 = table.x1_0_time_generate_2n;
time_greedy_1 = table.x1_0_time_greedy;

time_normal = [time_normal_125 time_normal_25 time_normal_5 time_normal_75 time_normal_1];
time_normal = mean(time_normal,2);
time_limit = [time_limit_125 time_limit_25 time_limit_5 time_limit_75 time_limit_1];
time_limit = mean(time_limit,2);
time_2k = [time_2k_125 time_2k_25 time_2k_5 time_2k_75 time_2k_1];
time_2k = mean(time_2k,2);
time_2n = [time_2n_125 time_2n_25 time_2n_5 time_2n_75 time_2n_1];
time_2n = mean(time_2n,2);
time_greedy = [time_greedy_125 time_greedy_25 time_greedy_5 time_greedy_75 time_greedy_1];
time_greedy = mean(time_greedy,2);

figure(2)
plot(nodes,log(time_normal),'x',"Color",[0.9290 0.6940 0.50])
title("Tempo de Execução médio")
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
saveas(gcf,"figs/time_all_avg.png")
