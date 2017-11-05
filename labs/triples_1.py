# 14 min  32 sec
def get_triples():
    ret = []
    for multiplier_1 in range(10,100):
        for multiplier_2 in range(multiplier_1,100):
            for multiplier_3 in range(multiplier_2,100):
                if multiplier_1<multiplier_2 and multiplier_2<multiplier_3:
                    if set(str(multiplier_1*multiplier_2*multiplier_3)) == set(str(multiplier_1)+str(multiplier_2)+str(multiplier_3)) and\
                            len(str(multiplier_1)+str(multiplier_2)+str(multiplier_3)) == len(set(str(multiplier_1)+str(multiplier_2)+str(multiplier_3))):
                        ret.append((multiplier_1,multiplier_2,multiplier_3))
    return ret


for triple in get_triples():
    print(triple[0],'x',triple[1],'x',triple[2],'=',triple[0]*triple[1]*triple[2])