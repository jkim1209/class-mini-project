import random

# ==============================
# [파트 1] 메인 실행 및 입출력 뼈대 담당
# - 전체 시뮬레이션 횟수 지정
# - 두 전략의 성공률 출력
# ==============================
def main():
    # 시뮬레이션 반복 횟수 지정
    trials = 100_000
    print("Simulation count:", trials)
    # 랜덤 전략 성공률 출력
    print(f"Random play wins: {play_random(trials):.1f}% of simulations")
    # 최적 전략 성공률 출력
    print(f"Optimal play wins: {play_optimal(trials):.1f}% of simulations")

# ==============================
# [파트 2] 랜덤 전략 함수 담당
# - 각 죄수가 상자를 무작위로 50개씩 선택
# - 100명 모두 성공하면 성공 카운트
# ==============================
def play_random(trials=100_000):
    # 전체 성공(모두 탈출) 횟수
    pardoned = 0
    # 0~99번 상자 번호 리스트
    in_drawer = list(range(100))
    # 0~99번 샘플링용 리스트
    sampler = list(range(100))
    # 시뮬레이션 trials만큼 반복
    for _ in range(trials):
        # 상자 번호 무작위 섞기
        random.shuffle(in_drawer)
        found = False
        # 100명의 죄수 각각 시도
        for prisoner in range(100):
            found = False
            # 무작위로 50개 상자 선택
            for reveal in random.sample(sampler, 50):
                card = in_drawer[reveal]
                # 자기 번호 찾으면 성공
                if card == prisoner:
                    found = True
                    break
            # 한 명이라도 실패하면 반복 종료
            if not found:
                break
        # 100명 모두 성공하면 pardoned 카운트
        if found:
            pardoned += 1
    # 최종 성공률(%) 반환
    return pardoned / trials * 100

<<<<<<< HEAD
def play_optimal(trials=100000):
=======
# ==============================
# [파트 3] 최적 전략(사이클 추적) 함수 담당
# - 각 죄수가 자기 번호 상자부터 시작해서
#   상자 내부 번호 따라 최대 50번 이동
# - 100명 모두 성공하면 성공 카운트
# ==============================
def play_optimal(trials=100_000):
    # 전체 성공(모두 탈출) 횟수
>>>>>>> upstream/main
    pardoned = 0
    # 0~99번 상자 번호 리스트
    in_drawer = list(range(100))
    # 시뮬레이션 trials만큼 반복
    for _ in range(trials):
        # 상자 번호 무작위 섞기
        random.shuffle(in_drawer)
        # 100명의 죄수 각각 시도
        for prisoner in range(100):
            reveal = prisoner
            found = False
            # 최대 50번 상자 내부 번호 추적(사이클 전략)
            for go in range(50):
                card = in_drawer[reveal]
                # 자기 번호 찾으면 성공
                if card == prisoner:
                    found = True
                    break
                # 못 찾으면 다음 상자는 카드에 적힌 번호로 이동
                reveal = card
            # 한 명이라도 실패하면 반복 종료
            if not found:
                break
        # 100명 모두 성공하면 pardoned 카운트
        if found:
            pardoned += 1
    # 최종 성공률(%) 반환
    return pardoned / trials * 100

# ==============================
# [파트 4] 실행 결과/리팩터링
# - 실행 결과 캡처, 코드 정리, 주석 추가, 문제 설명 등 기록
# ==============================

if __name__ == '__main__':
    # 메인 함수 실행
    main()

