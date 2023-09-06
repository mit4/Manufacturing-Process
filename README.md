# Manufaturing Process

## Introduction

This data was taken from an actual production line near Detroit, Michigan. The goal is to predict certain properties of the line's output from the various input data. The line is a high-speed, continuous manufacturing process with parallel and series stages.

## Content

The data comes from one production run spanning several hours. Liveline Technologies has a large quantity of this type of data from multiple production lines in various locations.

## Challenge  

The data comes from a multi-stage continuous flow manufacturing process. In the first stage, Machines 1, 2, and 3 operate in parallel, and feed their outputs into a step that combines the flows. Output from the combiner is measured in 15 locations surrounding the outer surface of the material exiting the combiner.
[Click Here More details about dataset](data/raw/notes_on_dataset.txt)

> Primary Goal: Predict measurements of output from first stage.

Next, the output flows into a second stage, where Machines 4 and 5 process in series. After Machine 5, measurements are made again in the same 15 locations surrounding the outer surface of the material exiting Machine 5.

> Secondary Goal: Predict measurements of output from second stage.

## Data Description

Dataset Structure: The dataset is structured with a DateTime index and various columns representing different sensors, machine properties, and environmental conditions.

## Data Visualization

A collection of visualizations related to this dataset is accessible in the [reports/figures/plots](reports/figures/plots) directory. These visualizations aid in comprehending the dataset's characteristics and patterns.

## Features

 The dataset contains features such as ambient conditions (humidity and temperature), raw material properties, machine parameters, and output measurements from multiple stages.

## Feature Selection

Feature selection involves identifying and selecting the most relevant features for model building. This process will include:

## Exploratory Data Analysis (EDA) to understand feature distributions and relationships

Statistical tests and correlation analysis to identify key features.
Dimensionality reduction techniques if needed.
Model Tuning
Model tuning is crucial for achieving the best predictive performance. Key steps in this phase include:

## Splitting the dataset and Model tuning

- Selecting appropriate machine learning algorithms (e.g., XGBoost, Random Forest).
- Tuning hyperparameters using techniques like grid search or Bayesian optimization.
- Evaluating model performance using appropriate metrics (e.g., RMSE, MAE).
- Iteratively refining the models for better predictions.

## Conclusion

In conclusion, this project focuses on predicting measurements of the output from a complex multi-stage manufacturing process. Through data exploration, feature selection, and model tuning, we aim to develop accurate predictive models. The insights gained from this project can potentially improve process efficiency and reduce production errors, leading to significant benefits in the manufacturing industry.
