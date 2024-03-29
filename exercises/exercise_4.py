def print_rectangle():
    # Your task is to create a nested loop to print a rectangle pattern.
    # For instance, a 3x3 rectangle would look like:
    # ***
    # ***
    # ***
    rown = 3
    col = 3

    for i in range(rown):
        for j in range(col):
            print('*', end='')
        print()

    pass

def main():
    print_rectangle()

# Unit tests
def test_print_rectangle():
    import sys
    from io import StringIO

    out = StringIO()
    sys.stdout = out
    print_rectangle()
    sys.stdout = sys.__stdout__
    assert out.getvalue().strip() == '***\n***\n***', 'Test Failed'

if __name__ == '__main__':
    main()
    test_print_rectangle()
