def list_del_nth(list_, index):
    try:
        del list_[index]
    except IndexError:
        print("Index not found")
    except:
        print("Unexcepted Error")
    else:
        print("Successfully")
