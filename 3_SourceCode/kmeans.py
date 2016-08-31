""" Import numpy so that we can use built-in functions like ones(), etc. """
import numpy as np

class kmeans:
	""" The k-Means algorithm"""
	def __init__(self,k,data):

		self.nData = np.shape(data)[0]
		self.nDim = np.shape(data)[1]
		self.k = k
      
     
	def kmeanstrain(self,data,maxIterations=200):  # Use max iteration to avoid infinite loop
		
		""" Find the minimum and maximum values for each feature """
		minima = data.min(axis=0)
		maxima = data.max(axis=0)
	
		""" Pick the centroid locations randomly based on the minimas/maximas """
		self.centroids = np.random.rand(self.k,self.nDim)*(maxima-minima)+minima
		oldCentroids = np.random.rand(self.k,self.nDim)*(maxima-minima)+minima
	
		count = 0
		
		while np.sum(np.sum(oldCentroids-self.centroids))!= 0 and count<maxIterations:
	
			oldCentroids = self.centroids.copy()
			count += 1
	
			""" Compute distances """
			distances = np.ones((1,self.nData))*np.sum((data-self.centroids[0,:])**2,axis=1)
			for j in range(self.k-1):
				distances = np.append(distances,np.ones((1,self.nData))*np.sum((data-self.centroids[j+1,:])**2,axis=1),axis=0)
	
			""" Identify the closest cluster based on their Euclidean distance """
			cluster = distances.argmin(axis=0)
			cluster = np.transpose(cluster*np.ones((1,self.nData)))
	
			""" Update the cluster centroids """
			for j in range(self.k):
				currCluster = np.where(cluster==j,1,0)
				if sum(currCluster)>0:
					self.centroids[j,:] = np.sum(data*currCluster,axis=0)/np.sum(currCluster)
		return self.centroids
	
        """ Function to use the trained parameters to classify datasets """
	def kmeanstest(self,data):
		
		nData = np.shape(data)[0]
		""" Compute distances """
		distances = np.ones((1,nData))*np.sum((data-self.centroids[0,:])**2,axis=1)
		for j in range(self.k-1):
			distances = np.append(distances,np.ones((1,nData))*np.sum((data-self.centroids[j+1,:])**2,axis=1),axis=0)
	
		""" Identify the closest cluster """
		cluster = distances.argmin(axis=0)
		cluster = np.transpose(cluster*np.ones((1,nData)))
	
		return cluster
