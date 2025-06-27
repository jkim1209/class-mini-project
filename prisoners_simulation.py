
import random

def play_random(trials=100000):
    pardoned = 0
    in_drawer = list(range(100))
    sampler = list(range(100))
    for _ in range(trials):
        random.shuffle(in_drawer)
        found = False
        for prisoner in range(100):
            found = False
            for reveal in random.sample(sampler, 50):
                card = in_drawer[reveal]
                if card == prisoner:
                    found = True
                    break
            if not found:
                break
        if found:
            pardoned += 1
    return pardoned / trials * 100



if __name__ == '__main__':
    print("100 Prisoners Problem 시뮬레이션 시작")
    print("코드 실행 준비됨")
