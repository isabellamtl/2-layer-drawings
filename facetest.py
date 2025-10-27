from sort import *
from collections import defaultdict
from collections import deque

def check_intervals(graph): 

    # Zuerst den Graphen sortieren
    graph = sort(graph)

    print("Überlappungsprüfung:")

    # Indizes der Top-Nodes
    top_index = {v: i for i, v in enumerate(graph.top_nodes)}

    # Zuordnung: bottom_node → Liste von Top-Node-Indizes
    connections = defaultdict(list)
    for v, w in graph.edges:
        connections[w].append(top_index[v])

    # Intervalle für Bottom-Nodes festlegen
    intervals = {}
    for w, indices in connections.items():
        intervals[w] = (min(indices), max(indices))

    # Funktion, die den Grad eines Knotens zurückgibt
    def degree(node):
        return len(connections[node])
    
    # Knoten, die nicht nochmal getauscht werden dürfen
    cant_be_swapped = defaultdict(bool)
    for w in graph.bottom_nodes:
        cant_be_swapped[w] = False

    # Funktion, die die Indizes der mittleren Kanten zurückgibt
    def middle_edges_indices(node):
        sorted_indices = sorted(connections[node])
        middle = sorted_indices[1:-1]
        return middle
    

    # Warteschlange für Bottom-Nodes, damit alle Knoten wirklich durchlaufen werden, auch wenn Tausch stattfindet
    queue = deque()
    queue.extend(graph.bottom_nodes)

    # Hauptschleife zur Überprüfung der Intervalle
    for _ in range(len(graph.bottom_nodes)-1):
        # Jeden Knoten nur einmal betrachten (außer den letzten)
        curr_node = queue.popleft()
        curr_interval = intervals[curr_node]

        # Gruppe von überlappenden Intervallen bilden
        group = [curr_node]

        # Überprüfen der nächsten 3 Knoten auf Überlappung, wenn vorhanden
        for j in range(1, 4):
            if graph.bottom_nodes.index(curr_node) + j < len(graph.bottom_nodes): #< + Einrückung -break
                
                next_node = graph.bottom_nodes[graph.bottom_nodes.index(curr_node) + j]
                next_interval = intervals[next_node]

                # Überlappung prüfen
                if max(curr_interval[0], next_interval[0]) < min(curr_interval[1], next_interval[1]):  
                    group.append(next_node)

            # Auf paarweise Überlappung prüfen am Ende der Schleife
            # Fall 1
            if j == 3 and len(group) == 4:
                intmid = intervals[group[2]] # vorletzter Knoten
                if not (max(intmid[0], next_interval[0]) < min(intmid[1], next_interval[1])):
                    group.pop()  # Letzten Knoten entfernen, wenn keine paarweise Überlappung
                    next_node = group[2]
                    next_interval = intervals[next_node]

            # Fall 2 (kann auch nach Fall 1 auftreten)
            if j == 3 and len(group) == 3:
                intmid = intervals[group[1]] # mittlerer Knoten
                int3 = intervals[group[2]] # letzter Knoten
                if not (max(intmid[0], int3[0]) < min(intmid[1], int3[1])):
                    group.pop()  # Letzten Knoten entfernen, wenn keine paarweise Überlappung
        
            
        # Intervall hat keine Überlappung
        if len(group) == 1:
            print(f"Intervall von {curr_node} hat KEINE Überlappung.")

        # 2 Intervalle überlappen 
        elif len(group) == 2:
            print(f"Intervall von {group[0]} überlappt mit dem von {group[1]}")

            m1 = middle_edges_indices(group[0])
            m2 = middle_edges_indices(group[1])
            
            # Fall, dass nur ein Knoten Grad ≥ 3 hat, mittler Kanten dürfen dann keine 2 Intervallgrenzen schneiden
            if degree(group[0]) >= 3 ^ degree(group[1]) >= 3:
                int1 = intervals[group[0]]
                int2 = intervals[group[1]]  
                if (max(m1, default= -1) > int2[1] or min(m2, default= float('inf')) < int1[0]):
                    print("Mittlere Kante liegt auf der anderen Seite des anderen Intervalls - keine Lösung möglich!")
                    break
               
            #  Mittlere Kanten überprüfen
            elif degree(group[0]) >= 3 and degree(group[1]) >= 3:
                print(f"Indizes der mittleren Kanten von {group[0]}: {m1}")
                print(f"Indizes der mittleren Kanten von {group[1]}: {m2}")

                if max(m1) <= min(m2):
                    print("Keine mittleren Kanten schneiden sich.")
                elif min(m1) >= max(m2):
                    print("Alle mittleren Kanten schneiden sich.")
                    print(f"{group[0]} und {group[1]} müssen getauscht werden!")
                    # Überprüfen, ob Tausch möglich
                    if cant_be_swapped[group[0]] or cant_be_swapped[group[1]]:
                        print("Tausch nicht möglich - keine Lösung möglich!")
                        break
                    else:
                        # tauschen
                        idx1 = graph.bottom_nodes.index(group[0])
                        idx2 = graph.bottom_nodes.index(group[1])
                        graph = graph.swap_bottom_nodes(idx1, idx2)
                        # Knoten dürfen nicht nochmal getauscht werden
                        cant_be_swapped[group[0]] = True
                        cant_be_swapped[group[1]] = True

                else: 
                    print("Es kommt in jedem Fall zu Kreuzungen - keine Lösung möglich!")
                    break

        # 3 Intervalle überlappen paarweise
        elif len(group) == 3:
            print(f"Intervalle von {group[0]}, {group[1]}, {group[2]} überlappen paarweise")

            # Intervalle
            int1 = intervals[group[0]]  # linker Knoten
            int2 = intervals[group[1]]  # mittlerer Knoten
            int3 = intervals[group[2]]  # rechter Knoten

            min_outer_start = max(int1[0], int3[0])
            max_outer_end = min(int1[1], int3[1])

            # Mittleres Intervall liegt komplett in den äußeren Intervallen
            if int2[0] > min_outer_start and int2[1] < max_outer_end:
                print(f"Intervall von {group[1]} liegt innerhalb von {group[0]} und {group[2]}")
                print("Kein 1+ real face 2-layer embedding möglich!")
                break

            # 1. Tausch-Fall
            elif int1[0] <= int3[0] and int3[0] <= int2[0] and int2[0] <= int1[1] and int1[1] <= int2[1]:
                print(f"{group[1]} und {group[2]} müssen getauscht werden!")
                # Überprüfen, ob Tausch möglich
                if cant_be_swapped[group[1]] or cant_be_swapped[group[2]]:
                    print("Tausch nicht möglich - keine Lösung möglich!")
                    break
                else:
                    # tauschen
                    idx1 = graph.bottom_nodes.index(group[1])
                    idx2 = graph.bottom_nodes.index(group[2])
                    graph = graph.swap_bottom_nodes(idx1, idx2)
                    # Knoten dürfen nicht nochmal getauscht werden
                    cant_be_swapped[group[1]] = True
                    cant_be_swapped[group[2]] = True
                    # Gruppenknoten aktualisieren
                    group[1], group[2] = group[2], group[1]

            # 2. Tausch-Fall
            elif int1[0] <= int2[0] and int2[0] <= int3[0] and int3[0] <= int2[1] and int2[1] <= int1[1]:
                print(f"{group[0]} und {group[1]} müssen getauscht werden!")
                # Überprüfen, ob Tausch möglich
                if cant_be_swapped[group[0]] or cant_be_swapped[group[1]]:
                    print("Tausch nicht möglich - keine Lösung möglich!")
                    break
                else:
                    # tauschen
                    idx1 = graph.bottom_nodes.index(group[0])
                    idx2 = graph.bottom_nodes.index(group[1])
                    graph = graph.swap_bottom_nodes(idx1, idx2)
                    # Knoten dürfen nicht nochmal getauscht werden
                    cant_be_swapped[group[0]] = True
                    cant_be_swapped[group[1]] = True
                    # Gruppenknoten aktualisieren
                    group[0], group[1] = group[1], group[0]

            # Erweiterung für Fall 3 Knoten
            # Intervalle neu festlegen, falls Gruppentausch stattfand   
            int1 = intervals[group[0]]
            int2 = intervals[group[1]]  
            int3 = intervals[group[2]]

            # Überprüfung der mittleren Kanten
            if any(degree(node) >= 3 for node in group):

                m1 = middle_edges_indices(group[0])
                m2 = middle_edges_indices(group[1])
                m3 = middle_edges_indices(group[2]) 

                # Mittlere Kanten dürfen sich nicht schneiden
                if max(m1, default= -1) > min(m2, default= float('inf')) or max(m2, default= -1) > min(m3, default= float('inf')):
                    print("Mittlere Kanten kreuzen sich - keine Lösung möglich!")
                    break
                # Mittlere Kanten der äußeren Knoten dürfen nicht in 3 Intervallen gleichzeitig liegen
                elif max(m1, default= -1) > int3[0] or min(m3, default= float('inf')) < int1[1]:
                    print("Mittlere Kanten liegen in 3 Intervallen - keine Lösung möglich!")
                    break
                # Mittlere Kanten des mittleren Knotens dürfen nicht außerhalb der äußeren Intervalle liegen
                elif min(m2, default= float('inf')) < int1[0] or max(m2, default= -1) > int3[1]:
                    print("Mittlere Kanten des mittleren Knotens liegen außerhalb der äußeren Intervalle - keine Lösung möglich!")
                    break
                # Mittlere Kanten des mittleren Knotens dürfen nicht in allen 3 Intervallen liegen
                for mid in m2:
                    if mid > int3[0] and mid < int1[1]:
                        print("Mittlere Kante des mittleren Knotens liegt in allen 3 Intervallen - keine Lösung möglich!")
                        return graph

        # 4 Intervalle überlappen paarweise                
        elif len(group) == 4:
            print(f"{group[0]}, {group[1]}, {group[2]}, {group[3]} überlappen paarweise")
            print("Kein 1+ real face 2-layer embedding möglich!")
            break

    return graph     



