def identical_strings(list_one, list_two):
    for i in list_two:  
        if i not in list_one:
            print "the lists are different"
            break   
        else:
            print "the lists are the same"
identical_strings(['celery','carrots','bread','milk'], ['celery','carrots','bread','cream'])