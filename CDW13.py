def disemvoweal(string_):
    for i in 'aeiouAEIOU':
        string_ = string_.replace(i, '')
    return string_

    
disemvoweal('What are you, a communist?')