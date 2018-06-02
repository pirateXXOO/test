# Author:Jack
# Date:2018/5/23

menu = {
    'Beijing':{
        'Chaoyang':{
            'Guomao':{
                'CICC':{},
                'HP':{},
                'Zhada bank':{},
                'CCTV':{},
            },
            'Wangjing':{
                'Momo':{},
                'Bentch':{},
                '360':{},
            },
            'Sanlitun':{
                'YUIKU':{},
                'Apple':{},
            },
        },
        'Changping':{
            'Shahe':{
                'Laonanhai':{},
                'Ataibaozi':{},
            },
            'Tiantongyuan':{
                'Lianjia':{},
                'Woaiwojia':{},
            },
            'Huilongguan':{},
        },
        'Haidian':{
            'Wudaokou':{
                'Google':{},
                'Wangyi':{},
                'Sohu':{},
                'Sogou':{},
                'Kuaishou':{},
            },
            'Zhongguancun':{
                'Youku':{},
                'Iqiyi':{},
                'Qichezhijia':{},
                'Xindongfang':{},
                'QQ':{},
            },
        },
    },
    'Shanghai':{
        'Pudong':{
            'lujiazui':{
                'CICC':{},
                'GaoSheng':{},
                'Mogen':{},
            },
            'Waitan':{},
        },
        'Minhang':{},
    },
    'Shandong':{
        'Jinan':{},
        'Qingdao':{},
        'Dezhou':{
            'Laoling':{
                'Dingwuzhen':{},
            },
            'Pingyuan':{},
        },
    },
}

# while True:
#         for key in menu:
#             print(key)
#         choice = input("1>>:").strip()
#         if choice in menu:
#             while True:
#                 for key2  in menu[choice]:
#                     print(key2)
#                 choice2 = input("2>>:").strip()
#                 if choice2 in menu[choice]:
#                     while True:
#                         for key3 in menu[choice][choice2]:
#                             print(key3)
#                         choice3 = input("3>>:").strip()
#                         if choice3 in menu[choice][choice2]:
#                             while True:
#                                 for key4 in menu[choice][choice2][choice3]:
#                                     print(key4)
#                                 choice4 = input("4>>:").strip()
#                                 print("Last level")

current_layer = menu
# parent_layer = menu
parent_layers = []

while True:
    for key in current_layer:
        print(key)
    choice = input(">>:").strip()
    if len(choice) == 0:continue
    if choice in current_layer:
        parent_layers.append(current_layer)

        current_layer = current_layer[choice]
    elif choice == 'b':
        if parent_layers:
            current_layer = parent_layers.pop()
    else:
        print("No such choice!")
