"""사목, 작성자: AI Sweigart al@inventwithpython.com
입체사목과 유사한, 타일을 떨어뜨려서 4개를 한 줄로 늘어놓는 게임"""

import sys
EMPTY_SPACE = "."
PLAYER_X = "X"
PLAYER_O = "O"

BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH

BOARD_TEMPLATE = """
1234567
+-------+
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
+-------+"""

def main():
    """사목 게임을 실행한다."""
    print(
        """사목, 작성자: AI Sweigart al@inventwithpython.com
        
두 사람이 차례로 7개 열 중 하나에 타일을 떨어뜨려
수평, 수직, 대각선으로 사목을 만든다.
"""
    )
    gameBoard = getNewBoard()
    playerTurn = PLAYER_X

    while True:
        displayBoard(gameBoard)
        playerMove = getPlayerMove(playerTurn, gameBoard)
        gameBoard[playerMove] = playerTurn

        if isWinner(playerTurn, gameBoard):
            displayBoard(gameBoard)
            print("플레이어 {}의 승리!".format(playerTurn))
            sys.exit()

        elif isFull(gameBoard):
            displayBoard(gameBoard)
            print("무승부 게임입니다!")
            sys.exit()

        if playerTurn == PLAYER_X:
            playerTurn = PLAYER_O
        elif playerTurn == PLAYER_O:
            playerTurn = PLAYER_X


def getNewBoard():
    """사목 말판을 표현하는 딕셔너리를 반환한다.


    키는 두 정수로 구성된 (columnIndex, rowIndex) 튜플이며,
    값은 "X", "O", "."(빈칸) 문자열이다."""
    board = {}
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            board[(columnIndex, rowIndex)] = EMPTY_SPACE
    return board


def displayBoard(board):
    """화면에 말판에 타일을 표시한다."""
    tileChars = []
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            tileChars.append(board[(columnIndex, rowIndex)])

    print(BOARD_TEMPLATE.format(*tileChars))


def getPlayerMove(playerTile, board):
    """ 플레이어가 말판에서 타일을 떨어뜨릴 열을 선택하게 한다.
    
타일이 떨어질 (column, row) 튜풀을 반환한다."""
    while True:
        print(f"플레이어 {playerTile}, 1에서 {BOARD_WIDTH}까지 숫자 또는 QUIT를 입력하십시오:")
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("즐겁게 퍼즐을 풀어주셔서 감사합니다!")
            sys.exit()
        
        if response not in COLUMN_LABELS:
            print(f"1에서 {BOARD_WIDTH}까지 숫자를 입력해주십시오.")
            continue

        columnIndex = int(response) -1

        if board[(columnIndex, 0)] != EMPTY_SPACE:
            print("열이 꽉 차 있으므로, 다른 열을 선택해주십시오.")
            continue

        for rowIndex in range(BOARD_HEIGHT -1, -1, -1):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return (columnIndex, rowIndex)
        

def isFull(board):
    """'board'에 빈칸이 없으면 True를 반환한다.
    그렇지 않으면 False를 반환한다."""
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return False
    return True


def isWinner(playerTile, board):
    """'playerTile'이 'board'에서 사목을 완성하면 True를 반환하고, 
    그렇지 않으면 Flase를 반환한다."""

    for columnIndex in range(BOARD_WIDTH -3):
        for rowIndex in range(BOARD_HEIGHT):
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex)]
            tile3 = board[(columnIndex + 2, rowIndex)]
            tile4 = board[(columnIndex + 3, rowIndex)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
            
    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT -3):
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex, rowIndex + 1)]
            tile3 = board[(columnIndex, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT -3):
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex + 1)]
            tile3 = board[(columnIndex + 2, rowIndex + 2)]
            tile4 = board[(columnIndex + 3, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
            
            tile1 = board[(columnIndex + 3, rowIndex)]
            tile2 = board[(columnIndex + 2, rowIndex + 1)]
            tile3 = board[(columnIndex + 1, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    return False

if __name__ == "__main__":
    main()