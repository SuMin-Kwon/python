# stock 리스트에는 종목(item), 시가(open), 고가 (high), 저가 (low) , 종가(close)가 저장.

class Stock:

    def __init__(self, li ) :
        self.stock = li

    def print_close(self):
        for el in self.stock[1::] :
            print(el[4], end=' ')
        print()        

    def print_close_grater(self, price ):
        for el in self.stock[1::]:
            if el[4] > price:
                print(f"{el[0]}:{el[4]}", end=" ")
        print()

    def get_open_item(self, item ):
        for el in self.stock[1::]:
            if el[0] == item:
                return el[1]

    def get_diff_item(self, item ):
        for el in self.stock[1::]:
            if el[0] == item:
                return el[1]-el[4]
 
