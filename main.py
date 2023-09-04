def padel_court_cost (court_type):
    if court_type == ('indoor'):
        return 30
    elif court_type == ('outdoor'):
        return 20
    

def rackets_cost (racket_brand):
    if rackets_cost == ('bullpadel'):
        return 100
    elif rackets_cost == ('nox'):
        return 140
    elif rackets_cost == ('siux'):
        return 200
    

def padel_balls_cost (ball_boxes):
    if padel_balls_cost == 1:
        return 2
    elif padel_balls_cost == 2:
        return 3.5
    elif padel_balls_cost == 3:
        return 5
    

def padel_game_cost():
    court_type = input("enter the court type (indoor/outdoor): ")
    racket_brand = input("enter the racket brand (bullpadel/nox/siux): ")
    ball_boxes = int(input("enter the number of ball boxes: "))

    court_cost = padel_court_cost(court_type)
    racket_cost = rackets_cost(racket_brand)
    balls_cost = padel_balls_cost(ball_boxes)
    game_cost = court_cost + racket_cost + balls_cost

    return padel_game_cost 
    
