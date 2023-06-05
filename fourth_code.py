# 6. 有n個人圍成一圈 並從第一個人開始報數(從1開始報數) 如果報到4的人就退出圓圈 請問留到最後留下的人是原本的第幾位？
class OutPerson:
    def __init__(self):
        self.people_num = 0
        self.lis = []
    def new_lis(self, people_num):
        self.people_num = people_num
        for i in range(self.people_num):
            self.lis.append(0)

        self.__out_loop()
        self.__find_final_out()

    def __out_loop(self):
        out_num = 0
        count = 1
        index = 0
        while 1 == 1:
            if index == self.people_num:
                index = 0
            if out_num == (self.people_num - 1):
                break
            if self.lis[index] != 0:
                index += 1
                continue

            if count == 4:
                count = 0
                out_num += 1
                self.lis[index] = out_num
            index += 1
            count += 1
        #print(self.lis)
    def __find_final_out(self):
        for i in range(self.people_num):
            if self.lis[i]==0:
                print("最後留下來的是第"+str(i+1)+"位")
                break

if __name__ == '__main__':
    outperson = OutPerson()
    outperson.new_lis(10)
