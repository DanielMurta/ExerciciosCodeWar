def domain_name(url):
    url = url.replace('http://', '')
    url = url.replace('https://', '')
    url = url.replace('www.', '')
    n_url = url[::-1]
    for i, n in enumerate(n_url):
        if n == '.':
            y = n_url[i+1::]
            for e, b in enumerate(y):
                if '.' in y:
                    k = y[3::]
                    return k[::-1]
                else:
                    return y[::-1]
                        
                    
                              

print(domain_name('http://google.com'))
print(domain_name('http://google.co.jp'))
print(domain_name('www.xakep.ru'))