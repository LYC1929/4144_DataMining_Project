with open("accuracy_results.txt", "a+b") as resultFile:
    kmeans_accuracy = 0;
    mlp_accuracy = 0;
    rbf_accuracy = 0;
    with open("kmeans_result.txt", "r") as kmeans:
        contents = kmeans.readlines();
        count = 0;
        for e in contents:
            if (float(e) * 100) > 30:
                count += 1;
                kmeans_accuracy += float(e) * 100;
        resultFile.write("K-means Accuracy: " + repr(kmeans_accuracy/count) + "\n");
    
    with open("mlp_result.txt", "r") as mlp:
        mlp_contents = mlp.readlines();
        for e in mlp_contents:
            mlp_accuracy += float(e);
        resultFile.write("MLP Accuracy: " + repr(mlp_accuracy/len(mlp_contents)) + "\n");
    
    with open("rbf_result.txt", "r") as rbf:
        rbf_contents = rbf.readlines();
        for e in rbf_contents:
            rbf_accuracy += float(e) * 100;
        resultFile.write("RBF Accuracy: " + repr(rbf_accuracy/len(rbf_contents)) + "\n");
                