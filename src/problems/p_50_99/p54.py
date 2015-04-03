''' https://projecteuler.net/problem=54
(Note this has a corresponding solution document.)


'''

import os

from utility import start

DATA_FILE = os.path.join(start.DATA_PATH, 'p054_poker.txt')

def parse_datafile(data_file=DATA_FILE):
    """Return player 1's hands and player 2's hands
    
    Return ( ['5H', '5C', '6S', '7S', 'KD'], ...], [ ... ])"""
    
    player1_hands = []
    player2_hands = []
    with open(data_file) as f:
        for line in f:
            cards = line.split(' ')
            player1_hands.append(cards[:5])
            player2_hands.append(cards[-5:])
    
    return player1_hands, player2_hands


def score_hand(hand):
    '''Return poker hand ['5H', '5C', '6S', '7S', 'KD'] score (Score, c1, c2...)
    where c1, c2, ... are comparison values for two hands of the same Score
    
    Scores:
    - Royal Flush, 10
    - Straight Flush, 9 (see c1)
    - Four of a Kind, 8 (see c1)
    - Full House, 7, (see c1)
    - Flush, 6 (see c1, c2, c3, c4, c5)
    - Straight, 5 (see c1)
    - Three of a kind, 4 (see c1)
    - Two pairs, 3 (see c1, c2, c3)
    - One pair, 2 (see c1, c2, c3, c4)
    - High card, 1 (see c1, c2, c3, c4, c5)
    '''
    
    VALUES = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    chand = {} #{5: ['D'], 14: ['C', 'D']}, ie. card-value: [suit1, suit2, ...]
    for card in hand:
        number = card[0]
        suit = card[1]
        
        if number in VALUES:
            new_number = VALUES[number]
        else:
            new_number = int(number)
        
        if new_number in chand:
            chand[new_number].append(suit)
        else:
            chand[new_number] = [suit]
    
    # Biggest to smallest
    sorted_card_values = []
    for value, suits in chand.items():
        sorted_card_values.extend([value]*len(suits))
    sorted_card_values.sort(reverse=True) # Biggest to smallest
    
    def is_flush():
        '''Return if Royal Flush, Straight Flush or Flush'''
        # 5 Different values are necessary, and
        # Only one suit
        return (len(chand) == 5 and len(set(s[0] for s in chand.values())) == 1)
    
    def is_royal_flush():
        return (sorted_card_values == [14, 13, 12, 11, 10] and is_flush())
    
    def is_four_kind():
        '''Return value of four of a kind or False'''
        # Only two unique values, and
        # All four suits of 1 value
        if len(chand) == 2:
            for value, suits in chand.items():
                if len(suits) == 4:
                    return value
        
        return False
    
    def is_full_house():
        '''Return three-kind value of full house or False'''
        # Only two unique values, with one value having three suits
        if len(chand) == 2:
            for value, suits in chand.items():
                if len(suits) == 3:
                    return value
        
        return False
    
    def is_straight():
        '''Return if 5 cards in a row'''
        return all([sorted_card_values[i] - 1 == sorted_card_values[i + 1]
                    for i in range(4)])
    
    def is_three_kind():
        '''Return three-kind value or False'''
        # Three unique values, with one value having three suits
        if len(chand) == 3:
            for value, suits in chand.items():
                if len(suits) == 3:
                    return value
        
        return False
    
    def is_two_pairs():
        '''Return (Highest pair value, Lowest pair value, final) or False'''
        # Three unique values, with each value having two suits
        if len(chand) == 3:
            values = []
            for value, suits in chand.items():
                if len(suits) == 2:
                    values.append(value)
                else:
                    final_value = value
            
            if len(values) == 2:
                values.sort(reverse=True)
                values.append(final_value)
                return values
        
        return False
    
    def is_pair():
        '''Return [Pair value, highest value, next highest, ...] or False'''
        # Four unique values, exactly one has two suits
        if len(chand) == 4:
            highest_value = None
            remaining = []
            for value, suits in chand.items():
                if len(suits) == 2:
                    highest_value = value
                else:
                    remaining.append(value)
            
            if highest_value:
                remaining.sort(reverse=True)
                return [highest_value] + remaining
        
        return False
    
    # Partial optimisation by having two most common cases at front
    if len(chand) == 5 and not is_straight() and not is_flush():
        return [1] + sorted_card_values
    elif len(chand) == 4:
        return [2] + is_pair()
    elif is_royal_flush():
        return (10, )
    elif is_straight() and is_flush():
        return (9, sorted_card_values[0])
    elif is_four_kind():
        return (8, is_four_kind())
    elif is_full_house():
        return (7, is_full_house())
    elif is_flush():
        return [6] + sorted_card_values
    elif is_straight():
        return (5, sorted_card_values[0])
    elif is_three_kind():
        return (4, is_three_kind())
    elif is_two_pairs():
        return [3] + is_two_pairs()
        


def is_player1_winner(hand1, hand2):
    '''Return if Player 1 wins (player 1 is hand1)'''
    s1, s2 = (score_hand(hand1), score_hand(hand2))
    
    for i in range(len(s1)):
        if s1[i] > s2[i]:
            return True
        elif s1[i] < s2[i]:
            return False
            
    raise Exception("They are all equal!")


def p54():
    player1_hands, player2_hands = parse_datafile()
    player1_wins = [is_player1_winner(player1_hands[i], player2_hands[i])
                    for i in range(len(player1_hands))]
    return player1_wins.count(True)


if __name__ == '__main__':
    start.time_functions(p54)
