import sys

if (len(sys.argv) != 3):
    print "usage: python {} Filename NumberOfIteration".format(sys.argv[0])
    sys.exit()
data = sys.argv[1]
iteration = sys.argv[2]
sampleinput = open (data, 'r')
sample = sampleinput.readlines()

def initVertex(sample):
    "Create vertices with its name, points, and number of links."
    numberofVertex = int(sample[0].rstrip("\n"))
    vertex = []
    links = []
    
    for i in range(1, numberofVertex+1):
        vertex.append({'Vertex':sample[i].rstrip("\n"), 'point': 100, 'link': 0})
        links.append([])
    
    for i in range(int(numberofVertex)+2, len(sample)):
        for chouten in range(len(vertex)):
            if sample[i][0] == vertex[chouten]['Vertex']:
                vertex[chouten]['link'] += 1
                links[chouten].append(sample[i][2])
    
    return (vertex, links)

def splitPoints(vertex, links):
    "Distribute points to its linked vertices."
    distributed = []
    
    for i in range(len(vertex)):
        distributed.append(0)
        vertex[i]['point'] = vertex[i]['point'] / vertex[i]['link']
    
    for i in range(len(links)):
        for x in range(len(vertex)):
            for y in range(len(links[i])):
                if links[i][y] == vertex[x]['Vertex']:
                    distributed[x] += vertex[i]['point']
    
    for i in range(len(vertex)):
        vertex[i]['point'] = distributed[i]
        distributed[i] = 0
    
    return (vertex, links)

def repeatSplit (vertex, links, iteration):
    "Repeats splitting points."
    for i in range(int(iteration)):
        points = splitPoints(vertex, links)
        vertex = points[0]
    return vertex

vertex = initVertex(sample)
result = repeatSplit(vertex[0], vertex[1], iteration)

print result