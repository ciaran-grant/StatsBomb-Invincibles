# StatsBomb-Invincibles

## Project Overview:
Arsenal's Invincibles season is unique to the Premier League, they are the only team that has gone a complete 38 game season without losing. They're considered to be one of the best teams ever to play in the Premier League. Going a whole season without losing suggests they were at least decent at defending, to reduce or completely remove bad luck from ruining their perfect record. This project aims to look into how Arsenal's defence managed this. To do so training a model is not necessary as this is a descriptive task, not a predictive one. Instead, I will focus on answering the questions with data visualisations to effectively represent and communicate the answers to the questions.

Using StatsBomb's public event data for the Arsenal 03/04 season* (33 games), I take a look at where Arsenal's defensive actions take place and how opponents attempted to progress the ball and create chances against them.

The goal is to identify areas of Arsenal's defensive strengths and the frequent approaches used by opponents. Tasks involved are as follows:

1. Download and preprocess StatsBomb's event data
2. Explore and visualise Arsenal's defensive actions
3. Explore and visualise Opponent's ball progression by thirds
4. Cluster and evaluate Opponent's ball progressions using several clustering methods.
5. Visualise clustering results to aid understanding.
6. Cluster and evaluate Opponent's shot creations using several clustering methods.
7. Visualise clustering results to aid understanding

### Libraries

Below libraries and versions were used.

pandas==1.1.1
numpy==1.18.2
matplotlib==3.0.0
seaborn==0.10.0
scikit-learn==0.22.2

``` python
import json
from pandas.io.json import json_normalize
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics

from CustomPitch import createVerticalPitch
from StatsBombPrep import ball_progression_events_into_thirds
from StatsBombViz import plot_sb_events, plot_sb_event_location, plot_sb_events_clusters, plot_individual_cluster_events
from StatsBombViz import plot_sb_event_grid_density_pitch, plot_histogram_ratio_pitch
from ClusterEval import kmeans_cluster, agglomerative_cluster, cluster_colour_map, cluster_evaluation, plot_cluster_evaluation
```
### Project Details

The .ipynb and .html files here are an initial submission for the Capstone Project from the Udacity Data Scientist Nanodegree: https://www.udacity.com/course/data-scientist-nanodegree--nd025
 
Blog post for submission: 
 - https://thelastmananalytics.home.blog/2020/10/31/26-invincibles-defending-with-statsbomb-events-v3-0/

Archived blog submissions:
 - http://thelastmananalytics.home.blog/2020/10/19/26-invincibles-defending-with-statsbomb-events/
 - https://thelastmananalytics.home.blog/2020/10/22/26-invincibles-defending-with-statsbomb-events-v2-0/
 - https://thelastmananalytics.home.blog/2020/10/24/26-written-summary-invincibles-defending-with-statsbomb-events/

The data used is freely available through StatsBomb (https://statsbomb.com/academy/, https://github.com/statsbomb/open-data). 
1. Sign the user agreement
2. Download the data
3. Ensure filepath to data is accessible from Jupyter Notebook (place in same folder or add filepath using sys.append())

### Arsenal's Defence
![Arsenal Relative Defensive Events](/Plots/img5.png)

### Opponent Ball Progression
![Ball Progression Clusters - From Middle Third](/Plots/img11.png)
