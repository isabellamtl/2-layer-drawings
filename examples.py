from sort import *
from facetest import *

# --------- Beispiele ------------

# 1: Intervall überlappt nicht und 2 Intervalle überlappen (möglich)
top1 = ['v1', 'v2', 'v3','v4','v5','v6', 'v7', 'v8', 'v9', 'v10']
bottom1 = ['w2', 'w1', 'w3']
edge1 = [
    ('v1','w1'),
    ('v2','w1'),
    ('v3','w1'),
    ('v4','w1'),
    ('v4','w2'),
    ('v5','w2'),
    ('v6','w2'),
    ('v8','w2'),
    ('v5','w3'),
    ('v7','w3'),
    ('v9','w3'),
    ('v10','w3'),
]

beispiel1 = BipartiteGraph(top1, bottom1, edge1)
beispiel1._draw_graph("Beispiel1")
sort(beispiel1)._draw_graph("Beispiel1_sorted")
print("Graph 1:")
check_intervals(beispiel1)._draw_graph("Beispiel1_final")
print("")

# 2: 2 Intervalle überlappen sich (möglich durch Tausch)
top2 = ['v1', 'v2', 'v3','v4','v5','v6', 'v7', 'v8']
bottom2 = ['w1', 'w2', 'w3']
edge2 = [
    ('v1','w1'),
    ('v5','w1'),
    ('v6','w1'),
    ('v2','w2'),
    ('v3','w2'),
    ('v4','w2'),
    ('v7','w2'),
    ('v6','w3'),
    ('v7','w3'),
    ('v8','w3'),
]

beispiel2 = BipartiteGraph(top2, bottom2, edge2)
beispiel2._draw_graph("Beispiel2")
sort(beispiel2)._draw_graph("Beispiel2_sorted")
print("Graph 2:")
check_intervals(beispiel2)._draw_graph("Beispiel2_final")
print("")

# 3: 2 Intervalle überlappen sich (nicht möglich, da mittlere Kanten sich schneiden)
top3 = ['v1', 'v2', 'v3','v4','v5','v6', 'v7', 'v8']
bottom3 = ['w1', 'w2']
edge3 = [
    ('v1','w1'),
    ('v4','w1'),
    ('v5','w1'),
    ('v2','w2'),
    ('v3','w2'),
    ('v6','w2'),
    ('v7','w2'),
    ('v8','w2'),
]

beispiel3 = BipartiteGraph(top3, bottom3, edge3)
beispiel3._draw_graph("Beispiel3")
sort(beispiel3)._draw_graph("Beispiel3_sorted")
print("Graph 3:")
check_intervals(beispiel3)._draw_graph("Beispiel3_final")
print("")

# 4: 4 Intervalle überlappen paarweise (nicht möglich)
top4 = ['v0','v1', 'v2', 'v3','v4','v5','v6', 'v7', 'v8', 'v9']
bottom4 = ['w1', 'w2', 'w3', 'w4', 'w5']
edge4 = [
    ('v0','w1'),
    ('v2','w1'),
    ('v1','w2'),
    ('v2','w2'),
    ('v5','w2'),
    ('v3','w3'),
    ('v5','w3'),
    ('v6','w3'),
    ('v7','w3'),
    ('v2','w4'),
    ('v8','w4'),
    ('v4','w5'),
    ('v9','w5'),
]

beispiel4 = BipartiteGraph(top4, bottom4, edge4)
beispiel4._draw_graph("Beispiel4")
sort(beispiel4)._draw_graph("Beispiel4_sorted")
print("Graph 4:")
check_intervals(beispiel4)._draw_graph("Beispiel4_final")
print("")

# 5: 2 mal 3 paarweise überlappende Intervalle (nicht möglich, da beim 2. Mal mittlerer Intervall in den äußeren liegt)
top5 = ['v1', 'v2', 'v3','v4','v5','v6', 'v7', 'v8']
bottom5 = ['w1', 'w2', 'w3', 'w4', 'w5']
edge5 = [
    ('v1','w1'),
    ('v3','w1'),
    ('v4','w1'),
    ('v2','w2'),
    ('v6','w2'),
    ('v4','w3'),
    ('v5','w3'),
    ('v3','w4'),
    ('v7','w4'),
    ('v8','w4'),
    ('v6','w5'),
    ('v8','w5'),
]

beispiel5 = BipartiteGraph(top5, bottom5, edge5)
beispiel5._draw_graph("Beispiel5")  
sort(beispiel5)._draw_graph("Beispiel5_sorted")
print("Graph 5:")
check_intervals(beispiel5)._draw_graph("Beispiel5_final")
print("")


