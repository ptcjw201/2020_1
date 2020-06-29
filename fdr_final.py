import matplotlib.pyplot as plt
import FinanceDataReader as fdr
from sklearn.linear_model import LinearRegression
import statistics
import numpy as np
import math
#Q1
def Q1():
    df_KOSPI = fdr.StockListing('KOSPI')
    df_KOSDAQ = fdr.StockListing('KOSDAQ')
    KOSPI = df_KOSPI['Symbol']
    KOSDAQ = df_KOSDAQ['Symbol']
    print(KOSPI)
    print(KOSDAQ)



#Q2
def Q2():
    df = fdr.DataReader('005930','2018-01-01','2018-12-31')
    plt.plot(df['Change'],'g')
    plt.xlabel('Date')
    plt.ylabel('Change')
    plt.show()



#Q3
def Q3():
    df_KOSPI = fdr.StockListing('KOSPI')
    df_KOSDAQ = fdr.StockListing('KOSDAQ')
    KOSPI = df_KOSPI['Symbol']
    KOSDAQ = df_KOSDAQ['Symbol']
    means_of_KOSPI = []
    means_of_KOSDAQ = []
    sd_of_KOSPI = []
    sd_of_KOSDAQ = []
    for i in KOSPI:
        new_df = fdr.DataReader(i,'2018','2019')
        if (new_df.empty):
            continue
        else:
            new_df = new_df.dropna(axis = 0)
            means_of_KOSPI.append(statistics.mean(new_df['Change']))
            sd_of_KOSPI.append(statistics.stdev(new_df['Change']))
    for j in KOSDAQ:
        new_df2 = fdr.DataReader(j,'2018','2019')
        if(new_df2.empty):
            continue
        else:
            new_df2 = new_df2.dropna(axis = 0)
            means_of_KOSDAQ.append(statistics.mean(new_df2['Change']))
            sd_of_KOSDAQ.append(statistics.stdev(new_df2['Change']))
    plt.subplot(221)
    plt.scatter(means_of_KOSPI,sd_of_KOSPI,s = 1)
    plt.subplot(222)
    plt.scatter(means_of_KOSDAQ,sd_of_KOSDAQ, s = 1)
    plt.show()

#Q4
def Q4():
    df_KOSPI = fdr.StockListing('KOSPI')
    df_KOSDAQ = fdr.StockListing('KOSDAQ')
    KOSPI = df_KOSPI['Symbol']
    KOSDAQ = df_KOSDAQ['Symbol']
    x_axis_KOSPI = []
    x_axis_KOSDAQ = []
    means_of_KOSPI = []
    means_of_KOSDAQ = []
    df_KOSPI200 = fdr.DataReader('KS200','2018','2019')
    rf = 0.03/365
    feat = []
    fit_a_KOSPI = []
    fit_b_KOSPI = []
    fit_a_KOSDAQ = []
    fit_b_KOSDAQ = []

    for j in df_KOSPI200['Change']:
        feat.append(j - rf)


    for i in KOSPI:
        new_df = fdr.DataReader(i,'2018','2019')
        if (new_df.empty):
            continue
        else:
            target = []
            for k in new_df['Change']:
                target.append(k-rf)

        if (len(feat) == len(target)):
            x_axis_KOSPI.append(i)
            fit_a_KOSPI.append(np.polyfit(feat,target,1)[1])
            fit_b_KOSPI.append(np.polyfit(feat,target,1)[0])
#making means of KOSPI
    for i in x_axis_KOSPI:
        new_df = fdr.DataReader(i,'2018','2019')
        means_of_KOSPI.append(statistics.mean(new_df['Change']))


    for i in KOSDAQ:
        new_df = fdr.DataReader(i, '2018', '2019')
        if (new_df.empty):
            continue
        else:
            target = []
            for k in new_df['Change']:
                target.append(k - rf)

        if (len(feat) == len(target)):
            x_axis_KOSDAQ.append(i)
            fit_a_KOSDAQ.append(np.polyfit(feat, target, 1)[1])
            fit_b_KOSDAQ.append(np.polyfit(feat, target, 1)[0])

    for i in x_axis_KOSDAQ:
        new_df = fdr.DataReader(i,'2018','2019')
        means_of_KOSDAQ.append(statistics.mean(new_df['Change']))



    plt.subplot(211)
    plt.scatter(means_of_KOSPI, fit_b_KOSPI, s=1)
    plt.subplot(212)
    plt.scatter(means_of_KOSDAQ, fit_b_KOSDAQ, s=1)
    plt.show()

