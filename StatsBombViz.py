import numpy as np
import seaborn as sns
from CustomPitch import createVerticalPitch

def plot_sb_event_location(events_df, pitch_length = 120, pitch_width = 80, metric = 'yards', alpha = 0.7, event_colour = 'royalblue', pitch_theme='light', pitch_line_colour = 'black', ax_colour = 'white', figsize=(5, 10), figax=None):
    
    '''
    Plots StatsBomb event data on a vertical pitch using transformed vertical locations.
    
    Parameters:
        events_df (dataframe): event dataframe with x and y vertical locations 
        pitch_length (integer): length of pitch in yards
        pitch_width (integer): width of pitch in yards
        metric (string): specify distance metric, yards (or metres - not yet available)
        alpha (numeric): transparency of events, 0-1
        event_colour (string): colour of events
        pitch_theme (string): specify 'light' or 'dark' to auto set pitch and line colours
        pitch_line_colour (string): specify colour for pitch lines
        ax_colour (string): specify colour for axes background colour
        figsize (tuple): specify (width, height) of figure
        figax (tuple): specify previous (fig, ax) to start from
        
    '''
    
    
    fig,ax = createVerticalPitch(length=pitch_length, width=pitch_width, metric=metric, pitch_theme = pitch_theme, linecolor=pitch_line_colour, ax_colour = ax_colour, figsize = figsize, figax = figax) 
    for index, event in events_df.iterrows():
        x = event['vertical_location_x']
        y = event['vertical_location_y']
        ax.plot(x, y, 'ro', alpha = alpha)
    return fig,ax


def plot_sb_events(events_df, pitch_length = 120, pitch_width = 80, metric = 'yards', alpha = 0.7, event_colour = 'royalblue', pitch_theme='light', pitch_line_colour = 'black', ax_colour = 'white', figsize=(5, 10), figax=None):
    
    '''
    Plots StatsBomb event data on a vertical pitch using transformed vertical start and end locations.
    
    Parameters:
        events_df (dataframe): event dataframe with x and y vertical locations 
        pitch_length (integer): length of pitch in yards
        pitch_width (integer): width of pitch in yards
        metric (string): specify distance metric, yards (or metres - not yet available)
        alpha (numeric): transparency of events, 0-1
        event_colour (string): colour of events
        pitch_theme (string): specify 'light' or 'dark' to auto set pitch and line colours
        pitch_line_colour (string): specify colour for pitch lines
        ax_colour (string): specify colour for axes background colour
        figsize (tuple): specify (width, height) of figure
        figax (tuple): specify previous (fig, ax) to start from
        
    '''
    
    fig,ax = createVerticalPitch(length=pitch_length, width=pitch_width, metric=metric, pitch_theme = pitch_theme, linecolor=pitch_line_colour, ax_colour = ax_colour, figsize = figsize, figax = figax) 
    for index, event in events_df.iterrows():
        x_start = event['vertical_location_x']
        y_start = event['vertical_location_y']
        x_end = event['vertical_end_location_x']
        y_end = event['vertical_end_location_y']

        ax.annotate("", xy=(x_end, y_end), xytext = (x_start, y_start), alpha = alpha,
                    arrowprops = dict(alpha=alpha, arrowstyle="->", color = event_colour))
    
    return fig, ax



