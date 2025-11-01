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

"""
# 11: Großes Beispiel, Abstand und Größe der Knoten in draw.py angepasst
top_nodes11 = ['v1', 'v2', 'v3','v4','v5','v6', 'v7', 'v8', 'v9', 'v10',
               'v11','v12','v13','v14','v15','v16','v17','v18','v19', 'v20', 'v21', 'v22', 'v23',
               'v24','v25','v26','v27']
bottom_nodes11 = [
    'w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w8', 'w9', 'w10',
    'w11', 'w12', 'w13', 'w14', 'w15', 'w16', 'w17', 'w18', 'w19', 'w20', 'w21', 'w22'
]
edges11 = [
    ('v1','w10'), ('v3','w10'),
    ('v1','w2'), ('v2','w2'), ('v4','w2'),
    ('v2','w21'), ('v4','w21'), ('v5','w21'),
    ('v5','w7'), ('v6','w7'),
    ('v4','w14'), ('v5','w14'), ('v6','w14'),
    ('v5','w5'), ('v6','w5'), ('v7','w5'),
    ('v6','w3'), ('v8','w3'),
    ('v7','w1'), ('v8','w1'), ('v9','w1'),('v10','w1'),
    ('v8','w9'), ('v9','w9'),
    ('v10','w19'), ('v12','w19'),
    ('v9','w13'), ('v10','w13'),('v11','w13'), ('v12','w13'),('v13','w13'), ('v14','w13'),
    ('v13','w12'), ('v15','w12'),
    ('v13','w4'), ('v16','w4'),
    ('v14','w11'), ('v17','w11'),('v16','w11'),
    ('v15','w8'), ('v18','w8'),('v16','w8'),
    ('v17','w6'), ('v18','w6'),
    ('v18','w15'), ('v19','w15'),('v20','w15'),
    ('v17','w18'), ('v19','w18'),
    ('v18','w22'), ('v22','w22'),
    ('v21','w20'), ('v25','w20'),('v26','w20'),
    ('v20','w17'), ('v23','w17'),('v19','w17'),
    ('v23','w16'), ('v24','w16'),('v27','w16'),('v25','w16')
]

beispiel11 = BipartiteGraph(top_nodes11, bottom_nodes11, edges11)
beispiel11._draw_graph("Beispiel11")  
sort(beispiel11)._draw_graph("Beispiel11_sorted")
print("Graph 11:")
check_intervals(beispiel11)._draw_graph("Beispiel11_final")
print("")
"""