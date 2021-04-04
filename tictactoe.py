import pygame
pygame.font.init()

win = pygame.display.set_mode((900, 900))

pygame.draw.line(win, "white", (300, 0), (300, 900))
pygame.draw.line(win, "white", (600, 0), (600, 900))

pygame.draw.line(win, "white", (0, 300), (900, 300))
pygame.draw.line(win, "white", (0, 600), (900, 600))

pygame.mouse.set_cursor(*pygame.cursors.diamond)

pygame.display.flip()

font = pygame.font.Font('freesansbold.ttf', 32)

gameOver = False

def x_col_detection(x):
    if x < 300:
        return 1
    elif x < 600:
        return 2
    else:
        return 3

def y_col_detection(y):
    if y < 300:
        return 1
    elif y < 600:
        return 2
    else:
        return 3

def draw_cross(x, y):
    pygame.draw.line(win, "red", (x, y), (x + 100, y - 100), 3)
    pygame.draw.line(win, "red", (x, y), (x + 100, y + 100), 3)
    pygame.draw.line(win, "red", (x, y), (x - 100, y - 100), 3)
    pygame.draw.line(win, "red", (x, y), (x - 100, y + 100), 3)
    pygame.display.flip()

def draw_circle(x, y):
    pygame.draw.circle(win, "blue", (x, y), 100, 5)
    pygame.display.flip()

turn = True

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

def winner():
    for row in range(len(board)):
        if board[row][0] != 0 and board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            pygame.draw.line(win, "green", (100, (row + 1) * 300 - 150), (800, (row + 1) * 300 - 150), 3)
            pygame.display.flip()
            return board[row][0]
    for i in range(len(board)):
        if board[0][i] != 0 and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            pygame.draw.line(win, "green", ((i + 1) * 300 - 150, 100), ((i + 1) * 300 - 150, 800), 3)
            pygame.display.flip()
            return board[0][i]
    if board[0][0] != 0 and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        pygame.draw.line(win, "green", (100, 100), (800, 800), 3)
        pygame.display.flip()
        return board[0][0]
    if board[2][0] != 0 and board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        pygame.draw.line(win, "green", (100, 800), (800, 100), 3)
        pygame.display.flip()
        return board[2][0]


while True:
    ev = pygame.event.get()

    mousex, mousey = pygame.mouse.get_pos()

    for event in ev:
        if event.type == pygame.MOUSEBUTTONDOWN and turn == True and board[y_col_detection(mousey) - 1][x_col_detection(mousex) - 1] == 0 and gameOver == False:
            draw_cross((x_col_detection(mousex) * 300 - 150), (y_col_detection(mousey) * 300 - 150))
            turn = False
            board[y_col_detection(mousey) - 1][x_col_detection(mousex) - 1] = 1

            if winner() == 1:
                gameOver = True
                print('cross is the winner')
            elif winner() == 2:
                gameOver = True
                print('circle is the winner')

            print(board[0])
            print(board[1])
            print(board[2])
            print('---------')

        elif event.type == pygame.MOUSEBUTTONDOWN and turn == False and board[y_col_detection(mousey) - 1][x_col_detection(mousex) - 1] == 0 and gameOver == False:
            draw_circle((x_col_detection(mousex) * 300 - 150), (y_col_detection(mousey) * 300 - 150))
            turn = True
            board[y_col_detection(mousey) - 1][x_col_detection(mousex) - 1] = 2

            if winner() == 1:

                gameOver = True
                print('cross is the winner')
            elif winner() == 2:
                gameOver = True
                print('circle is the winner')

            print(board[0])
            print(board[1])
            print(board[2])
            print('---------')