def plot_sb_events_clusters(events_df, clusters=4, pitch_length = 120, pitch_width = 80, metric = 'yards', pitch_theme = 'light', line_colour = 'black', ax_colour = 'white', alpha = 0.7, figsize = (5, 10), figax=None):
    
    '''
    Applies k-means clustering to events with given number of clusters.
    Then plots StatsBomb event data on a vertical pitch using transformed vertical start and end locations with random colours per cluster.
    
    Parameters:
        events_df (dataframe): event dataframe with x and y vertical locations
        clusters (integer): number of clusters to use for k-means
        pitch_length (integer): length of pitch in yards
        pitch_width (integer): width of pitch in yards
        metric (string): specify distance metric, yards (or metres - not yet available)
        alpha (numeric): transparency of events, 0-1
        event_colour (string): colour of events
        pitch_theme (string): specify 'light' or 'dark' to auto set pitch and line colours
        pitch_line_colour (string): specify colour for pitch lines
        ax_colour (string): specify colour for axes background colour
        figsize (tuple): specify (width, height) of figure
        figax (tuple): specify previous (fig, ax) to start from
        
    '''
    
    from ClusterEval import kmeans_cluster, cluster_colour_map
    
    cluster_labels = kmeans_cluster(events_df, clusters)
    label_colour = cluster_colour_map(cluster_labels, clusters)
    
    fig,ax = createVerticalPitch(length=pitch_length, width=pitch_width, metric=metric, pitch_theme = pitch_theme, linecolor=line_colour, ax_colour = ax_colour, figsize = figsize, figax = figax)
    
    cluster_colour=0
    for index, event in events_df.iterrows():
        x_start = event['vertical_location_x']
        y_start = event['vertical_location_y']
        x_end = event['vertical_end_location_x']
        y_end = event['vertical_end_location_y']
  
        ax.annotate("", xy=(x_end, y_end), xytext = (x_start, y_start), alpha = alpha,
                    arrowprops = dict(alpha=alpha, arrowstyle="->", color = label_colour[cluster_colour]))
        cluster_colour=cluster_colour+1
    
    return fig, ax, cluster_labels

def plot_individual_cluster_events(rows, cols, events_df, cluster_labels, sample_size = 5, pitch_length=120, pitch_width=80, pitch_theme = 'dark', line_colour='white', ax_colour = '#303030', event_colour='royalblue', figsize=(10, 16)):
    
    '''
    Creates figure and axes grid using specified rows x columns.
    Plots each cluster of StatsBomb event data on a separate pitch with specified number of sample events.
    
    Parameters:
        rows (integer): number of rows in axes grid 
        cols (integer): number of columns in axes grid
        events_df (dataframe): event dataframe with x and y vertical locations
        cluster_labels (list): list of labels assigned to each respective event
        sample_size (integer): number of sample events to plot on each axes
        pitch_length (integer): length of pitch in yards
        pitch_width (integer): width of pitch in yards
        metric (string): specify distance metric, yards (or metres - not yet available)
        alpha (numeric): transparency of events, 0-1
        event_colour (string): colour of events
        pitch_theme (string): specify 'light' or 'dark' to auto set pitch and line colours
        pitch_line_colour (string): specify colour for pitch lines
        ax_colour (string): specify colour for axes background colour
        figsize (tuple): specify (width, height) of figure
        
    '''
    import matplotlib.pyplot as plt
    import collections
                              
    fig, axs = plt.subplots(rows,cols, sharex = True, sharey = True, figsize = figsize)
    
    if pitch_theme == 'dark':
        fig.patch.set_facecolor('#303030')
    
    
    cluster_freq = collections.Counter(cluster_labels)
    cluster_sorted = list(zip(*cluster_freq.most_common()))[0]
    cluster_freq_sorted = list(zip(*cluster_freq.most_common()))[1]

    for ax, cluster, event_count in zip(axs.flat, cluster_sorted, cluster_freq_sorted):
        cluster_events = events_df[cluster_labels == cluster].sample(sample_size)
        createVerticalPitch(length=pitch_length, width=pitch_width, metric='yards', pitch_theme = pitch_theme, linecolor=line_colour, ax_colour = ax_colour, figsize = figsize, figax = (fig, ax))
        plot_sb_events(cluster_events, figax = (fig, ax), pitch_theme=pitch_theme, event_colour=event_colour)
        ax.set_title("Cluster " + str(cluster+1) + " - (" + str(event_count) + ")",
                     fontdict = dict(fontweight='bold',
                                     color='white'))
        ax.axis('off')
    plt.subplots_adjust()
    plt.tight_layout()
    
    return fig, axs


