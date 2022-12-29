import random
from collections import Counter

single_points = {1: 100, 5: 50}
triple_points = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}


class GameLogic:
    def __init__(self):
        pass

    @staticmethod
    def calculate_score(tuple):
        dice_counts = Counter(tuple)

        if len(dice_counts) == 6:
            return 1500

        total = 0

        if len(dice_counts) == 3 and all(value == 2 for value in dice_counts.values()):
            return 1500

        for number, count in dice_counts.items():
            if count < 3:
                total += count * single_points.get(number, 0)
            elif count == 3:
                total += triple_points[number]
            elif count == 4:
                total += triple_points[number] * 2
            elif count == 5:
                total += triple_points[number] * 3
            elif count == 6:
                total += triple_points[number] * 4
        return total

    @staticmethod
    def roll_dice(dice):
        number_list = []
        for num in range(dice):
            roll = random.randint(1, 6)
            number_list.append(roll)
        number_list = tuple(number_list)
        return number_list

    @staticmethod
    def get_scorers(tuple):
        """
        INPUT >> Tuple - The dice list that was rolled
        OUPUT >> Tuple - Only the dices that are worth points
        """
        counts = Counter(tuple)

        # Straights
        if len(counts) == 6:
            return tuple

        # 3 Pairs
        if len(counts) == 3:
            if all(value == 2 for value in counts.values()):
                return tuple

        result = []

        for number, count in counts.items():
            if count >= 3:
                result += [number] * count
            elif number == 1 or number == 5:
                result += [number] * count

        return result

    @staticmethod
    def validate_keepers(roll, keepers):
        """
        INPUT >> - Tuple - the actual list of dices
                 - Tuple - The users choice
        OUTPUT >>  Boolean - True/False if user picked from the actual list
        """
        count1 = Counter(roll)
        count2 = Counter(keepers)

        for number, count in count2.items():
            if number not in count1:
                return False
            elif count > count1[number]:
                return False
        return True





