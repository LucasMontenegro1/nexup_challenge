"""
Function that adds each element of two given strings 
in the form of a "block", that is, the first element 
of the first string is added to the first element of 
the second and so on.
returns a third string with the result separated by 
spaces
"""
def addNumbers(first, second):
    try:
        x = list(map(float, first.split(' ')))
        y = list(map(float, second.split(' ')))

        if len(x) != len(y):
            raise Exception('Both strings must be the same size')

        sums =  [x + y for x, y in zip(x, y)]
        return ' '.join([str(elem) for elem in sums])

    except ValueError as err:
        print(f"Invalid string format {err=}, {type(err)=}")
        raise