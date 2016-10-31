# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) K-Means Clustering Lab

## Introduction

We know what clustering is, how to setup your data for clustering, and how to evaluate your analysis.

For this lab session, we are going to complete a full k-means clustering process using Python. 

You're working for a large marketing agency as a data scientist, and we're trying to market a high-end luxury good to consumers. We know that we want to target consumers with large incomes, however we do not know anything else about the demographic makeup of our target market. You're given a [dataset](./assets/datasets/adult.csv) with census information on income size and various other demographic indicators.

Your task is to perform a cluster analysis of potential consumers, so we can better target our marketing efforts.

## Exercise

#### Requirements

- Import the data
- Format the data - we've been given some messy census data; your job is to make sense of it
- Perform K-means clustering with sklearn to reveal patterns in the consumer demographics
- Find inertia and silhouette scores for any clusterings you do
- Look at who is assigned to each cluster. Can you describe these groups qualitatively?

Just as in a real life scenario, the data and your analysis will not always be clear cut. While you may be wondering when you've succeeded in solving the problem, we're looking for your best recommendations based on the available data.

Work through the process until you and your partner have enough information to provide an analysis and recommendation to the agency.

#### Starter Code & Data

- Download the [data](./assets/datasets/adult.csv)
- Grab the [starter code](./code/starter-code/starter-code.ipynb) to get started. 

## Additional Resources

- A link to [K-Means Documentation](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
- Extra relevant [Silhoutte Score Documentation](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html)
