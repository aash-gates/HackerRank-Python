def fun(s):
    try:
        username, url = s.split("@")
        website, extension = url.split(".")
        if any([username=='',website=='',url=='']): return False
    except ValueError:
        return  False
        
    cond1 = all([x.isdigit() or 
    x.isupper() or 
    x.islower() or 
    x == '-' or x=='_' for x in username])
    
    cond2 = all([x.isdigit() or 
    x.isupper() or 
     x.islower() for x in website])
    
    cond3 = 0< len(extension) < 4
    
    return all([cond1,cond2,cond3])

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)