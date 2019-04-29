import networkx as nx
import csv
import pickle
import matplotlib.pyplot as plt


# G.add_node(1, time='5pm')
# G.add_edges_from([(1, 2), (1, 3)])

if __name__ == '__main__':
    # with open('peopleblogs.csv', newline='') as csvfile:
    #     pbreader = csv.reader(csvfile)
    #     pblist = list(pbreader)
    #     with open('pblist.pkl', 'wb') as f:
    #         pickle.dump(pblist, f)

    with open('pblist.pkl', 'rb') as f:
        pb = pickle.load(f)
    del pb[0]

    G = nx.Graph()

    for row in pb:
        G.add_node(row[0], up=row[1], age=row[2], cat=row[3], len=row[4], views=row[5], rate=row[6], ratings=row[7], comm=row[8], numrel=row[9], ap=row[10])
        edge_list = []
        for relid in row[11:]:
            edge_list.append((row[0], relid))
        if len(edge_list) > 0:
            G.add_edges_from(edge_list)

    nx.write_gpickle(G, "g.gpickle")
    G2 = nx.read_gpickle("g.gpickle")
    print (G2)
