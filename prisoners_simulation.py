def play_optimal(trials=100000):
    pardoned = 0
    in_drawer = list(range(100))
    for _ in range(trials):
        random.shuffle(in_drawer)
        for prisoner in range(100):
            reveal = prisoner
            found = False
            for go in range(50):
                card = in_drawer[reveal]
                if card == prisoner:
                    found = True
                    break
                reveal = card
            if not found:
                break
        if found:
            pardoned += 1
    return pardoned / trials * 100 

