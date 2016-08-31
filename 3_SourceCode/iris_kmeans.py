import numpy as np
import kmeans

""" Load dataset and preprocess """
import os

helloMsg = "Kmeans Classifer for Iris Data Set";
print "*" * (len(helloMsg) + 2);
print "", helloMsg;
print "*" * (len(helloMsg) + 2);
print "\n";

def readFileName():
    fileName = raw_input("Enter the file: ");
    # Check if file exists
    if os.path.isfile(fileName) == False:
        print "File \"%s\" does not exist!" % fileName;
        fileName = readFileName();
    return fileName;

fileN = readFileName();
data_set = np.loadtxt(fileN,delimiter=',')
data_set[:,:4] = data_set[:,:4]-data_set[:,:4].mean(axis=0);
imax = np.concatenate((data_set.max(axis=0)*np.ones((1,5)),data_set.min(axis=0)*np.ones((1,5))),axis=0).max(axis=0);
data_set[:,:4] = data_set[:,:4]/imax[:4];

target = data_set[:,4];

print "\nData preprocessing done.\nShuffle the data and start testing for 1000 times.\n";

""" Test for 1000 times """
totalCount = 0;
accuracyAvg = 0;
for i in range(0, 1000):
    """ Randomly reorder the set """
    order = range(np.shape(data_set)[0]);
    np.random.shuffle(order);
    data_set = data_set[order,:];
    target = target[order];
    
    train = data_set[::2,0:4];
    traint = target[::2];
    valid = data_set[1::4,0:4];
    validt = target[1::4];
    test = data_set[3::4,0:4];
    testt = target[3::4];
    
    """ Train the dataset """
    km = kmeans.kmeans(3,train);
    km.kmeanstrain(train);
    cluster = km.kmeanstest(test);
    result = 1.*cluster;
    
    """ Count the number of correct tags """
    count = 0;
    
    for index, e in enumerate(result):
        if e[0] == data_set[3::4,4][index]:
            count += 1;
    accuracy = (count / (len(result) + 0.0));
    if accuracy > 0.3:
        accuracyAvg += accuracy;
        totalCount += 1;
    print "Accuracy for iteration %4d is %.4f" % (i+1, accuracy);
    
    """ Calculate the accuracy and write it to a file """
    with open("kmeans_result.txt", "a+b") as resultFile:
        resultFile.write(repr(accuracy) + "\n");
        if i == 999:
            resultFile.write("\n");

""" Check if the file is closed """
if resultFile.closed == False:
   resultFile.close();
print "\nOverall Accuracy: %.4f" % (accuracyAvg/totalCount);