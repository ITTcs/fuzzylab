% https://www.mathworks.com/help/fuzzy/defuzzification-methods.html

x = 0:0.1:20;

mf1 = trapmf(x,[0 2 8 12]);
mf2 = trapmf(x,[5 7 12 14]);
mf3 = trapmf(x,[12 13 18 19]);
mf = max(0.5*mf2,max(0.9*mf1,0.1*mf3));

plot(x,mf,'LineWidth',3)
ylim([-1 1])

xCentroid = defuzz(x,mf,'centroid');
xBisector = defuzz(x,mf,'bisector');
xMOM = defuzz(x,mf,'mom');
xSOM = defuzz(x,mf,'som');
xLOM = defuzz(x,mf,'lom');

hCentroid = line([xCentroid xCentroid],[-0.2 1.2],'Color','k'); 
tCentroid = text(xCentroid,-0.2,' centroid','FontWeight','bold');
hBisector = line([xBisector xBisector],[-0.4 1.2],'Color','k'); 
tBisector = text(xBisector,-0.4,' bisector','FontWeight','bold');
hMOM = line([xMOM xMOM],[-0.7 1.2],'Color','k'); 
tMOM = text(xMOM,-0.7,' MOM','FontWeight','bold');
hSOM = line([xSOM xSOM],[-0.7 1.2],'Color','k'); 
tSOM = text(xSOM,-0.7,' SOM','FontWeight','bold');
hLOM = line([xLOM xLOM],[-0.7 1.2],'Color','k'); 
tLOM = text(xLOM,-0.7,' LOM','FontWeight','bold');

gray = 0.7*[1 1 1];

hBisector.Color = gray;
tBisector.Color = gray;
hCentroid.Color = 'red';
tCentroid.Color = 'red';
hMOM.Color = gray;
tMOM.Color = gray;
hSOM.Color = gray;
tSOM.Color = gray;
hLOM.Color = gray;
tLOM.Color = gray;
