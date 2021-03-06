import sys, numpy, time

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
    
    for i in range(numberofNodes):                       #Takes in account for dangling node
        column = 0
        for j in range(numberofNodes):
            column += tensor[i][j]
        if column == 0:
            for j in range(numberofNodes):
                tensor[i][j] = 1.0                       #Fill in the elements with 1.0
    
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
        prevector = vector
        vector    = tensorMatrix * vector                #Multiply tensor to vector
    
    for i in range(len(vector)):
        vector[i] = round(vector[i], 2)                  #Round values to two decimal places
    
    return (vector, prevector)

def Check (vector, prevector):
    "Checks if the system has converged or not."
    difference = vector - prevector                      #Difference between vector and the previous one
    SUM = []
    for i in range(len(difference)):
        element = abs(int(difference[i]))
        SUM.append(element)
    SUM = sum(SUM)                                       #Sum of elements of difference
    
    if abs(SUM) <= 0.5:                                  #Condition for convergence
        print 'The result is or is close to converged final result.'
    else:
        print '''
        The number of iteration might not be enough, please try again with bigger number of steps.
        If this keeps popping up, then the result might be diverging.
        '''
    return SUM

start   = time.time()                                    #Start timer

initial = initTensor(sample)
answer  = Iteration(initial[0], initial[1], steps)

end     = time.time()                                    #End timer

time = end - start
print answer[0]                                          #Final vector
print "It took {} sec.".format(time)

check = Check(answer[0], answer[1])