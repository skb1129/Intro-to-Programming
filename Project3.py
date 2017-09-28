def check(text, ans):
    """This function takes text and its answers as arguments and checks
    the user input with the answers."""
    for index in range(len(ans)):
        input_text = 'In Place of ' + str(index + 1) + ' ? '
        count = 5
        print text, '\n\nYou have ', count, 'chance.'
        user_input = str(raw_input(input_text))
        while user_input.lower() != ans[index]:
            count -= 1
            if count == 0:
                print '\nYou Lost\n'
                return
            print '\nWrong Answer\n\n', text
            print '\nYou have ', count, 'chance left.'
            user_input = str(raw_input(input_text))
        print '\nCorrect\n'
        replace_text = '__' + str(index + 1) + '__'
        text = text.replace(replace_text, ans[index])
    print 'You Won!\n\n', text


def easy():
    # assigning value of question text and answers
    text = '''A common first thing to do in a language is display
'Hello __1__!'  In __2__ this is particularly easy; all you have to do
is type in:
__3__ "Hello __1__!"
Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the __3__ command, and
produces a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an __4__ file in a browser, but it's
a step in learning __2__ syntax, and that's really its purpose.'''
    ans = ['world', 'python', 'print', 'html']
    # calling the function to check for user inputs
    check(text, ans)


def medium():
    # assigning value of question text and answers
    text = '''A __1__ is created with the def keyword.  You specify the inputs a
__1__ takes by adding __2__ separated by commas between the parentheses.
__1__s by default returns __3__ if you don't specify the value to retrun.
__2__ can be standard data types such as string, integer, dictionary, tuple,
and __4__ or can be more complicated such as objects and lambda functions.'''
    ans = ['function', 'arguments', 'none', 'list']
    # calling the function to check for user inputs
    check(text, ans)


def hard():
    # assigning value of question text and answers
    text = '''When you create a __1__, certain __2__s are automatically
generated for you if you don't make them manually. These contain multiple
underscores before and after the word defining them.  When you write
a __1__, you almost always include at least the __3__ __2__, defining
variables for when __4__s of the __1__ get made.  Additionally, you generally
want to create a __5__ __2__, which will allow a string representation
of the method to be viewed by other developers.

You can also create binary operators, like __6__ and __7__, which
allow + and - to be used by __4__s of the __1__.  Similarly, __8__,
__9__, and __10__ allow __4__s of the __1__ to be compared
(with <, >, and ==).'''
    ans = ['class', 'function', 'init', 'object', 'repr', 'plus',
           'addition', 'subtraction', 'greater', 'equal']
    # calling the function to check for user inputs
    check(text, ans)


while True:
    # start off the game by asking user for game difficulty
    level = str(raw_input('Select a level : easy, medium or hard : '))
    if level.lower() == 'easy':
        easy()
        break
    elif level.lower() == 'medium':
        medium()
        break
    elif level.lower() == 'hard':
        hard()
        break
    else:
        print '\nWrong Input\n'
