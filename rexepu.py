# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 13:43:24 2018

@author: dingq
"""

## rex for rmrb epu


import re  # import the package for regular expression


## defining the uncertainty terms
uncertainty1=u'不确定'
uncertainty2=u'不明确'
uncertainty3=u'不明朗'
uncertainty4=u'未明'
uncertainty5=u'难料'
uncertainty6=u'难以预计'
uncertainty7=u'难以估计'
uncertainty8=u'难以预测'
uncertainty9=u'难以预料'
uncertainty10=u'未知'

## defining the economy terms
economy1=u'经济'
economy2=u'商业'
economy3=u'生产'
economy4=u'产业'
economy5=u'发展'
economy6 =u'工业'
economy7 =u'工商'
economy8 =u'市场'
economy9 =u'国民'
economy10 =u'供应'

# defining the policy terms
policy1=u'财政'
policy2=u'货币'
policy3=u'证监会'
policy4=u'银监会'
policy5=u'财政部'
policy6=u'人民银行'
policy7=u'国家发改委'
policy8=u'开放'
policy9=u'改革'
policy10=u'商务部'
policy11=u'法律'
policy12=u'法规'
policy13=u'税收'
policy14=u'国债'
policy15=u'政府债务'
policy16=u'央行'
policy17=u'外经贸部'
policy18=u'关税'
policy19=u'政府赤字'

policy20=u'中共中央'
policy21=u'国务院'
policy22=u'全国人大'
policy23=u'贸易'
policy24=u'财政'
policy26=u'金融'
policy27=u'改革'
policy28=u'开放'

policy25=u'保险'
policy29=u'经贸'
policy30=u'法规'
policy31=u'法律'
policy32=u'产业'
policy33=u'监管'

policy34 = u'通货膨胀'
policy35 = u'供销'
policy36 = u'国营'
policy37 = u'党委'
policy38 = u'社队'
policy39 = u'生产队'
policy40 = u'三中全会'
policy41 = u'全国政协'
policy42 = u'公社'
policy43 = u'共产党'
policy44 = u'农村'
policy45 = u'开发'
policy46 = u'外贸'
policy47 = u'党政'
policy48 = u'检察'
policy49 = u'外汇'
policy50 = u'外商'
policy51 = u'宏观'
policy52 = u'人民币'
policy53 = u'海关'
policy54 = u'股市'
policy55 = u'失业'
policy56 = u'下岗职工'
policy57 = u'人大常委'
policy58 = u'党中央'

# defining T terms of TPU

tpolicy1=u'进口关税'
tpolicy2=u'进口税'
tpolicy3=u'进口壁垒'
tpolicy4=u'WTO'
tpolicy5=u'世界贸易组织'
tpolicy6=u'世贸组织'
tpolicy7=u'贸易条约'
tpolicy8=u'贸易协定'
tpolicy9=u'贸易政策'
tpolicy10=u'贸易法'
tpolicy11=u'多哈回合'
tpolicy12=u'乌拉圭回合'
tpolicy13=u'GATT'
tpolicy14=u'关贸总协定'
tpolicy15=u'倾销'
tpolicy16=u'保护主义'
tpolicy17=u'贸易壁垒'
tpolicy18=u'出口补贴'


# defining M terms of MPU

mpolicy1=u'银监会'
mpolicy2=u'人民银行'
mpolicy3=u'公开市场操作'
mpolicy4=u'公开市场业务'
mpolicy5=u'存款准备金'
mpolicy6=u'窗口指导'

# compile the terms
pu1=re.compile(uncertainty1)
pu2=re.compile(uncertainty2)
pu3=re.compile(uncertainty3)
pu4=re.compile(uncertainty4)
pu5=re.compile(uncertainty5)
pu6=re.compile(uncertainty6)
pu7=re.compile(uncertainty7)
pu8=re.compile(uncertainty8)
pu9=re.compile(uncertainty9)
pu10=re.compile(uncertainty10)

pe1=re.compile(economy1)
pe2=re.compile(economy2)
pe3=re.compile(economy3)
pe4=re.compile(economy4)
pe5=re.compile(economy5)
pe6=re.compile(economy6)
pe7=re.compile(economy7)
pe8=re.compile(economy8)
pe9=re.compile(economy9)
pe10=re.compile(economy10)

pp1 =re.compile(policy1)
pp2 =re.compile(policy2)
pp3 =re.compile(policy3)
pp4 =re.compile(policy4)
pp5 =re.compile(policy5)
pp6 =re.compile(policy6)
pp7 =re.compile(policy7)
pp8 =re.compile(policy8)
pp9 =re.compile(policy9)
pp10 =re.compile(policy10)
pp11 =re.compile(policy11)
pp12 =re.compile(policy12)
pp13 =re.compile(policy13)
pp14 =re.compile(policy14)
pp15 =re.compile(policy15)
pp16 =re.compile(policy16)
pp17 =re.compile(policy17)
pp18 =re.compile(policy18)
pp19 =re.compile(policy19)
pp20 =re.compile(policy20)
pp21 =re.compile(policy21)
pp22 =re.compile(policy22)
pp23 =re.compile(policy23)
pp24 =re.compile(policy24)
pp25 =re.compile(policy25)
pp26 =re.compile(policy26)
pp27 =re.compile(policy27)
pp28 =re.compile(policy28)
pp29 =re.compile(policy29)
pp30 =re.compile(policy30)
pp31 =re.compile(policy31)
pp32 =re.compile(policy32)
pp33 =re.compile(policy33)

pp34 =re.compile(policy34)
pp35 =re.compile(policy35)
pp36 =re.compile(policy36)
pp37 =re.compile(policy37)
pp38 =re.compile(policy38)
pp39 =re.compile(policy39)
pp40 =re.compile(policy40)
pp41 =re.compile(policy41)
pp42 =re.compile(policy42)
pp43 =re.compile(policy43)
pp44 =re.compile(policy44)
pp45 =re.compile(policy45)
pp46 =re.compile(policy46)
pp47 =re.compile(policy47)
pp48 =re.compile(policy48)
pp49 =re.compile(policy49)
pp50 =re.compile(policy50)
pp51 =re.compile(policy51)
pp52 =re.compile(policy52)
pp53 =re.compile(policy53)
pp54 =re.compile(policy54)
pp55 =re.compile(policy55)
pp56 =re.compile(policy56)
pp57 =re.compile(policy57)
pp58 =re.compile(policy58)


tp1 =re.compile(tpolicy1)
tp2 =re.compile(tpolicy2)
tp3 =re.compile(tpolicy3)
tp4 =re.compile(tpolicy4)
tp5 =re.compile(tpolicy5)
tp6 =re.compile(tpolicy6)
tp7 =re.compile(tpolicy7)
tp8 =re.compile(tpolicy8)
tp9 =re.compile(tpolicy9)
tp10 =re.compile(tpolicy10)
tp11 =re.compile(tpolicy11)
tp12 =re.compile(tpolicy12)
tp13 =re.compile(tpolicy13)
tp14 =re.compile(tpolicy14)
tp15 =re.compile(tpolicy15)
tp16 =re.compile(tpolicy16)
tp17 =re.compile(tpolicy17)
tp18 =re.compile(tpolicy18)

mp1=re.compile(mpolicy1)
mp2 =re.compile(mpolicy2)
mp3 =re.compile(mpolicy3)
mp4 =re.compile(mpolicy4)
mp5 =re.compile(mpolicy5)
mp6 =re.compile(mpolicy6)

#Terms for EPU, the compounded version of SCMP
spolicy1=u'政策'
spolicy2=u'支出'
spolicy3=u'预算'
spolicy4=u'政治'
spolicy5=u'利率'
spolicy6=u'改革'

sgeneral1=u'政府'
sgeneral2=u'中共中央'
sgeneral3=u'国务院'

spolicy7=u'税收'
spolicy8=u'规定'
spolicy9=u'监管'
spolicy10=u'央行'
spolicy11=u'人民银行'
spolicy12=u'赤字'
spolicy13=u'WTO'
spolicy14=u'世界贸易组织'
spolicy15=u'世贸组织'


sp1 =re.compile(spolicy1)
sp2 =re.compile(spolicy2)
sp3 =re.compile(spolicy3)
sp4 =re.compile(spolicy4)
sp5 =re.compile(spolicy5)
sp6 =re.compile(spolicy6)
sp7 =re.compile(spolicy7)
sp8 =re.compile(spolicy8)
sp9 =re.compile(spolicy9)
sp10 =re.compile(spolicy10)
sp11 =re.compile(spolicy11)
sp12 =re.compile(spolicy12)
sp13 =re.compile(spolicy13)
sp14 =re.compile(spolicy14)
sp15 =re.compile(spolicy15)

sg1 =re.compile(sgeneral1)
sg2 =re.compile(sgeneral2)
sg3 =re.compile(sgeneral3)

# a function to combine the defining and compiling keywords
def keywords(article,keyword):
    counts=[]
    for i in article:
        result=len(keyword.findall(i))
        if result>0:
            count=result
        else:
            count=0  
        counts.append(count)
    return counts
    
