    
    if username.replace("-", "").replace("_", "").isalnum() is False:
        return False
    elif website.isalnum() is False:
