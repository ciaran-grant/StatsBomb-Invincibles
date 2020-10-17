from sklearn import metrics

def kmeans_cluster(events_df, clusters=4):
    
    '''
    Applies k-means clustering to events start and end vertical locations and returns cluster labels
    
    Parameter:
        events_df (dataframe): event dataframe with x and y vertical locations
        clusters (integer): number of clusters to use for k-means

    '''
    
    from sklearn.cluster import KMeans
    
    events_locations = events_df[['vertical_location_x', 'vertical_location_y', 'vertical_end_location_x', 'vertical_end_location_y']]
    
    kmeans = KMeans(n_clusters=clusters)
    kmeans.fit(events_locations)
    
    cluster_labels = kmeans.predict(events_locations)
    
    return cluster_labels


def cluster_colour_map(cluster_labels, clusters):
    
    '''
    Maps each cluster label to a random colour.
    
    Parameter:
        cluster_labels (list): list of assigned cluster labels
        clusters (integer): number of clusters to use for k-means

    '''
    
    import numpy as np
    
    cluster_colour_dict = {}
    
    for cluster in range(clusters):
        random_colour = np.random.rand(3,)
        cluster_colour_dict[cluster] = random_colour

    label_colour = [cluster_colour_dict[l] for l in cluster_labels]

    return label_colour


def cluster_evaluation(events_df, max_clusters):
    
    '''
    Applies k-means clustering to events start and end vertical locations using all numbers of clusters up to max_clusters.
    Cluster evaluation measures are calculated and stored in dataframe.
    
    Parameter:
        events_df (dataframe): event dataframe with x and y vertical locations
        max_clusters (integer): maximum number of clusters to evaluate for k-means

    '''
    
    import pandas as pd
    from sklearn.cluster import KMeans
    from sklearn import metrics
    
    events_locations = events_df[['vertical_location_x', 'vertical_location_y', 'vertical_end_location_x', 'vertical_end_location_y']]

    cluster_list = []
    ss_intertia_list = []
    silhouette_list = []
    ch_score_list = []
    db_score_list = []
    for n in range(2, max_clusters):
        kmeans = KMeans(n_clusters=n)
        kmeans.fit(events_locations)
        cluster_labels = kmeans.predict(events_locations)

        cluster_list.append(n)

        ss_intertia = kmeans.inertia_
        ss_intertia_list.append(ss_intertia)

        silhouette = metrics.silhouette_score(events_locations, cluster_labels, metric='euclidean')
        silhouette_list.append(silhouette)

        ch_score = metrics.calinski_harabasz_score(events_locations, cluster_labels)
        ch_score_list.append(ch_score)

        db_score = metrics.davies_bouldin_score(events_locations, cluster_labels)
        db_score_list.append(db_score)

    cluster_evaluation_dict = {'Clusters': cluster_list,
                               'Sum of Squares' : ss_intertia_list,
                               'Silhouette Coefficient' : silhouette_list,
                               'Calinski-Harabasz Index' : ch_score_list,
                               'Davies-Bouldin Index' : db_score_list}
    cluster_evaluation_df = pd.DataFrame(cluster_evaluation_dict)
    
    return cluster_evaluation_df


def plot_cluster_evaluation(cluster_evaluation_df):
    
    '''
    Plot cluster evaluation metrics in a 2x2 grid.
    
    Parameters:
        cluster_evaluation_df (dataframe): dataframe of cluster evaluation metrics from cluster_evaluation()

    ''' 
    
    import matplotlib.pyplot as plt
    
    fig, axs = plt.subplots(2, 2, figsize = (8, 8))
    axs[0,0].plot(cluster_evaluation_df['Clusters'], cluster_evaluation_df['Sum of Squares'])
    axs[0,0].set_title("Sum of Squares within Cluster")
    axs[0,1].plot(cluster_evaluation_df['Clusters'], cluster_evaluation_df['Silhouette Coefficient'])
    axs[0,1].set_title("Silhouette Coefficient")
    axs[1,0].plot(cluster_evaluation_df['Clusters'], cluster_evaluation_df['Calinski-Harabasz Index'])
    axs[1,0].set_title("Calinski-Harabasz Index")
    axs[1,1].plot(cluster_evaluation_df['Clusters'], cluster_evaluation_df['Davies-Bouldin Index'])
    axs[1,1].set_title("Davies-Bouldin Index")

    for ax in axs.flat:
        ax.set(xlabel='Clusters')
        ax.label_outer() 

    return fig, axs