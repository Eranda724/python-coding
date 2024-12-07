import math

def myfun(N):
    pegs = [[] for _ in range(N)]
    ball_number = 1

    while True:
        placed = False
        for peg in pegs:
            if not peg or math.isqrt(peg[-1] + ball_number)**2 == peg[-1] + ball_number:
                peg.append(ball_number)
                placed = True
                break
        if not placed:
            return ball_number - 1
        ball_number += 1


def main():
    T = int(input().strip())
    for i in range(T):
        N = int(input().strip())
        print(myfun(N))


if __name__ == "__main__":
    main()