% https://www.mathworks.com/help/fuzzy/trimf.html

x = 0:0.1:10;
y = trimf(x,[3 6 8]);

plot(x,y)
title('trimf, P = [3 6 8]')
xlabel('x')
ylabel('Degree of Membership')
ylim([-0.05 1.05])
