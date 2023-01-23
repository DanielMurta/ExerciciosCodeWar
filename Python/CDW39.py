def to_jaden_case(string):
    return ' '.join(s.capitalize() for s in string.split(' '))

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))