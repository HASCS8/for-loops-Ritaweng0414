def print_characters():
    # Your task is to use a for loop to iterate over the characters in the string "Python" and print each character.
    string_name = "Python"
    for element in string_name:
        print(element)
    pass

def main():
    print_characters()

# Unit tests
def test_print_characters():
    import sys
    from io import StringIO

    out = StringIO()
    sys.stdout = out
    print_characters()
    sys.stdout = sys.__stdout__
    assert out.getvalue().strip() == 'P\ny\nt\nh\no\nn', 'Test Failed'

if __name__ == '__main__':
    main()
    test_print_characters()
