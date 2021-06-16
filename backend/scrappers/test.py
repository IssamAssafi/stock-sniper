def get_list():
    l=[1,2,3,4,5]
    def only_first_two():
        return l[:2]

    return l

res=get_list().only_first_two()
print(res)
    

