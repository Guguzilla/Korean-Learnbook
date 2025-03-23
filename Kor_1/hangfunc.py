import numpy as np

#Importations ------------------------------------------------------------------------------------


def importation1():
    all_hangeul = ['아', '어', '오', '우', '으', '이', '야', '여', '요', '유',
                '애', '얘', '에', '예', '와', '왜', '외', '워', '웨', '위', '의',
                ]
    all_alphageul = ['a', 'eo', 'o', 'ou', 'eu', 'i', 'ya', 'yeo', 'yo', 'you',
                    'ae', 'yae', 'e', 'ye', 'wa', 'wae', 'oe', 'wo', 'we', 'wi', 'eui',
                    ]
    
    all_hangeul_dict = {}
    for i, hangeul in enumerate(all_hangeul):
        all_hangeul_dict[hangeul] = all_alphageul[i]

    return (all_hangeul, all_alphageul, all_hangeul_dict)

#---------------------------------------------------------------------------------------

def importation2():
    all_hangeul = ['ㄱ', 'ㅋ', 'ㄷ', 'ㅌ', 'ㅂ', 'ㅍ', 'ㅈ', 'ㅊ', 'ㅅ', 'ㅎ', 'ㄴ', 'ㅁ', 'ㅇ', 'ㄹ',
                '까', '따', '빠', '싸', '짜'
                ]
    all_alphageul = ['g,k', 'k', 'd,t', 't', 'b,p', 'p', 'dj', 'tch', 's', 'h', 'n', 'm', 'ng', 'r,l',
                    'kk', 'tt', 'pp', 'ss', 'djj'
                    ]
    
    all_hangeul_dict = {}
    for i, hangeul in enumerate(all_hangeul):
        all_hangeul_dict[hangeul] = all_alphageul[i]

    return (all_hangeul, all_alphageul, all_hangeul_dict)

#---------------------------------------------------------------------------------------------

def importation3():
    all_hangeul = ['아', '어', '오', '우', '으', '이', '야', '여', '요', '유',
                '애', '얘', '에', '예', '와', '왜', '외', '워', '웨', '위', '의',
                'ㄱ', 'ㅋ', 'ㄷ', 'ㅌ', 'ㅂ', 'ㅍ', 'ㅈ', 'ㅊ', 'ㅅ', 'ㅎ', 'ㄴ', 'ㅁ', 'ㅇ', 'ㄹ',
                '까', '따', '빠', '싸', '짜']
    all_alphageul = ['a', 'eo', 'o', 'ou', 'eu', 'i', 'ya', 'yeo', 'yo', 'you',
                    'ae', 'yae', 'e', 'ye', 'wa', 'wae', 'oe', 'wo', 'we', 'wi', 'eui',
                    'g,k', 'k', 'd,t', 't', 'b,p', 'p', 'dj', 'tch', 's', 'h', 'n', 'm', 'ng', 'r,l',
                    'kk', 'tt', 'pp', 'ss', 'djj']
    
    all_hangeul_dict = {}
    for i, hangeul in enumerate(all_hangeul):
        all_hangeul_dict[hangeul] = all_alphageul[i]

    return (all_hangeul, all_alphageul, all_hangeul_dict)

all_hangeul, all_alphageul, all_hangeul_dict = importation3()


#---------------------------------------------------------------------------
def gethangeul(all_hangeul,all_hangeul_dict):
    rn = np.random.randint(0, len(all_hangeul_dict))
    
    return (all_hangeul[rn])

#---------------------------------------------------------------------------
def choice(rand_hangeul,user_ans,all_hangeul_dict):
    if user_ans == all_hangeul_dict[rand_hangeul]:
        return True
    else:
        return False



