from examples import *

def check_intervals(graph): 

    print("Überlappungsprüfung:")

    top_index = {v: i for i, v in enumerate(graph.top_nodes)}

    connections = defaultdict(list)
    for v, w in graph.edges:
        connections[w].append(top_index[v])

    intervals = {}
    for w, indices in connections.items():
        intervals[w] = (min(indices), max(indices))

    for i in range(len(graph.bottom_nodes)):
        curr_node = graph.bottom_nodes[i]
        curr_interval = intervals[curr_node]

        # Liste für überlappende Knoten
        group = [curr_node]

        for j in range(1, 4):  # prüfe die nächsten 3 Knoten
            if i + j >= len(graph.bottom_nodes):
                break
            next_node = graph.bottom_nodes[i + j]
            next_interval = intervals[next_node]

            # Prüfe Überlappung
            if max(curr_interval[0], next_interval[0]) <= min(curr_interval[1], next_interval[1]):
                group.append(next_node)
            else:
                break  # sobald kein Überlapp mehr, abbrechen

        # Jetzt je nach Gruppengröße Aktionen definieren
        if len(group) == 1:
            # ⚠️ KEINE Überlappung
            print(f"{curr_node} hat KEINE Überlappung.")
           

        elif len(group) == 2:
            # Überlappung mit i+1
            print(f"{group[0]} überlappt mit {group[1]}")
           
        elif len(group) == 3:
            # i, i+1, i+2 überlappen paarweise
            print(f"{group[0]}, {group[1]}, {group[2]} überlappen paarweise")

            int1 = intervals[group[0]]
            int2 = intervals[group[1]]  # mittlerer Knoten
            int3 = intervals[group[2]]

            # Prüfe, ob int2 komplett innerhalb von int1 und int3 liegt
            min_outer_start = max(int1[0], int3[0])
            max_outer_end = min(int1[1], int3[1])

            if int2[0] > min_outer_start and int2[1] < max_outer_end:
                print(f"Intervall von {group[1]} liegt innerhalb von {group[0]} und {group[2]}")
                print("Kein 1+ real face 2-layer embedding möglich!")
                break

            elif int1[0] < int3[0] and int3[0] < int2[0] and int2[0] < int1[1] and int1[1] < int2[1]:
                print(f"{group[1]} und {group[2]} müssen getauscht werden!")
                
            elif int1[0] < int2[0] and int2[0] < int3[0] and int3[0] < int2[1] and int2[1] < int1[1]:
                print(f"{group[0]} und {group[1]} müssen getauscht werden!")

        elif len(group) == 4:
            # i, i+1, i+2, i+3 überlappen paarweise
            print(f"{group[0]}, {group[1]}, {group[2]}, {group[3]} überlappen paarweise")
            print("Kein 1+ real face 2-layer embedding möglich!")
            break

    return graph     

print("Graph 1:")
sorted_graph1 = sort(graph1)
check_intervals(sorted_graph1)
print("")

print("Graph 2:")
sorted_graph2 = sort(graph2)
check_intervals(sorted_graph2)
print("")

#sorted_graph4 = sort(graph4)
#check_intervals(sorted_graph4)

print("Graph 4_5:")
sorted_graph4_5 = sort(graph4_5)
check_intervals(sorted_graph4_5)
print("")

print("Graph 5:")
sorted_graph5 = sort(graph5)
check_intervals(sorted_graph5)
print("")

print("Graph 6:")
sorted_graph6 = sort(graph6)
check_intervals(sorted_graph6)
print("")