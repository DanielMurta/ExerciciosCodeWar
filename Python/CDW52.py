def string_to_array(s):
    if s == "":
        return [""]
    
    return s.split()

string_to_array("Robin Singh")
string_to_array("CodeWars")
string_to_array("I love arrays they are my favorite")
string_to_array("1 2 3")
string_to_array("")

# return string.split() if string else ['']