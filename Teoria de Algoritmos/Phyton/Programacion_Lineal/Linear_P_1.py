import pulp 

def ejemplo():
    #Vamos a crear variables x e y 
    x = pulp.LpVariable("x")
    y = pulp.LpVariable("y")
    problem = pulp.LpProblem("Producto",pulp.LpMaximize)
    problem += 3*x >= y
    problem += x+ 2*y <= 14
    problem += x-y <= 2
    problem += 5*x + 2*y 
    problem.solve()

    
    return pulp.value(x),pulp.value(y)

if __name__ == "__main__":
    x,y = ejemplo()
    print(x,y)