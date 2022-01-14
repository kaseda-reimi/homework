import numpy as np

table = np.ones([18,18])
table[0] = [1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  0.5,0,  1,  1,  0.5,1]#normal
table[1] = [1,  0.5,0.5,1,  2,  2,  1,  1,  1,  1,  1,  2,  0.5,1,  0.5,1,  2,  1]#fire
table[2] = [1,  2,  0.5,1,  0.5,1,  1,  1,  2,  1,  1,  1,  2,  1,  0.5,1,  1,  1]#water
table[3] = [1,  1,  2,  0.5,0.5,1,  1,  1,  0,  2,  1,  1,  1,  1,  0.5,1,  1,  1]#electric
table[4] = [1,  0.5,2,  1,  0.5,1,  1,  0.5,2,  0.5,1,  0.5,2,  1,  0.5,1,  0.5,1]#grass
table[5] = [1,  0.5,0.5,1,  2,  0.5,1,  1,  2,  2,  1,  1,  1,  1,  2,  1,  0.5,1]#ice
table[6] = [2,  1,  1,  1,  1,  2,  1,  0.5,1,  0.5,0.5,0.5,2,  0,  1,  2,  2,  0.5]#fight
table[7] = [1,  1,  1,  1,  2,  1,  1,  0.5,0.5,1,  1,  1,  0.5,0.5,1,  1,  0,  2]#poison
table[8] = [1,  2,  1,  2,  0.5,1,  1,  2,  1,  0,  1,  0.5,2,  1,  1,  1,  2,  1]#earth
table[9] = [1,  1,  1,  0.5,2,  1,  2,  1,  1,  1,  1,  2,  0.5,1,  1,  1,  0.5,1]#fly
table[10]= [1,  1,  1,  1,  1,  1,  2,  2,  1,  1,  0.5,1,  1,  1,  1,  0,  0.5,1]#esper
table[11]= [1,  0.5,1,  1,  2,  1,  0.5,0.5,1,  0.5,2,  1,  1,  0.5,1,  2,  0.5,0.5]#bug
table[12]= [1,  2,  1,  1,  1,  2,  0.5,1,  0.5,2,  1,  2,  1,  1,  1,  1,  0.5,1]#rock
table[13]= [0,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  1,  1,  2,  1,  0.5,1,  1]#ghost
table[14]= [1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  1,  0.5,0]#dragon
table[15]= [1,  1,  1,  1,  1,  1,  0.5,1,  1,  1,  2,  1,  1,  2,  1,  0.5,1,  0.5]#dark
table[16]= [1,  0.5,0.5,0.5,1,  2,  1,  1,  1,  1,  1,  1,  2,  1,  1,  1,  0.5,2]#metal
table[17]= [1,  0.5,1,  1,  1,  1,  2,  0.5,1,  1,  1,  1,  1,  1,  2,  2,  0.5,1]#fairy

if __name__ == '__main__':
    #first time
    n = int(input("Enter attacker type(0~17): "))
    judge = int(input("Enter the judge(1~4): "))
    #batsugun:1, imahitotu:2, mukou:3, toubai:4
    answer = [[18,18]]
    if judge == 1:
        for i in range(table.shape[1]):
            for j in range(i,table.shape[1]):
                if table[n][i]*table[n][j] > 1:
                    answer = np.append(answer,[[i,j]],axis=0)
    elif judge == 2:
        for i in range(table.shape[1]):
            for j in range(i,table.shape[1]):
                if 0 < table[n][i]*table[n][j] < 1:
                    answer = np.append(answer,[[i,j]],axis=0)
    elif judge == 3:
        for i in range(table.shape[1]):
            for j in range(i,table.shape[1]):
                if table[n][i]*table[n][j] == 0:
                    answer = np.append(answer,[[i,j]],axis=0)
    elif judge == 4:
        for i in range(table.shape[1]):
            for j in range(i,table.shape[1]):
                if table[n][i]*table[n][j] == 1:
                    answer = np.append(answer,[[i,j]],axis=0)
    answer = np.delete(answer, 0, 0)
    print(answer)
    print(answer.shape[0])
    #onwards
    loop = True
    while loop:
        _answer = [[18,18]]
        n = int(input("Enter attacker type(0~17): "))
        judge = int(input("Enter the judge(1~4): "))
        if judge == 0:
            break
        if judge == 1:
            for i in range(answer.shape[0]):
                if table[n][answer[i][0]]*table[n][answer[i][1]] > 1:
                    _answer = np.append(_answer,[answer[i]],axis=0)
        elif judge == 2:
            for i in range(answer.shape[0]):
                if 0 < table[n][answer[i][0]]*table[n][answer[i][1]] < 1:
                    _answer = np.append(_answer,[answer[i]],axis=0)
        elif judge == 3:
            for i in range(answer.shape[0]):
                if table[n][answer[i][0]]*table[n][answer[i][1]] == 0:
                    _answer = np.append(_answer,[answer[i]],axis=0)
        elif judge == 4:
            for i in range(answer.shape[0]):
                if table[n][answer[i][0]]*table[n][answer[i][1]] == 1:
                    _answer = np.append(_answer,[answer[i]],axis=0)
        answer = np.delete(_answer, 0, 0)
        print(answer)
        print(answer.shape[0])
        if answer.shape[0] == 0:
            print("gaitou nasi")
            loop = False