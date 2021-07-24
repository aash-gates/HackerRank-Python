try:
        username, url = s.split("@")
        website, extension = url.split(".")
        if any([username=='',website=='',url=='']): return False
    except ValueError:
        return  False
				
    cond1 = all(map(lambda x : 
    x.isdigit() or 
    x.isupper() or 
    x.islower() or 
    x == '-' or x=='_', 
    username))
		
    cond2 = all(map(lambda x : 
    x.isdigit() or 
    x.isupper() or 
     x.islower(), 
    website))
		
    cond3 = 0< len(extension) < 4
    
    return all([cond1,cond2,cond3])