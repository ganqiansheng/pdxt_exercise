import calendar
import datetime
import time
import numpy as np
import matplotlib.pyplot as plt
if __name__ == '__main__':





    import pandas as pd
    print(f'pandas version: {pd.__version__}')
    data = {
        'brand': ['Python数据之道', '价值前瞻', '菜鸟数据之道', 'Python', 'Java'],
        'A': [10, 2, 5, 20, 16],
        'B': [4, 6, 8, 12, 10],
        'C': [8, 12, 18, 8, 2],
        'D': [6, 18, 14, 6, 12],
        'till years': [4, 1, 1, 30, 30]
    }
    df = pd.DataFrame(data=data)
    print(df)
    index = [8, 3, 4, 5, 2]
    df = pd.DataFrame(data=data, index=index)
    print('df:',df)
    print(df.sort_index())
    print(df.sort_index(axis=1))
    print(df.sort_index(axis=0))
    print(df.sort_values(['till years','B']))
    print(df.columns)
    # print(df.query('brand == "Python数据之道"'))
    # print(df[df['brand'] == 'Python数据之道'])
    # print(df.query('A == 2'))
    # print(df.query('A > 5'))
    # name = 'Python'
    # print(df.query('brand == @name'))
    # print(df.query("brand in ['价值前瞻', '菜鸟数据之道'] & A>1"))
    # print('till years:',df.query("`till years`> 2")[['brand','A']])


    #
    # m, n = (5, 3)
    # x = np.linspace(0, 1, m)
    # y = np.linspace(0, 1, n)
    # X, Y = np.meshgrid(x, y)
    # # print(x)
    # # print(y)
    # # print(X)
    # # print(Y)
    # plt.plot(X, Y, marker='.', color='blue', linestyle='none')
    # plt.show()
    # z = [i for i in zip(X.flat, Y.flat)]
    # print(z)




    # print(np.random.rand(4,4))
    # print(np.random.rand(2,3))
    # print(np.random.randn(2,3))
    # a = np.random.randint(5,10,size=(2,3))
    # print(a)
    # b = a * a
    # print(b)
    #




    # arr1 = np.array([1, 2, 3, 4])
    # print(arr1)
    # arr2 = np.array((1,2,3,4))
    # print(arr2)
    # arr3 = np.array([[1,2,4],[3,4,5]])
    # print(arr3)
    # print(arr3[0][1])
    # print(arr3[1,2])
    #
    # arr = np.arange(24).reshape(2, 3, 4)
    # print(arr,arr.ndim,arr.shape,arr.size,arr.itemsize,arr.nbytes)
    # print(arr.T)
    #
    # print(np.array([1.22,3.45,6.779], dtype='int8'))
    # a = np.arange(24).reshape(4,6)
    # print(a)
    # print(a.T)
    # b = a.flat
    # a.flat = 7
    # print(a)
    # a.flat[[1,4]] =1
    # print('a:\n',a)
    # c = np.arange(1,51,1).reshape(1,50)
    # print(c)
    # print(np.cumsum(c,axis=1))
    # print(51*25)
    # print(a.resize(4,3))
    # print(b)
    # print(b[1])
    # for item in b:
    #     print(item)
    # print(b[[1,4]])
    # def pySum():
    #     a = list(range(10000))
    #     b = list(range(10000))
    #     c = []
    #     for i in range(len(a)):
    #         c.append(a[i] ** 2 + b[i] ** 2)
    #     return c


    # a = [4, 5, 6, 5, 6, 7, 8, 9, 10, 13, 14, 15, 20, 21, 22]
    # print([a[i] for i in [1,3,6]])
    # d = {'x': '1', 'y': '8', 'z': '4'}
    # e = sorted(d.items(),key=lambda x:x[1],reverse=True)
    # f =dict(e)
    # print(e)
    # print(f)
    #
    # date =datetime.datetime.today()
    # print(date)
    # print(date.date())
    # print(date.time().hour)
    # print(date.time().minute)
    # print(date.time().second)
    # print(date.time().microsecond)
    # print(date.time().tzinfo)
    # print(date.time().tzname())
    # print(date.weekday())
    # print(date.isoweekday())
    # # d2 =date.replace(year=2020)
    # # print(d2.date())
    # print(datetime.timedelta(days=31, seconds=24640, microseconds=1000))
    # print(date + datetime.timedelta(days=1, seconds=0, microseconds=0))
    # print(datetime.timedelta())
    #
    # import pytz
    # sh = pytz.timezone('Asia/Shanghai')
    # d_tz = datetime.datetime(2020, 10, 12, hour=8, tzinfo=sh)
    # print(d_tz.tzinfo)
    # datestr = date.strftime('%Y-%m-%d %H:%M:%S')
    # print('datestr:',datestr)
    # print(date.isoformat())
    # print(date.timestamp())
    # print(date.timestamp())
    # print('时间戳：',datetime.datetime.fromtimestamp(date.timestamp()))
    # print('时间戳：',datetime.date.fromtimestamp(date.timestamp()))
    # print('时间戳：',datetime.date.fromtimestamp(date.timestamp()))
    #
    # print("datetime.datetime.strptime(datestr,'%Y-%m-%d %H:%M:%S'):",datetime.datetime.strptime(datestr,'%Y-%m-%d %H:%M:%S'))
    #
    # datestart = datetime.datetime(1970,1,1,8,0)
    # timedelta = date - datestart
    # print('timedelta:',timedelta)
    # timedelta_s = timedelta.total_seconds()
    # print('时间戳：',timedelta_s)
    # print(timedelta_s)
    # print(time.time())
    # timedelta_s2 = time.time() -1602728783.2113311
    # print('间隔天数:',datetime.date.today()-datetime.date.fromtimestamp(1602728783.2113311))
    # print('时间戳3',datetime.datetime.fromtimestamp(timedelta_s2))
    # print(datetime.datetime.fromtimestamp(timedelta_s))
    # print(datetime.date.today(),datetime.time.min)
    # print(datetime.date.today(),datetime.time.max)
    # print(datetime.date.today(),datetime.datetime.now())
    # print(datetime.date.today() + datetime.timedelta(days=2))
    # print(datetime.date.today() - datetime.timedelta(seconds=1000000))
    #
    # print(date.date().today() - datetime.timedelta(datetime.date.today().weekday()))
    # print(date.date().today() + datetime.timedelta(6 - datetime.date.today().weekday()))
    # t = time.localtime()
    # print('type of t:',type(t))
    # print('type of time.asctime(t):',type(time.asctime(t)))
    # print(t)
    #
    # print([t[i] for i in range(9)])
    #
    # tt = time.mktime(t)
    # print(tt)
    # print(datetime.datetime.fromtimestamp(tt))
    #
    # print(time.asctime(t))
    # print(time.strftime('%Y-%m-%d %H:%M:%S',t))
    # print(time.strptime(time.asctime(t)))
    #
    # print(calendar.prcal(2022))
    # print(calendar.month(2022,5))

    # [c_list[i] for i in [0, 1, 3]]
    # s1 = 'Python 数 据 之 道 '
    # # 编 码 encode
    # s2 = s1.encode(encoding='utf-8')
    # print(s2)
    # s3 = s2.decode(encoding='utf-8')
    # print(s3)
    # s7 = ''
    # # isdigit() 、 isnumeric() 为 True
    # # isdecimal() 为 False
    # print(s7.isdigit())
    # print(s7.isdecimal())
    # print(s7.isnumeric())
    #
    # s8 = '贰拾'
    # print(s8.isdigit())
    # print(s8.isdecimal())
    # print(s8.isnumeric())
    #
    # s = 'hello, world'
    # print(s.replace('l', 'L', 1))
    # print(s.replace('l', 'L'))
    #
    # print(" 列 表 相 加 ： ", [1, 2, 3] + ['a', 'b'])
    # a = [1, 2, 3]
    # b = ['a', 'b']
    # a.extend(b)
    # print(" 列 表 相 加 ： ", a)
    # print(" 将 元 组 转 为 列 表 ： ", list((3, 9, 6)))
    #
    # two_for_list = []
    # for x in range(5):
    #     for y in range(4, 7):
    #         two_for_list.append(x ** 2 + y)
    # print(two_for_list)

    # dict1 = {1:'name1',2:'name2',3:'name3',4:'name1',5:'name1',6:'name1',7:'name1',8:'name1',9:'name6'}
    # result = [k for k,v in dict1.items() if v == 'name1']
    # print(result)
    # print(dict1[9])
    # dict1[9] = 'name7'
    # print(dict1)
    # dict1.pop(3)
    # print(dict1)
    # del dict1[4]
    # print(dict1)
    # dict1.popitem()
    # print(dict1)
    # print(len(dict1))
    # print(str(dict1))
    # dict2=dict(dict1)
    # print(dict2)
    # print(type(dict2))
    # print(dict2[1])
    # # 用 setdefault() 方法统计一个列表里单词出现的次数
    # strings = ('Lemon', 'kitten', 'Lemon', 'Lemon',
    #            'lemon_zs', 'Lemon', 'Lemon', 'lemon_zs')
    # counts = {}
    # for kw in strings:
    #     counts[kw] = counts.setdefault(kw, 0) + 1
    #     print(counts)
    # print(counts)
    # my_dict01 = {x: x*x for x in range(6)}
    # print(my_dict01)
    # my_dict03 = {x: x * x for x in range(10) if x % 2 == 0}    1
    # s1 = 'Lemon'
    # s2 = "Python 数 据 之 道 "
    # s3 = """
    # hello, world! 56
    # """
