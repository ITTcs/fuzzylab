x = 0:0.1:10;
y = trimf(x,[3 6 8]);
plot(x,y)
xlabel('trimf, P = [3 6 8]')
ylim([-0.05 1.05])