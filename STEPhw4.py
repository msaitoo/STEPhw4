import sys

if (len(sys.argv) != 3):
    print "usage: python {} Filename NumberOfSteps".format(sys.argv[0])
    sys.exit()

data        = sys.argv[1]
steps       = sys.argv[2]

sampleinput = open (data, 'r')
sample      = sampleinput.readlines()

def initVertex(sample):
    "Create dataset of vertices with its name, points, and number of links."
    numberofVertex = int(sample[0].rstrip("\n"))
    vertex = []             #Store vertex and its data
    links  = []             #Store where it links to
    
    for i in range(1, numberofVertex+1):
                            #dict              'name',   'points',  'number of links'
        vertex.append({'Vertex':sample[i].rstrip("\n"), 'point': 100.0, 'link': 0})
        
        links.append([])    #Index corresponds to vertex of origin of points
    
    for i in range(int(numberofVertex)+2, len(sample)):
        for chouten in range(len(vertex)):
            for index in range(len(sample[i])):
                if sample[i][index] == ' ':         #Indicate where the two vertices names are
                    space = index
                if sample[i][index] == "\n":
                    end   = index
                
            sourseVertex = sample[i][0:space]
            if sourseVertex == vertex[chouten]['Vertex']:
                vertex[chouten]['link'] += 1        #Count number of links
                
                link = sample[i][space+1: end]
                links[chouten].append(link)         #Add vertex names where it links to
    
    return (vertex, links)

def splitPoints(vertex, links):
    "Distribute points to its linked vertices."
    distributed = []                            #Store distributed points
    
    for i in range(len(vertex)):
        distributed.append(0)                   #Received points
        #Calculate how much of its points a vertex will distribute to each link
        if vertex[i]['link'] != 0:
            vertex[i]['point'] = vertex[i]['point'] / vertex[i]['link']
    
    for i in range(len(links)):
        for x in range(len(vertex)):
            for y in range(len(links[i])):
                if links[i][y] == vertex[x]['Vertex']:      #Find linked vertex and give points
                    distributed[x] += vertex[i]['point']
                    distributed[x]  = round(distributed[x], 2)
    
    for i in range(len(vertex)):
        vertex[i]['point'] = distributed[i]     #Save in dict
        distributed[i]     = 0                  #Reset received points to 0
    
    return (vertex, links)

def repeatPoints (vertex, links, steps):
    "Repeats distribution of points for number of steps given."
    for i in range(int(steps)):
        points = splitPoints(vertex, links)
        vertex = points[0]
    return vertex

vertex = initVertex(sample)
result = repeatPoints(vertex[0], vertex[1], steps)

print result