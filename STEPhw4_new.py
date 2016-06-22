import sys, numpy

if (len(sys.argv) != 3):
    print "usage: python {} Filename NumberOfSteps".format(sys.argv[0])
    sys.exit()

data        = sys.argv[1]               #Filename
steps       = sys.argv[2]               #Number of iteration

sampleinput = open (data, 'r')
sample      = sampleinput.readlines()

def initTensor(sample):
    "Create initial colum vector and transformation matrix."
    numberofNodes = int(sample[0].rstrip("\n"))
    
    initVector = numpy.zeros((numberofNodes, 1))
    for i in range(numberofNodes):
        initVector[i] = 100                              #Give starting value
    
    node, links = [], []                                 #Store node names and where it links to
    
    for i in range(1, numberofNodes+1):                  #Linked nodes
        node.append(sample[i].rstrip("\n"))
        links.append([])
    
    for i in range(int(numberofNodes)+2, len(sample)):
        for chouten in range(len(node)):
            for index in range(len(sample[i])):
                if sample[i][index] == ' ':
                    space = index
                if sample[i][index] == "\n":
                    end   = index
                
            sourseNode = sample[i][0:space]              #Indicate where node name is
            if sourseNode == node[chouten]:
                linkedNode = sample[i][space+1: end]     #Indicate where it links to
                
                for x in range(len(node)):
                    if linkedNode == node[x]:            #Store index of linked nodes
                        links[chouten].append(x)
    
    tensor = numpy.zeros((numberofNodes, numberofNodes)) #Create translation matrix
    for j in range(numberofNodes):
        for i in range(len(links[j])):
            tensor[links[j][i]][j] = 1.0/(len(links[j])) #Fraction of distribution
    
    return (tensor, initVector)

def makeMatrix(tensor, initVector):
    "Change arrays of tensor and initVector into matrices."
    Tensorelements = []
    for i in range(len(tensor[0])):
        Tensorelements.append((tensor[i]))
    tensorMatrix = numpy.matrix(Tensorelements)          #Make tensor into numpy matrix form
    
    Pointelements = []
    for i in range(len(initVector)):
        Pointelements.append((initVector[i]))
    vectorMatrix = numpy.matrix(Pointelements)           #Make colum array into numpy matrix form
    
    return (tensorMatrix * vectorMatrix)                 #Multiply two matrices

def Iteration(tensorMatrix, vector, steps):
    "Iterate multiplication of matrices for given number of steps"
    vector = makeMatrix(initial[0], initial[1])          #First iteration
    
    for i in range(int(steps)-1):
        vector = tensorMatrix * vector                   #Multiply tensor to vector
    
    for i in range(len(vector)):
        vector[i] = round(vector[i], 2)                  #Round values to two decimal places
    
    return vector

initial = initTensor(sample)
answer = Iteration(initial[0], initial[1], steps)
print answer