def marginal_dist_grid(x, y, ax, ax_x, ax_y, nbins = 6, grid_colour_map = 'Reds', bar_colour = 'Red'):
        
    '''
    Create a figure with three axes, 2D histogram with density plots along top and right side.
    
    Parameters:
        x (Series): horizontal, x locations of events
        y (Series): vertical, y locations of events
        ax (axes): ax for 2D histogram
        ax_x (axes): ax for density plot on top
        ax_y (axes): ax for density plot on right
        nbins (integer): number of bins for 2D histogram
        grid_colour_map (string): Matplotlib colour map
        bar_colour (string): colour of density plot bars
    ...
    ...
    
    '''
    # the hist grid
    ax.hist2d(x, y, bins=nbins, cmap = grid_colour_map)
    
    # the top distribution
    sns.distplot(x, color = bar_colour, ax=ax_x)
    ax_x.patch.set_alpha(0)
    ax_x.axis('off')
    # the right distribution
    sns.distplot(y, color=bar_colour, vertical=True, ax=ax_y)
    ax_y.patch.set_alpha(0)
    ax_y.axis('off')
    
    return ax, ax_x, ax_y
    

def plot_sb_event_grid_density_pitch(events_df, pitch_length = 120, pitch_width = 80, metric = 'yards', pitch_line_colour='black',spacing = 0.005, nbins = 6, grid_colour_map = 'Reds', bar_colour = 'Red', figsize=(5, 10)):

    '''
    Plot a 2D histogram of event locations with marginal density plots both vertically and horizontally.
    
    Parameters:
        events_df (dataframe): event dataframe with x and y vertical locations
        pitch_length (integer): length of pitch in yards
        pitch_width (integer): width of pitch in yards
        metric (string): specify distance metric, yards (or metres - not yet available)
        pitch_line_colour (string): specify colour for pitch lines
        nbins (integer): number of bins for 2D histogram
        grid_colour_map (string): Matplotlib colour map
        bar_colour (string): colour of density plot bars
        figsize (tuple): specify (width, height) of figure
        
    '''
    
    x = events_df['vertical_location_x']
    y = events_df['vertical_location_y']
    
    fig, ax = createVerticalPitch(pitch_length, pitch_width, metric, linecolor=pitch_line_colour, figsize = figsize)
    ax_pos = ax.get_position()

    left, width = ax_pos.x0, ax_pos.x1 - ax_pos.x0
    bottom, height = ax_pos.y0, ax_pos.y1 - ax_pos.y0

    rect_histx = [left, bottom + height + spacing, width, 0.1]
    rect_histy = [left + width + spacing, bottom, 0.2, height]

    ax_histx = fig.add_axes(rect_histx, sharex=ax)
    ax_histy = fig.add_axes(rect_histy, sharey=ax)

    ax, ax_x, ax_y = marginal_dist_grid(x, y, ax, ax_histx, ax_histy, nbins = nbins, grid_colour_map = grid_colour_map, bar_colour = bar_colour)

    return fig, ax, ax_x, ax_y

def plot_histogram_ratio_pitch(events_1, events_2, pitch_length=120, pitch_width=80, metric='yards', line_colour='black', nbins=6, grid_colour_map='RdBu', figsize=(5, 10)):
    '''
    Calculate and plot the ratio of two 2D histograms with specified number of bins.
    
    Parameters:
        events_1 (dataframe): event dataframe with x and y vertical locations
        events_2 (dataframe): event dataframe with x and y vertical locations
        pitch_length (integer): length of pitch in yards
        pitch_width (integer): width of pitch in yards
        metric (string): specify distance metric, yards (or metres - not yet available)
        pitch_line_colour (string): specify colour for pitch lines
        nbins (integer): number of bins for 2D histogram
        grid_colour_map (string): Matplotlib colour map
        figsize (tuple): specify (width, height) of figure
    '''  
    
    x1, y1 = events_1['vertical_location_x'], events_1['vertical_location_y']
    x2, y2 = events_2['vertical_location_x'], events_2['vertical_location_y']
    
    h1, xedges, yedges = np.histogram2d(x1, y1, bins=nbins)
    h2, xedges, yedges = np.histogram2d(x2, y2, bins=nbins)
    h = -1 * (h1 / h2)
    
    fig, ax = createVerticalPitch(pitch_length, pitch_width, metric, linecolor=line_colour, figsize = figsize)
    ax.pcolorfast(xedges, yedges, h.T, cmap=grid_colour_map)
    
    return fig, ax

