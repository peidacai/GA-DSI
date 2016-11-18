


---
title: Data Science Triangle
type: exercise
duration: "2:00"
creator:
    name: Alexander Combs
    city: NYC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)  Data Science Triangle

This morning we are going to have a team-based competition. The goal is to create the best performing model on a hold-out sample of data. Simple right? 

Well, there is a catch. 

This will be a constrained optimization. To understand what that means, let's take a look at the Project Management Triangle.

# ![](http://www.joesdump.com/wp-content/uploads/2014/08/GoodFastCheap_Pick2.png)

The idea is that for any project you can have any two of these. You can have good work done cheap, but it will take a long time. You can have good work done fast, but it won't be cheap. Or you can have work done fast and on the cheap, but it won't be good. 

Today we will apply this concept to data science. 

You will be given a dataset and asked to pick two of the following: samples, features, algorithm. Here's how it will work. You will be given the training set and be required to decide which of the following you would like to choose for our competition:

### Team Samples 
- Your choice of algorithm
- Your choice of features
- **The other teams' choice of number of samples**

### Team Features
- Your choice of algorithm
- **The other teams' choice of which features**
- Your choice of samples

### Team Algorithm
- **The other teams' choice of algorithm**
- Your choice of features
- Your choice of samples

You should be aware that **other teams' options** while not the worst-case scenario, **will be highly unfavorable to you.**  Choose wisely.

Once you have made your selection, your team will have until 12pm to build the best model possible under those constraints.

There will be an award for the winning team. It will be favorable to you.

# ![](https://media.giphy.com/media/aL4bDxt8fbpy8/giphy.gif)

The feature data can be downloaded [here](./assets/data/X_train.csv) and the target can be downloaded [here](./assets/data/y_train.csv)

At noon, you will be given a holdout test set, you should return via email (alex.combs@ga.co) your predictions for each row in that set. This will simply be a csv with a single column of 1s and 0s _without a header_.

The task is to predict if a person's income is in excess of $50,000 given certain profile information.

Good luck!






