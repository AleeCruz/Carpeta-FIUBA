%Vamos a ejecutar un programa muy corto que lo unico que hace es graficar
%Debemos de tener en cuenta que se debe de ejecutar correctamente para que esto duncion
f = @ (x) -3 *(x-2).^2.*(x+1)+2

a = -2
b = 3


x = a:0.1:b;



y = f(x)

plot (x,y,'r','LineWidth',2)

grid on
