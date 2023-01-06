def order(sentence):
    words = []
    for i in range(1,10):
        for word in sentence.split():
            if str(i) in word:
                words.append(word)
    return " ".join()    
        
        

print(order('4of Fo1r pe6ople g3ood th5e the2'))