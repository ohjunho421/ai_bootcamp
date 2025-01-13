def solution(keyinput, board):
    answer = [0,0]
    
    for key in keyinput:
        if key == "left":
            answer[0] -= 1
        elif key == "right":
            answer[0] += 1
        elif key == "up":
            answer[1] += 1
        elif key == "down":
            answer[1] -= 1
            
        max_x = board[0] // 2
        max_y = board[1] // 2
        answer[0] = max(min(answer[0], max_x), -max_x)
        answer[1] = max(min(answer[1], max_y), -max_y)  

    return answer