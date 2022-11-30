"""하노이 탑, 작성자: AI Sweigart al@inventwithpython.com
원판 더미를 움직이는 퍼즐 게임"""

import copy
import sys

TOTAL_DISKS = 5

SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))


def main():
    """하노이 탑 게임을 실행한다."""
    towers = {"A": SOLVED_TOWER, "B": [], "C": []}
    while True:
        displayTowers(towers)
        fromTower, toTower = getPlayerMove(towers)
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)
        print(SOLVED_TOWER, towers.values())
        if SOLVED_TOWER in (towers["B"], towers["C"]):
            displayTowers(towers)
            print("퍼즐을 풀었습니다! 참 잘했습니다!")
            sys.exit()



def getPlayerMove(towers):
    """플레이어에게 이동 명령을 요청한다. (formTower, toTower)를 반환한다."""
    while True:
        print('탑의 "시작"과 "끝"의 글자 또는 QUIT를 입력하십시오.')
        print("(예: 탑 A에서 탑 B로 원판을 이동하려면 AB를 입력합니다.)")
        print()
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("즐겁게 퍼즐을 풀어주셔서 감사합니다!")
            sys.exit()
        
        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("AB, AC, BA, BC, CA, CB 중 하나를 입력하십시오.")
            continue
        
        fromTower, toTower = response[0], response[1]

        if len(towers[fromTower]) == 0:
            print("원판이 없는 탑을 선택했습니다.")
            continue
        elif len(towers[toTower]) == 0:
            return fromTower, toTower
        elif towers[toTower][-1] < towers[fromTower][-1]:
            print("더 작은 원판에 더 큰 원판을 올릴 수 없습니다.")
            continue
        else:
            return fromTower, toTower


def displayTowers(towers):
    """세 탑에 배치된 원판을 표시한다."""
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                displayDisk(0)
            else:
                displayDisk(tower[level])
        print() #개행
        
    emptySpace = " " * (TOTAL_DISKS)
    print("{0} A{0}{0} B{0}{0} C\n".format(emptySpace))

def displayDisk(width):
    """주어진 width로 원판을 표시한다. width가 0이면 원판이 없음을 의미한다."""
    emptySpace = " " * (TOTAL_DISKS - width)

    if width == 0:
        print(f"{emptySpace}||{emptySpace}", end="")
    else:
        disk = "@" * width
        numLabel = str(width).rjust(2, "_")
        print(f"{emptySpace}{disk}{numLabel}{disk}{emptySpace}", end="")

        
if __name__ == "__main__":
    main()