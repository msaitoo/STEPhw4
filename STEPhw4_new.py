import sys, numpy

if (len(sys.argv) != 3):
    print "usage: python {} Filename NumberOfSteps".format(sys.argv[0])
    sys.exit()

data        = sys.argv[1]
steps       = sys.argv[2]

sampleinput = open (data, 'r')
sample      = sampleinput.readlines()

def initTensor(sample):
    "Create initial colum vector and transformation matrix."
    numberofNodes = int(sample[0].rstrip("\n"))
    
    initVector = numpy.zeros((numberofNodes, 1))
    for i in range(numberofNodes):
        initVector[i] = 100
    
    node, links, linknumber   = [], [], []
    
    for i in range(1, numberofNodes+1):
        node.append(sample[i].rstrip("\n"))
        links.append([])
        linknumber.append(0)
    
    for i in range(int(numberofNodes)+2, len(sample)):
        for chouten in range(len(node)):
            for index in range(len(sample[i])):
                if sample[i][index] == ' ':
                    space = index
                if sample[i][index] == "\n":
                    end   = index
                
            sourseNode = sample[i][0:space]
            if sourseNode == node[chouten]:
                linknumber[chouten] += 1
                
                linkedNode = sample[i][space+1: end]
                for x in range(len(node)):
                    if linkedNode == node[x]:
                        links[chouten].append(x)
    
    tensor = numpy.zeros((numberofNodes, numberofNodes))
    for j in range(numberofNodes):
        for i in range(len(links[j])):
            tensor[links[j][i]][j] = 1.0/(linknumber[j])
    return (node, linknumber, links, tensor, initVector)   

def distributePoints(tensor, initVector):
    elements = []
    for i in range(len(tensor[0])):
        elements.append((tensor[i]))
    tensorMatrix = numpy.matrix(elements)
    
    Pointelements = []
    for i in range(len(initVector)):
        Pointelements.append((initVector[i]))
    initVector = numpy.matrix(Pointelements)
    
    return (tensorMatrix*initVector)

def repeatProcess(tensorMatrix, vector, steps):
    vector = distributePoints(initial[3], initial[4])
    
    for i in range(int(steps)):
        vector = tensorMatrix*vector
    
    for i in range(len(vector)):
        vector[i] = round(vector[i], 2)
    
    return vector

initial = initTensor(sample)
answer = repeatProcess(initial[3], initial[4], steps)
print answer