# 6: 2 mal 3 paarweise überlappende Intervalle (möglich durch Tausch)
top6 = ['v1', 'v2', 'v3','v4','v5','v6', 'v7', 'v8', 'v9', 'v10']
bottom6 = ['w1', 'w2', 'w3', 'w4', 'w5', 'w6']
edge6 = [
    ('v1','w1'),
    ('v5','w1'),
    ('v2','w2'),
    ('v4','w2'),
    ('v3','w3'),
    ('v4','w3'),
    ('v5','w3'),
    ('v6','w3'),
    ('v6','w4'),
    ('v8','w4'),
    ('v7','w5'),
    ('v9','w5'),
    ('v6','w6'),
    ('v8','w6'),
    ('v10','w6'),
]

beispiel6 = BipartiteGraph(top6, bottom6, edge6)
beispiel6._draw_graph("Beispiel6")  
sort(beispiel6)._draw_graph("Beispiel6_sorted")
print("Graph 6:")
check_intervals(beispiel6)._draw_graph("Beispiel6_final")
print("")

# 7: 3 paarweise überlappende Intervalle (nicht möglich,
#mittlere Kante des mittleren Knotens außerhalb der andren Intervalle)
top7 = ['v1', 'v2', 'v3','v4','v5','v6', 'v7']
bottom7 = ['w1', 'w2', 'w3']
edge7 = [
    ('v1','w1'),
    ('v2','w1'),
    ('v3','w1'),
    ('v4','w1'),
    ('v2','w2'),
    ('v6','w2'),
    ('v7','w2'),
    ('v3','w3'),
    ('v5','w3'),
]

beispiel7 = BipartiteGraph(top7, bottom7, edge7)
beispiel7._draw_graph("Beispiel7")  
sort(beispiel7)._draw_graph("Beispiel7_sorted")
print("Graph 7:")
check_intervals(beispiel7)._draw_graph("Beispiel7_final")
print("")


# 8: 3 paarweise überlappende Intervalle (nicht möglich,
# mittlere Kanten schneiden sich)
top8 = ['v1', 'v2', 'v3','v4','v5','v6', 'v7', 'v8']
bottom8 = ['w1', 'w2', 'w3','w4']
edge8 = [
    ('v1','w1'),
    ('v2','w1'),
    ('v3','w1'),
    ('v2','w2'),
    ('v4','w2'),
    ('v6','w2'),
    ('v7','w2'),
    ('v3','w3'),
    ('v5','w3'),
    ('v6','w3'),
    ('v5','w4'),
    ('v7','w4'),
    ('v8','w4'),
]

beispiel8 = BipartiteGraph(top8, bottom8, edge8)
beispiel8._draw_graph("Beispiel8")  
sort(beispiel8)._draw_graph("Beispiel8_sorted")
print("Graph 8:")
check_intervals(beispiel8)._draw_graph("Beispiel8_final")
print("")

# 9: 3 paarweise überlappende Intervalle (nicht möglich,
# Mittlere Kante liegt in 3 Intervallen gleichzeitig)
top9 = ['v1', 'v2', 'v3','v4','v5','v6', 'v7', 'v8']
bottom9 = ['w1', 'w2', 'w3']
edge9 = [
    ('v1','w1'),
    ('v2','w1'),
    ('v3','w1'),
    ('v4','w1'),
    ('v6','w1'),
    ('v3','w2'),
    ('v4','w2'),
    ('v5','w2'),
    ('v7','w2'),
    ('v4','w3'),
    ('v6','w3'),
    ('v7','w3'),
    ('v8','w3'),
]

beispiel9 = BipartiteGraph(top9, bottom9, edge9)
beispiel9._draw_graph("Beispiel9")  
sort(beispiel9)._draw_graph("Beispiel9_sorted")
print("Graph 9:")
check_intervals(beispiel9)._draw_graph("Beispiel9_final")
print("")


# 10: Beispiel aus Einleitung
top10 = ['a', 'b', 'c','d','e','f', 'g', 'h', 'i']
bottom10 = ['u', 'v', 'w', 'x', 'y', 'z']
edge10 = [
    ('h','u'),
    ('i','u'),
    ('a','v'),
    ('b','v'),
    ('d','v'),
    ('c','w'),
    ('e','w'),
    ('f','w'),
    ('i','w'),
    ('a','x'),
    ('b','x'),
    ('c','x'),
    ('f','x'),
    ('g','y'),
    ('h','y'),
    ('e','z'),
    ('f','z'),
    ('g','z'),
]

beispiel10 = BipartiteGraph(top10, bottom10, edge10)
beispiel10._draw_graph("Beispiel10")  
sort(beispiel10)._draw_graph("Beispiel10_sorted")
print("Graph 10:")
check_intervals(beispiel10)._draw_graph("Beispiel10_final")
print("")