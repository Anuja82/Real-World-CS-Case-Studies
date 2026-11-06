cache=[]
capacity=3
def access_page(page):
    if page in cache:
        cache.remove(page)
        print(f"{page} already exists in cache")
    else:
        if len(cache)==capacity:
            removed=cache.pop(0)
            print(f"Removed least recently used: {removed}")
        print(f"Added page:{page}")
    cache.append(page)
    print("Current cache:", cache)
    print("-----------------")
access_page("A")
access_page("B")
access_page("C")
access_page("A")
access_page("D")