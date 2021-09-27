def sum(l, N):
    for i, item in enumerate(l):
        for j in range(i+1, len(l)):
            total_of_two_items = l[i] + l[j]
            if(total_of_two_items == N):
                return True
    return False

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()