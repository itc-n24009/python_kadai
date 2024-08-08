name_age = {"tanaka": 35, "satou": 25, "suzuki": 27}

def dict_info(x,key):
    try:
        return x[key]
    except:
        return "key is not found"

