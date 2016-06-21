import sys

if (len(sys.argv) != 2):
    print "usage: python {} filename".format(sys.argv[0])
    sys.exit()
filename = sys.argv[1]
sampleinput = open (filename, 'r')
sample = sampleinput.readlines()

numberofVertex = int(sample[0].rstrip("\n"))
numberofLinks = int(sample[numberofVertex+1].rstrip("\n"))

def initVertex(sample):
    "Create vertices with its name, points, number of links (in & out)."
    vertex = []
    links = []
    for i in range(1, numberofVertex+1):
        vertex.append({'Vertex':sample[i].rstrip("\n"), 'point': 100.0, 'link': 0, 'in': 0})
        links.append([])
    for i in range(int(numberofVertex)+2, len(sample)):
        for chouten in range(len(vertex)):
            if sample[i][0] == vertex[chouten]['Vertex']:
                vertex[chouten]['link'] += 1
                links[chouten].append(sample[i][2])
    return (vertex, links)

def splitPoints(vertex, links):
    for i in range(len(vertex)):
        vertex[i]['point'] = vertex[i]['point'] / vertex[i]['link']
    for i in range(len(links)):
        for x in range(len(vertex)):
            for y in range(len(links[i])):
                if links[i][y] == vertex[x]['Vertex']:
                    vertex[x]['in'] += vertex[i]['point']
    for i in range(len(vertex)):
        vertex[i]['point'] = vertex[i]['in']
        vertex[i]['in'] = 0
    return vertex

vertex = initVertex(sample)
points = splitPoints(vertex[0], vertex[1])