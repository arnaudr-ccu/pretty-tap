# pretty-tap

Pretty print a TAP text.

    $ cat example.tap 
    1..4
    ok 1 - Input file opened
    not ok 2 - First line of the input valid
    ok 3 - Read the rest of the file
    not ok 4 - Summarized correctly # TODO Not written yet

    $ ./pretty-tap.py < example.tap 
     ✓ - Input file opened
     ✗ - First line of the input valid
     ✓ - Read the rest of the file
     ✗ - Summarized correctly
    
    4 test(s), 2 failure(s)

References:

- <http://testanything.org/>
- <https://github.com/python-tap/tappy>
