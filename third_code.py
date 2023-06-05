# 5. 輸入一組list [4,3,6,8,9,2,5,1,7] 最大的數值與第最後一個交換 最小的與第一個交換 並輸出
class SwitchNUM:
    def __init__(self, lis, max_index=0, min_index=0):
        self.lis = lis

    def find_max(self):
        val = 0
        for i in range(len(self.lis)):
            if val < self.lis[i]:
                val = self.lis[i]
                self.max_index = i

    def find_min(self):
        val = 999999
        for i in range(len(self.lis)):
            if val > self.lis[i]:
                val = self.lis[i]
                self.min_index = i

    def swap(self):
        self.lis[self.max_index], self.lis[len(self.lis) - 1] = self.lis[len(self.lis) - 1], self.lis[self.max_index]
        self.lis[self.min_index], self.lis[0] = self.lis[0], self.lis[self.min_index]
        print(self.lis)


class SwitchNUM1:
    def __init__(self, lis):
        self.lis = lis

    def swap(self):
        max_val = self.lis[0]
        min_val = self.lis[0]
        max_index = 0
        min_index = 0

        for i in range(len(self.lis)):
            if self.lis[i] > max_val:
                max_val = self.lis[i]
                max_index = i
            elif self.lis[i] < min_val:
                min_val = self.lis[i]
                min_index = i
        # print(min_val,max_val)
        self.lis[max_index], self.lis[len(self.lis) - 1] = self.lis[len(self.lis) - 1], self.lis[max_index]
        self.lis[min_index], self.lis[0] = self.lis[0], self.lis[min_index]
        print(self.lis)


if __name__ == '__main__':
    lis = [4, 3, 6, 8, 9, 2, 5, 1, 7]
    # 第一種
    switch = SwitchNUM(lis)
    switch.find_max()
    switch.find_min()
    switch.swap()
    # 第二種
    switch1 = SwitchNUM1(lis)
    switch1.swap()
