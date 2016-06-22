import sys

if (len(sys.argv) != 3):
    print "usage: python {} Filename NumberOfSteps".format(sys.argv[0])
    sys.exit()

data        = sys.argv[1]
steps       = sys.argv[2]

sampleinput = open (data, 'r')
sample      = sampleinput.readlines()

def initVertex(sample):
    "Create dataset of nodes with its name, points, and number of links."
    numberofNodes = int(sample[0].rstrip("\n"))
    node   = []             #Store node and its data
    links  = []             #Store where it links to
    
    for i in range(1, numberofNodes+1):
                            #Give each node a 'name', 'points', and' number of links'
        node.append({'Node':sample[i].rstrip("\n"), 'point': 100.0, 'link': 0})
        
        links.append([])    #Index corresponds to a node of origin of points
    
    for i in range(int(numberofNodes)+2, len(sample)):
        for chouten in range(len(node)):
            for index in range(len(sample[i])):
                if sample[i][index] == ' ':           #Indicate where the two nodes' names are
                    space = index
                if sample[i][index] == "\n":
                    end   = index
                
            sourseNode = sample[i][0:space]
            if sourseNode == node[chouten]['Node']:
                node[chouten]['link'] += 1            #Count number of links
                
                link = sample[i][space+1: end]
                links[chouten].append(link)           #Add vertex names where it links to
    
    return (node, links)

def splitPoints(node, links):
    "Distribute points to its linked vertices."
    distributed = []                            #Store distributed points
    
    for i in range(len(node)):
        distributed.append(0)                   #Received points
        #Calculate how much of its points a vertex will distribute to each link
        if node[i]['link']  != 0:
            node[i]['point'] = node[i]['point'] / node[i]['link']
    
    for i in range(len(links)):
        for x in range(len(node)):
            for y in range(len(links[i])):
                if links[i][y] == node[x]['Node']:      #Find linked nodes and give points
                    distributed[x] += node[i]['point']
                    distributed[x]  = round(distributed[x], 2)
    
    for i in range(len(node)):
        node[i]['point']   = distributed[i]      #Save in dict
        distributed[i]     = 0                   #Reset received points to 0
    
    return (node, links)

def repeatPoints (node, links, steps):
    "Repeats distribution of points for number of steps given."
    for i in range(int(steps)):
        points = splitPoints(node, links)
        node   = points[0]
    return node

def organiseData (node):
    "Returns a list of results with a node's name and its points."
    result = []
    for i in range(len(node)):
        result.append({node[i]['Node']: node[i]['point']})
    return result

node     = initVertex(sample)
repeated = repeatPoints(node[0], node[1], steps)
result   = organiseData(repeated)

print result