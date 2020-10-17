def ball_progression_events_into_thirds(events, x_min=0, y_min=0, x_max=80, y_max=120, x_pen_area=44, y_pen_area=18):

    '''
    Separates StatsBomb event data into thirds using vertical x, y locations.
    
    Parameters:
        events (dataframe): event dataframe with x and y vertical locations 
        x_min (integer): minimum x location
        y_min (integer): minimum y location
        x_max (integer): maximum x location
        y_max (integer): maximum y location
        x_pen_area (integer): penalty area x distance
        y_pen_area (integer): penalty area y distance

    '''
    y_final_third = y_max / 3
    y_own_third = y_max - y_final_third
    x_right_pen_area = x_max - ((x_max - x_pen_area) / 2)
    x_left_pen_area = x_min + ((x_max - x_pen_area) / 2)
         
    from_own_third = events[(events['vertical_location_y'] > y_own_third) & (events['vertical_end_location_y'] < y_own_third) &
                           (events['vertical_location_y'] - events['vertical_end_location_y'] > 10)]
    
    from_mid_third = events[(events['vertical_location_y'] < y_own_third) & (events['vertical_location_y'] > y_final_third) &
                           (events['vertical_end_location_y'] < y_final_third) & 
                           (events['vertical_location_y'] - events['vertical_end_location_y'] > 10)]
    
    from_final_third = events[(events['vertical_location_y'] < y_final_third) & (events['vertical_location_y'] > events['vertical_end_location_y'])]
    into_pen_area = events[(events['vertical_end_location_y'] < y_min + y_pen_area) & 
                           (events['vertical_end_location_x'] > x_left_pen_area) & 
                           (events['vertical_end_location_x'] < x_right_pen_area)]
    
    return from_own_third, from_mid_third, from_final_third, into_pen_area