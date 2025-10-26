from examples import *
from collections import defaultdict

def check_intervals2(graph): 

    print("Überlappungsprüfung:")

    top_index = {v: i for i, v in enumerate(graph.top_nodes)}

    connections = defaultdict(list)
    for v, w in graph.edges:
        connections[w].append(top_index[v])

    intervals = {}
    for w, indices in connections.items():
        intervals[w] = (min(indices), max(indices))

    def degree(node):
        return len(connections[node])

    def middle_edges(node):
        sorted_indices = sorted(connections[node])
        middle = sorted_indices[1:-1]
        return [(graph.top_nodes[i], node) for i in middle]

    def edges_cross(edge1, edge2):
        v1, w1 = edge1
        v2, w2 = edge2

        top_index = {v: i for i, v in enumerate(graph.top_nodes)}
        bottom_index = {w: i for i, w in enumerate(graph.bottom_nodes)}

        # Vergleiche Positionen der Kantenendpunkte
        return (top_index[v1] < top_index[v2] and bottom_index[w1] > bottom_index[w2]) or \
             (top_index[v1] > top_index[v2] and bottom_index[w1] < bottom_index[w2])

    for i in range(len(graph.bottom_nodes)):
        curr_node = graph.bottom_nodes[i]
        curr_interval = intervals[curr_node]

        group = [curr_node]

        for j in range(1, 4):
            if i + j >= len(graph.bottom_nodes):
                break
            next_node = graph.bottom_nodes[i + j]
            next_interval = intervals[next_node]

            if max(curr_interval[0], next_interval[0]) <= min(curr_interval[1], next_interval[1]):  # < oder <= ?
                group.append(next_node)
            else:
                break

        if len(group) == 1:
            print(f"{curr_node} hat KEINE Überlappung.")

        elif len(group) == 2:
            print(f"{group[0]} überlappt mit {group[1]}")

            #  Erweiterung für Fall 2 Knoten
            if degree(group[0]) >= 3 and degree(group[1]) >= 3:
                m1 = middle_edges(group[0])
                m2 = middle_edges(group[1])
                print(f"Mittlere Kanten von {group[0]}: {m1}")
                print(f"Mittlere Kanten von {group[1]}: {m2}")

                crossed = any(edges_cross(e1, e2) for e1 in m1 for e2 in m2)

                if crossed:
                    print(f"{group[0]} und {group[1]} müssen getauscht werden!")
                    # tauschen
                    idx1 = graph.bottom_nodes.index(group[0])
                    idx2 = graph.bottom_nodes.index(group[1])
                    graph.bottom_nodes[idx1], graph.bottom_nodes[idx2] = graph.bottom_nodes[idx2], graph.bottom_nodes[idx1]

                    # Neuprüfung nach Tausch
                    group = [graph.bottom_nodes[idx1], graph.bottom_nodes[idx2]]
                    m1 = middle_edges(group[1])
                    m2 = middle_edges(group[0])
                    crossed_again = any(edges_cross(e1, e2) for e1 in m1 for e2 in m2)

                    if crossed_again:
                        print("Mittlere Kanten schneiden sich weiterhin - keine Lösung möglich!")
                        break

        elif len(group) == 3:
            print(f"{group[0]}, {group[1]}, {group[2]} überlappen paarweise")

            int1 = intervals[group[0]]
            int2 = intervals[group[1]]  # mittlerer Knoten
            int3 = intervals[group[2]]

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

            # Erweiterung für Fall 3 Knoten
            if any(degree(node) >= 3 for node in group):
                middle_edges_dict = {node: middle_edges(node) for node in group}
                for node_mid in group:
                    mids = middle_edges_dict[node_mid]
                    others = [n for n in group if n != node_mid]
                    count_crosses = 0
                    for e_mid in mids:
                        for n in others:
                            for e in middle_edges_dict[n]:
                                if edges_cross(e_mid, e):
                                    count_crosses += 1
                        if count_crosses >= 1:  # 1 oder 2?
                            print(f"Kante von {node_mid} schneidet mittlere Kanten – keine Lösung möglich!")
                            return

        elif len(group) == 4:
            print(f"{group[0]}, {group[1]}, {group[2]}, {group[3]} überlappen paarweise")
            print("Kein 1+ real face 2-layer embedding möglich!")
            break

    return graph     


print("Graph 1:")
sorted_graph1 = sort(graph1)
check_intervals2(sorted_graph1)
print("")

print("Graph 2:")
sorted_graph2 = sort(graph2)
check_intervals2(sorted_graph2)
print("")

print("Graph 4_5:")
sorted_graph4_5 = sort(graph4_5)
check_intervals2(sorted_graph4_5)
print("")

print("Graph 5:")
sorted_graph5 = sort(graph5)
check_intervals2(sorted_graph5)
print("")

print("Graph 6:")
sorted_graph6 = sort(graph6)
check_intervals2(sorted_graph6)
print("")

print("Graph 7:")
sorted_graph7 = sort(graph7)
check_intervals2(sorted_graph7)
print("")

print("Graph 8:")
sorted_graph8 = sort(graph8)
check_intervals2(sorted_graph8)
print("")

print("Graph 9:")
sorted_graph9 = sort(graph9)
check_intervals2(sorted_graph9)
print("")

print("Graph 10:")
sorted_graph10 = sort(graph10)
check_intervals2(sorted_graph10)
print("")


