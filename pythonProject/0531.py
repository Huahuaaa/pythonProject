import datetime
time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
time2 = datetime.datetime.now().strptime('20220531', '%Y%m%d')
# 单行注释1
# 单行注释2
print(time1)
'''
多行注释1
多行注释2
'''
print(time2)
"""
多行注释3
多行注释4
"""