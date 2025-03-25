import re

uncertainty_terms = [u'不确定', u'不明确', u'不明朗', u'未明', u'难料', 
                     u'难以预计', u'难以估计', u'难以预测', u'难以预料', '未知']
uncertainty_terms_regex = [re.compile(term) for term in uncertainty_terms]

economy_terms = [u'经济', u'商业', u'生产', u'产业', u'发展',
                 u'工业', u'工商', u'市场', u'国民', u'供应']
economy_terms_regex = [re.compile(term) for term in economy_terms]

policy_terms = [u'财政', u'货币', u'证监会', u'银监会', u'财政部', u'人民银行', u'国家发改委', u'开放', u'改革', u'商务部',
                u'法律', u'法规', u'税收', u'国债', u'政府债务', u'央行', u'外经贸部', u'关税', u'政府赤字', u'中共中央',
                u'国务院', u'全国人大', u'贸易', u'财政', u'金融', u'改革', u'开放', u'保险', u'经贸', u'法规',
                u'法律', u'产业', u'监管', u'通货膨胀', u'供销', u'国营', u'党委', u'社队', u'生产队', u'三中全会',
                u'全国政协', u'公社', u'共产党', u'农村', u'开发', u'外贸', u'党政', u'检察', u'外汇', u'外商', 
                u'宏观', u'人民币', u'海关', u'股市', u'失业', u'下岗职工', u'人大常委', u'党中央']
policy_terms_regex = [re.compile(term) for term in policy_terms]

trade_policy_terms = [u'进口关税', u'进口税', u'进口壁垒', u'WTO', u'世界贸易组织', u'世贸组织', u'贸易条约', u'贸易协定', u'贸易政策', 
                      u'贸易法', u'多哈回合', u'乌拉圭回合', u'GATT', u'关贸总协定', u'倾销', u'保护主义', u'贸易壁垒', u'出口补贴']
trade_policy_terms_regex = [re.compile(term) for term in trade_policy_terms]

monetary_policy_terms = [u'银监会', u'人民银行', u'公开市场操作',
                         u'公开市场业务', u'存款准备金', u'窗口指导']
monetary_policy_terms_regex = [re.compile(term) for term in monetary_policy_terms]

scmp_policy_terms = [u'政策', u'支出', u'预算', u'利率', u'改革', u'税收', u'规定', u'监管', u'央行',
                     u'人民银行', u'赤字', u'WTO', u'世界贸易组织', u'世贸组织']
scmp_policy_terms_regex = [re.compile(term) for term in scmp_policy_terms]

scmp_general_terms = [u'政府', u'中共中央', u'国务院']
scmp_general_terms_regex = [re.compile(term) for term in scmp_general_terms]

def keywords(articles, keyword):
    counts = []
    for i in articles:
        counts.append(max(0, len(keyword.findall(i))))
    return counts