#Q5
def Q5():
    df_KOSPI = fdr.StockListing('KOSPI')
    df_KOSDAQ = fdr.StockListing('KOSDAQ')
    KOSPI = df_KOSPI['Symbol']
    KOSDAQ = df_KOSDAQ['Symbol']
    cumsum_of_KOSPI = []
    dict_of_KOSPI = {}
    dict_of_KOSDAQ = {}
    list_of_3month_change_KOSPI = []
    list_of_6month_change_KOSPI = []
    list_of_3month_change_KOSDAQ = []
    list_of_6month_change_KOSDAQ = []
    cumsum_of_KOSDAQ = []
    for i in KOSPI:
        df_for_0629_KOSPI = fdr.DataReader(i,'2018-06-29', '2018-06-29')
        df_for_0102_KOSPI = fdr.DataReader(i, '2018-01-02', '2018-01-02')
        if bool('Change' in df_for_0102_KOSPI) & bool('Change' in df_for_0629_KOSPI):
            close_0629_KOSPI = df_for_0629_KOSPI['Close']
            close_0102_KOSPI = df_for_0102_KOSPI['Close']
            #close가 series임
            if close_0102_KOSPI.empty or close_0629_KOSPI.empty:
                continue
            else:
                cumx  = (float(close_0629_KOSPI)-float(close_0102_KOSPI))/float(close_0102_KOSPI)
            dict_of_KOSPI[i] = cumx
    dict_of_KOSPI = dict(sorted(dict_of_KOSPI.items(),key = lambda x:x[1]))
    n = int(len(dict_of_KOSPI)/10)
    #10개의 그룹으로 세분화
    groups_of_KOSPI = [list(dict_of_KOSPI.keys())[i * n:(i + 1) * n] for i in range((len(list(dict_of_KOSPI.keys())) + n - 1) // n)]
    for j in groups_of_KOSPI:
        for k in j:
            df_for_0928_KOSPI = fdr.DataReader(k,'2018-09-28','2018-09-28')
            df_for_0702_KOSPI = fdr.DataReader(k,'2018-07-02','2018-07-02')
            df_for_1228_KOSPI = fdr.DataReader(k,'2018-12-28','2018-12-28')

            if bool('Change' in df_for_0702_KOSPI) & bool('Change' in df_for_0928_KOSPI) & bool('Change' in df_for_1228_KOSPI):
                close_0928_KOSPI = df_for_0928_KOSPI['Close']
                close_0702_KOSPI = df_for_0702_KOSPI['Close']
                close_1228_KOSPI = df_for_1228_KOSPI['Close']
                if close_0702_KOSPI.empty or close_0928_KOSPI.empty or close_1228_KOSPI.empty:
                    continue
                else:
                    cum_change_3_KOSPI = (float(close_0928_KOSPI) - float(close_0702_KOSPI)) / float(close_0702_KOSPI)
                    cum_change_6_KOSPI = (float(close_1228_KOSPI) - float(close_0702_KOSPI)) / float(close_0702_KOSPI)
                list_of_3month_change_KOSPI.append(cum_change_3_KOSPI)
                list_of_6month_change_KOSPI.append(cum_change_6_KOSPI)

    n = int(math.ceil((len(list_of_3month_change_KOSPI)/10)))
    m = int(math.ceil((len(list_of_6month_change_KOSPI)/10)))
    groups_of_3monthchange_KOSPI = [list_of_3month_change_KOSPI[i * n:(i + 1) * n] for i in range((len(list_of_3month_change_KOSPI) + n - 1) // n)]
    groups_of_6monthchange_KOSPI = [list_of_6month_change_KOSPI[i * m:(i + 1) * m] for i in range((len(list_of_6month_change_KOSPI) + m - 1) // m)]


    for i in range(len(groups_of_3monthchange_KOSPI)):
        groups_of_3monthchange_KOSPI[i] = statistics.mean(groups_of_3monthchange_KOSPI[i])
    for i in range(len(groups_of_6monthchange_KOSPI)):
        groups_of_6monthchange_KOSPI[i] = statistics.mean(groups_of_6monthchange_KOSPI[i])


    for j in KOSDAQ:
        df_for_0629_KOSDAQ = fdr.DataReader(j,'2018-06-29', '2018-06-29')
        df_for_0102_KOSDAQ = fdr.DataReader(j, '2018-01-02', '2018-01-02')
        if bool('Change' in df_for_0102_KOSDAQ) & bool('Change' in df_for_0629_KOSDAQ):
            close_0629_KOSDAQ = df_for_0629_KOSDAQ['Close']
            close_0102_KOSDAQ = df_for_0102_KOSDAQ['Close']
            #close가 series임
            if close_0102_KOSDAQ.empty or close_0629_KOSDAQ.empty:
                continue
            else:
                cumx2  = (float(close_0629_KOSDAQ)-float(close_0102_KOSDAQ))/float(close_0102_KOSDAQ)
            dict_of_KOSDAQ[j] = cumx2
    dict_of_KOSDAQ = dict(sorted(dict_of_KOSDAQ.items(),key = lambda x:x[1]))
    m = int(len(dict_of_KOSDAQ)/10)
    #10개의 그룹으로 세분화
    groups_of_KOSDAQ = [list(dict_of_KOSDAQ.keys())[i * m:(i + 1) * m] for i in range((len(list(dict_of_KOSDAQ.keys())) + m - 1) // m)]
    for j in groups_of_KOSDAQ:
        for k in j:
            df_for_0928_KOSDAQ = fdr.DataReader(k,'2018-09-28','2018-09-28')
            df_for_0702_KOSDAQ = fdr.DataReader(k,'2018-07-02','2018-07-02')
            df_for_1228_KOSDAQ = fdr.DataReader(k,'2018-12-28','2018-12-28')

            if bool('Change' in df_for_0702_KOSDAQ) & bool('Change' in df_for_0928_KOSDAQ) & bool('Change' in df_for_1228_KOSDAQ):
                close_0928_KOSDAQ = df_for_0928_KOSDAQ['Close']
                close_0702_KOSDAQ = df_for_0702_KOSDAQ['Close']
                close_1228_KOSDAQ = df_for_1228_KOSDAQ['Close']
                if close_0702_KOSDAQ.empty or close_0928_KOSDAQ.empty or close_1228_KOSDAQ.empty:
                    continue
                else:
                    cum_change_3_KOSDAQ = (float(close_0928_KOSDAQ) - float(close_0702_KOSDAQ)) / float(close_0702_KOSDAQ)
                    cum_change_6_KOSDAQ = (float(close_1228_KOSDAQ) - float(close_0702_KOSDAQ)) / float(close_0702_KOSDAQ)
                list_of_3month_change_KOSDAQ.append(cum_change_3_KOSDAQ)
                list_of_6month_change_KOSDAQ.append(cum_change_6_KOSDAQ)

    n = int(math.ceil((len(list_of_3month_change_KOSDAQ)/10)))
    m = int(math.ceil((len(list_of_6month_change_KOSDAQ)/10)))
    groups_of_3monthchange_KOSDAQ = [list_of_3month_change_KOSDAQ[i * n:(i + 1) * n] for i in range((len(list_of_3month_change_KOSDAQ) + n - 1) // n)]
    groups_of_6monthchange_KOSDAQ = [list_of_6month_change_KOSDAQ[i * m:(i + 1) * m] for i in range((len(list_of_6month_change_KOSDAQ) + m - 1) // m)]

    for i in range(len(groups_of_3monthchange_KOSDAQ)):
        groups_of_3monthchange_KOSDAQ[i] = statistics.mean(groups_of_3monthchange_KOSDAQ[i])
    for i in range(len(groups_of_6monthchange_KOSDAQ)):
        groups_of_6monthchange_KOSDAQ[i] = statistics.mean(groups_of_6monthchange_KOSDAQ[i])

    lb = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th']
    x_values1 = [2* element + (0.8) for element in range(0,10)]
    x_values2 = [2* element + (0.8)*2 for element in range(0,10)]


    middle_x = [(a + b)/2 for (a,b) in zip(x_values1, x_values2)]
    plt.subplot(211)
    plt.bar(x_values1, groups_of_3monthchange_KOSPI)
    plt.bar(x_values2, groups_of_6monthchange_KOSPI)
    plt.xticks(middle_x, lb)
    plt.subplot(212)
    plt.bar(x_values1, groups_of_3monthchange_KOSDAQ)
    plt.bar(x_values2, groups_of_6monthchange_KOSDAQ)
    plt.xticks(middle_x, lb)
    plt.show()

def main():
#    Q1()
#    Q2()
#    Q3()
#    Q4()
#    Q5()
    return 0

main()