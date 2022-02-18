from csp import Constraint,CSP
class MapColoringConstraint(Constraint):
    def __init__(self,place1,place2):
        super().__init__([place1,place2])
        self.place1 = place1
        self.place2 = place2
    def satisfied(self,assignment):
        if self.place1 not in assignment or self.place2 not in assignment:
            return True
        return assignment[self.place1] != assignment[self.place2]

if __name__ == "__main__":
    file = open('states.txt')
    strings = file.read().split('\n')
    variables = strings[0].split(',')
    colors = strings[1].split(',')
    #variables = ["Западная Австралия","Южная Австралия","Северная Территория",
                #"Квинсленд","Новый Южный Уэльс","Виктория","Тасмания"]

    domains = {}
    for variable in variables:
        domains[variable] = colors
    csp = CSP(variables,domains)
    for t in strings[2:len(strings)-1]:
        gran = t.split(' - ')
        print(gran[0],gran[1])
        csp.add_constraint(MapColoringConstraint(gran[0],gran[1]))

    '''
    csp.add_constraint(MapColoringConstraint("Западная Австралия","Южная Австралия"))
    csp.add_constraint(MapColoringConstraint("Южная Австралия","Северная Территория"))
    csp.add_constraint(MapColoringConstraint("Северная Территория","Квинсленд"))
    csp.add_constraint(MapColoringConstraint("Квинсленд","Южная Австралия"))
    csp.add_constraint(MapColoringConstraint("Квинсленд","Новый Южный Уэльс"))
    csp.add_constraint(MapColoringConstraint("Новый Южный Уэльс","Южная Австралия"))
    csp.add_constraint(MapColoringConstraint("Виктория","Южная Австралия"))
    csp.add_constraint(MapColoringConstraint("Виктория","Новый Южный Уэльс"))
    csp.add_constraint(MapColoringConstraint("Виктория","Тасмания"))
    '''
    solution = csp.backtracking_search()
    if solution is None:
        print("NO")
    else:
        print(solution)