% https://www.mathworks.com/help/fuzzy/gbellmf.html

x = 0:0.1:10;
y = gbellmf(x,[2 4 6]);

plot(x,y)
title('gbellmf, P=[2 4 6]')
xlabel('x')
ylabel('Degree of Membership')
ylim([-0.05 1.05])
