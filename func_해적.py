
import random
def game():
    print('''
                    ---------
                    |+++++++++|
                    ___________
                    |  O   @  |
                    |    o    |
                     ---===---
                       |   |
                ---------------------
                | {0} | {1} | {2} | {3} |
             --------------------------
            | {4} | {5} | {6} | {7} | {8} |
             --------------------------
            | {9} | {10} | {11} | {12} | {13} |
             -------------------------
               | {14} | {15} | {16} | {17} |
               ---------------------
            '''.format(status[0], status[1], status[2], status[3], status[4],
                    status[5], status[6], status[7], status[8], status[9],
                    status[10], status[11], status[12], status[13], status[14],
                    status[15], status[16], status[17],))
def head():
      print('''
                  ---------
                 |+++++++++|
                 ___________
                 |  O   @  |
                 |    o    |
                  ---===---
                    |   |
                       ~ /  
                    \ ~ /
                     \   
                    /  ~\ 
                   /     \ 
                    ~~~~~ 
                퐁~~~~ 당신이 걸렸습니다!''')

com = random.randrange(0,17)
status = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18"]
while True :
    game()
    use = int(input("숫자입력 :"))
    status[use-1] = "\\"
    if com == use :
        head()
        break   
