def list_average():
    try:
        return sum(x)/len(x)
    except:
        print("list_len:", len(x))
        return None
