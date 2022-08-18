% https://www.mathworks.com/help/fuzzy/trapmf.html

x = 0:0.1:10;
y = trapmf(x,[1 5 7 8]);

plot(x,y)
title('trapmf, P = [1 5 7 8]')
xlabel('x')
ylabel('Degree of Membership')
ylim([-0.05 1.05])
