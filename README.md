CSCI 4144 Project Documentation
===

Team member 1: **Yucheng Liu**

Team member 2: **Yiying Zhang**

The program implements k-means algorithm based on the iris dataset, **iris_proc.data**. It contains two files: **kmeans.py** and **iris_kmeans.py**. The program produces a text file called **kmeans_result.txt**, which stores the accuracy results of 1000 tests.

The project was our team work originally shared on Dropbox in 2015. This reporsitory is just a transplant.


##Usage##
- - - -

To run the program, open a console and `cd` to the directory containing the program file.

Type in the command `python iris_kmeans.py`, and follow the instruction.

###Sample Output:###
		************************************
		Kmeans Classifer for Iris Data Set
		************************************
		
		
		Enter the file: iris_proc.data
		Data preprocessing done.
		Shuffle the data and start testing for 1000 times.
		
		Accuracy for iteration    1 is 0.5946
		Accuracy for iteration    2 is 0.0000
		Accuracy for iteration    3 is 0.1081
		Accuracy for iteration    4 is 0.0811
		Accuracy for iteration    5 is 0.4054
		Accuracy for iteration    6 is 0.4865
		Accuracy for iteration    7 is 0.4054
		Accuracy for iteration    8 is 0.0541
		Accuracy for iteration    9 is 0.0811
		Accuracy for iteration   10 is 0.0000
		Accuracy for iteration   11 is 0.3784
		Accuracy for iteration   12 is 0.4595
		Accuracy for iteration   13 is 0.0811
		Accuracy for iteration   14 is 0.0270
		Accuracy for iteration   15 is 0.0270
		Accuracy for iteration   16 is 0.9189
		Accuracy for iteration   17 is 0.4324
		Accuracy for iteration   18 is 0.8919
		                …
		Accuracy for iteration   992 is 0.3784
		Accuracy for iteration   993 is 0.1892
		Accuracy for iteration   994 is 0.3514
		Accuracy for iteration   995 is 0.4054
		Accuracy for iteration   996 is 0.0000
		Accuracy for iteration   997 is 0.9189
		Accuracy for iteration   998 is 0.2703
		Accuracy for iteration   999 is 0.4054
		Accuracy for iteration   1000 is 0.0000
		
		Overall Accuracy: 0.5627


##Structure##
- - - -

- **kmeans.py**：Implement k-means algorithm

   - `kmeanstrain()`: Train the program so that it finds the suitable clusters for the dataset

   - `kmeanstest()`: Classify the input test dataset

- **iris_kmeans.py**：apply k-means algorithm on the iris dataset, and build the user interface

   - `readFileName()`: Check and load the dataset


