"""The Game of Hog."""

#Richard Wong
#Jason Shan


from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.

def max_Digit(num_rolls):
    str(num_rolls)
    max(num_rolls)
    return int(num_rolls)

def is_prime(score):
    if score <= 1:
        return False
    k = 2
    while k < n:
        if score % k == 0:
            return False
        k = k + 1
    return True

def next_prime(score):
    k = score
    while True:
        k = k + 1
        if is_prime(k):
            return k

def score_average(*args):
    n, total_score = num_samples, 0
    while (n>0):
        total_score = total_score + fn(*args)
        n = n - 1
    return total_score / num_samples


######################
# Phase 1: Simulator # 
def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 0.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN Question 1
   
    total = 0
    roll_outcome = 0
    did_roll_one = False

    for x in range (0, num_rolls):
        if (roll_outcome == 1): 
            did_roll_one = True
        else:
            total = total + 1

    if (did_roll_one == True):
        return 0

    return total

    # END Question 1


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN Question 2

    if num_rolls == 0:
        score = (max_Digit(opponent_score) + 1)
    else:
        score = roll_dice(num_rolls, dice)

    if(is_Prime(score) == True):
        return next_prime(score)

    # END Question 2


def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    # BEGIN Question 3
    if (score + opponent_score) % 7 == 0:
        return four_sided
    else: 
        return six_sided

    # END Question 3


def is_swap(score0, score1):
    """Returns whether the last two digits of SCORE0 and SCORE1 are reversed
    versions of each other, such as 19 and 91.
    """
    # BEGIN Question 4
    if str(score0) == str(score1)[::-1]:
        return True
    else:
        return False
    # END Question 4


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN Question 5
    while (score0<goal and score1<goal):
        if (who==0):
            scored=0
            num_dice=strategy0(score0,score1)
            scored=take_turn(num_dice,score1, select_dice(score0,score1))
            if (scored==0):
                score1+=num_dice
            score0+=scored
            if (is_swap(score0,score1)):
                temp=score0
                score0=score1
                score1=temp
        else:
            if (score0<goal and score1< goal):
                num_dice=strategy1(score1,score0)
                scored=take_turn(num_dice,score0, select_dice(score1,score0))
                if (scored==0):
                    score0+=num_dice
                score1+=scored
                
                if (is_swap(score0,score1)):
                    temp=score0
                    score0=score1
                    score1=temp
        if (who==0):
            who+=1
        else:
            who=0
    # END Question 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n

    return strategy


# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    5.5

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 0.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 5.5.
    Note that the last example uses roll_dice so the hogtimus prime rule does
    not apply.
    """
    # BEGIN Question 6
    return score_average
    # END Question 6


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN Question 7
    num_rolls=1
    highest=1
    highestAvg=0
    while (num_rolls<=10):
        tempAvg=make_averaged(roll_dice,num_samples)(num_rolls,dice)
        if tempAvg>highestAvg:
            highest=num_rolls
            highestAvg=tempAvg
        num_rolls+=1
    return highest
    # END Question 7


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    "*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 8
    maxDigitBacon = (max_Digit(opponent_score)+1)
    if is_Prime(maxDigitBacon) == True:
        maxDigitBacon = next_Prime(maxDigitBacon)
    if (maxDigitBacon >= margin):
        return 0
    return num_rolls
    return 5  # Replace this statement
    # END Question 8


def swap_strategy(score, opponent_score, num_rolls=5):
    """This strategy rolls 0 dice when it results in a beneficial swap and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 9
    maxDigitBacon=(max_Digit(opponent_score)+1)
    if (is_Prime(maxDigitBacon)):
        maxDigitBacon=next_Prime(maxDigitBacon)
    score+=maxDigitBacon
    if (score<opponent_score and is_swap(score,opponent_score)):
        return 0
    return 5  # Replace this statement
    # END Question 9


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN Question 10

    margin = 6
    if score==0:
        return 4
    hDig=highest_Digit(opponent_score)+1
    myhDig=highest_Digit(score)+1 
    if is_Prime(myhDig):
        myhDig=next_Prime(myhDig)   
    if is_Prime(hDig):
        hDig=next_Prime(hDig) 
    if ((score+hDig) < opponent_score and is_swap (score+hDig, opponent_score)): #Only benefit from swapping scors
        return swap_strategy (score, opponent_score)
    if (score<opponent_score and abs(opponent_score-swapped(score))<=10): #bait them into swapping
            if (opponent_score+abs(opponent_score-swapped(score))<100):
                return (abs(opponent_score-swapped(score)))  #I am in the lead
    if (myhDig>=margin):
        return 0
    if (score + opponent_score +hDig) % 7 == 0: #makes the opponent use a four sided dice on his turn
        return dont_Roll(score, opponent_score)
    if (hDig>= margin): #if my bacon rule is more than margin, 8, take 9 points instead
        if not (is_swap(hDig+score,opponent_score) and hDig+score>=opponent_score):
            return bacon_strategy(score, opponent_score) #Opponent is in the lead
    return 5
    # END Question 10


##########################
# Command Line Interface #
##########################


# Note: Functions in this section do not need to be changed. They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
