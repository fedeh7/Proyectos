"""Play Bulls and Cows."""
import random
NUM_DIGITS = 5

class IllegalNumber(Exception):
    """An exception to raise when the class Num has an instance of an
    illegal number."""
    pass

class Num(object):
    """Represent a number that consists of different NUM_DIGITS digits.
    n -- a representation of the number (int, str or a
          sequence of digits)."""
    def __init__(self, n):
        self.num = tuple(int(d) for d in str(n)) if isinstance(n, (int, str)) \
            else tuple(int(d) for d in n)  # convert n into a tuple of digits
        if not self._is_legal():
            raise IllegalNumber

    def _is_legal(self):
        if len(self.num) != NUM_DIGITS:
            return False
        if len(set(self.num)) < NUM_DIGITS: # Does it contain equal digits?
            return False
        if self.num[0] == 0:
            return False
        if not all(0 <= d <= 9 for d in self.num):
            return False
        return True

    def __str__(self):
        return ''.join(str(d) for d in self.num)

    def compare(self, other):
        """If one number was A's secret number and the second one
        was B's guess, how many bulls and cows are there? Return
        them in a (bulls, cows) tuple representation.

        >>> Num(1234).compare(Num(5243)) ==> 1, 2
        """
        bulls, cows = 0, 0
        for i in xrange(NUM_DIGITS):
            if self.num[i] == other.num[i]:
                bulls += 1
            elif self.num[i] in other.num:
                cows += 1
        return bulls, cows

class ComputerPlayer(object):
    """An average computer player."""
    def __init__(self):
        self.possible_nums = []
        for num in xrange(10**(NUM_DIGITS-1), 10**NUM_DIGITS):
        # Iterate over the numbers that has NUM_DIGITS digits.
            try:
                self.possible_nums.append(Num(num))
            except IllegalNumber:
                pass
        self._secret_num = random.choice(self.possible_nums)

    def guess(self, check_func):
        """Guess a number and check it with the given function.
        The function gets a guess and returns the bulls and cows.
        Return True if the player won, and False otherwise.
        """
        try:
            guess_num = random.choice(self.possible_nums)
        except IndexError:
            # If self.possible_nums is empty, the opponent cheated or
            # mistaked
            return True  # If one player mistakes, his opponent wins
        bulls, cows = check_func(guess_num)
        if bulls == NUM_DIGITS:
            return True
        self.possible_nums = [n for n in self.possible_nums
                              if n.compare(guess_num) == (bulls, cows)]
          # The possible numbers that could be the opponent's secret number.
        return self.possible_nums == []  # If it's empty, the opponent cheated

    def check(self, guess_num):
        """Check the opponent's guess, and return the bulls and cows."""
        return self._secret_num.compare(guess_num)

class HumanPlayer(object):
    """Ask the user for a guess, show him the suitable bulls and cows
    for the guess, and ask him for suitable bulls and cows for the
    opponent's guess - let the user play Bulls and Cows."""

    def guess(self, check_func):
        """Ask the user for a guess, and check it with the
        given function, that gets the guess and returns
        the bulls and cows in a (bulls, cows) representation.
        Print the results to the user.
        Return True if the player won, and False otherwise.
        """
        while True:
            try:
                guess_num = Num(raw_input('Enter a guess: '))
            except IllegalNumber:
                print ("The number should consist of %d different digits"
                       "and the first digit can't be 0." % NUM_DIGITS)
                continue
            break
        bulls, cows = check_func(guess_num)
        if (bulls, cows) == (NUM_DIGITS, 0):
            print ('You won!')
            return True
        print 'You have {} bulls and {} cows.'.format(bulls, cows)
        print '-----'
        return False

    def check(self, num):
        """Check the opponent's guess, and return the bulls and cows."""
        # The messages are indented, to improve the readibility
        # for the user - he can easily distinguish between messages
        # from `guess` and messages from `check`
        print "\tYour opponent's guess is {}.".format(num)
        bulls, cows = int(raw_input('\tBulls: ')), int(raw_input('\tCows: '))
        if (bulls, cows) == (NUM_DIGITS, 0):
            print 'You lost!'
        return bulls, cows

def play(player1, player2):
    """Play a game between the two given Player classes.
    Each player class should contain `guess` and `check` methods.
    `check` will get the opponent's guess and return the suitable
    bulls and cows, and `guess` will get a function (the opponent's
    `check` method) and let the player guess a number and check it
    with the given function. `guess` will return True if the player
    won, and False otherwise.
    Return 1 if player1 won, and 2 if player2 won.
    """
    current_player, opponent = random.sample((player1(), player2()), 2)
    while not current_player.guess(opponent.check):
        current_player, opponent = opponent, current_player
    return {player1: 1, player2: 2}[current_player.__class__]

play(HumanPlayer, ComputerPlayer)

raw_input("Thanks for playing Bulls and Cows! ")