import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def createVerticalPitch(length=120, width=80, metric='yards', pitch_theme = 'light', linecolor='black', ax_colour = 'white', figsize = (5, 10), figax = None):

    '''
    Creates a vertical football pitch.
    
    Parameters:
        pitch_length (integer): length of pitch in yards
        pitch_width (integer): width of pitch in yards
        metric (string): specify distance metric, yards (or metres - not yet available)
        pitch_theme (string): specify 'light' or 'dark' to auto set pitch and line colours
        linecolor (string): specify colour for pitch lines
        ax_colour (string): specify colour for axes background colour
        figsize (tuple): specify (width, height) of figure
        figax (tuple): specify previous (fig, ax) to start from
        
    '''
    
    
    if figax == None:
        #print("figax == None")
        fig = plt.figure(figsize = figsize)
        ax = fig.add_subplot(111)
        ax.xlim=(0, width)
        ax.ylim=(0, length)
    else:
        #print("fig, ax = figax")
        fig, ax = figax

    if pitch_theme == 'light':
        linecolor = 'black'
        ax_colour = 'white'
    elif pitch_theme == 'dark':
        linecolor = 'white'
        ax_colour = '#303030'
    
    ax.set_facecolor(ax_colour)
    
    #Pitch Outline & Centre Line
    ax.plot([0,width],[0,0], color=linecolor)
    ax.plot([0,0],[0,length], color=linecolor)
    ax.plot([0, width],[length, length], color=linecolor)
    ax.plot([width, width],[0, length], color=linecolor)
    ax.plot([0,width], [length/2,length/2], color=linecolor)

    #Bottom Penalty Area
    ax.plot([(width/2 +22),(width/2-22)],[18 ,18],color=linecolor)
    ax.plot([(width/2 +22),(width/2 +22)], [0,18],color=linecolor)
    ax.plot([(width/2 -22),(width/2 -22)],[18,0],color=linecolor)

    #Top Penalty Area
    ax.plot([(width/2 +22),(width/2 +22)],[(length-18),length],color=linecolor)
    ax.plot([(width/2 +22),(width/2-22)],[(length-18), (length-18)],color=linecolor)
    ax.plot([(width/2 -22),(width/2 -22)],[(length-18),length],color=linecolor)

    #Bottom 6-yard Box
    ax.plot([(width/2+7.32/2+6),(width/2+7.32/2+6)],[0,6],color=linecolor)
    ax.plot([(width/2+7.32/2+6),(width/2-7.32/2-6)],[6,6],color=linecolor)
    ax.plot([(width/2-7.32/2-6),(width/2-7.32/2-6)],[6,0],color=linecolor)

    #Top 6-yard Box
    ax.plot([(width/2+7.32/2+6),(width/2+7.32/2+6)],[length,length-6],color=linecolor)
    ax.plot([(width/2+7.32/2+6),width/2-7.32/2-6],[length-6,length-6],color=linecolor)
    ax.plot([(width/2-7.32/2-6),width/2-7.32/2-6],[length-6,length],color=linecolor)

    #Prepare Circles; 10 yards distance. penalty on 12 yards
    centreCircle = plt.Circle((width/2,length/2),10,color=linecolor,fill=False)
    centreSpot = plt.Circle((width/2,length/2),0.8,color=linecolor)
    bottomPenSpot = plt.Circle((width/2,12),0.8,color=linecolor)
    topPenSpot = plt.Circle((width/2,length-12),0.8,color=linecolor)

    #Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(bottomPenSpot)
    ax.add_patch(topPenSpot)

    #Prepare Arcs
    bottomArc = Arc((width/2,11),height=20,width=20,angle=0,theta1=48,theta2=132,color=linecolor)
    topArc = Arc((width/2,length-11,),height=20,width=20,angle=0,theta1=228,theta2=312,color=linecolor)

    #Draw Arcs
    ax.add_patch(bottomArc)
    ax.add_patch(topArc)

    #Tidy Axes
    #ax.axis('off')
    plt.xticks([])
    plt.yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    
    ax.set_aspect('equal')
    
    return fig,ax