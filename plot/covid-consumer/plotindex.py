import pandas as pd
import plotly.express as px
from statsmodels.tsa.seasonal import seasonal_decompose
from matplotlib import pyplot



def main():
    avgWeekly = pd.read_csv('avgWeekly.csv', index_col=None, thousands=',')
    avgWeekly_seas = pd.read_csv('avgWeekly-seas.csv', index_col=None, thousands=',')
    ts1 = pd.to_datetime(avgWeekly_seas[avgWeekly_seas.columns[0]], format="%b-%y")
    avgWeekly_seas['Date'] = pd.to_datetime(avgWeekly_seas[avgWeekly_seas.columns[0]], format="%b-%y")
    avgWeekly_seas = avgWeekly_seas.set_index(ts1)
    title = 'Average weekly earnings in Canada by industry, monthly, unadjusted for seasonality'
    # plt_unfil(avgWeekly_seas, title, melt=True, write=True, fname="avgWeeklyEarnings-all.html")
    # plt_unfil(avgWeekly_seas, title, melt=True, write=True, fname="avgWeeklyEarnings_seas.html")
    seas_dff = calc_dff(avgWeekly_seas)
    title = 'Average weekly earnings in Canada by industry, monthly, differenced, filtered for increased series'
    #fig = plt(seas_dff, title)
    #fig.write_html('seas_dff_sub.html')

    calcdf = calc(avgWeekly_seas)
    plt_hist(calcdf)

    # plt_unfil(avgWeekly)
    # plt_fil(avgWeekly)
    # calcdf = calc(avgWeekly)
    # plt_hist(calcdf)
    # calcdf = calcdf.sort_values(by='percentage change (%)', ascending=False)
    # calcdf.reset_index(drop=True, inplace=True)
    # html = calcdf.to_html()
    # print('done')


def calc_dff(df):
    seas_dff = pd.DataFrame(columns=('Date', 'industry', 'value', 'last4avg'))
    for i in df.columns[1:]:
        series = df[i]
        # plt_decom(series, i)
        series2 = series.diff().dropna()
        filetitle = str('diff_' + i)
        # plt_decom(series2, filetitle)
        last2avg = sum(series2.tail(2))/2
        for j in range(0, series2.size):
            seas_dff = seas_dff.append({'Date': series2.index[j], 'industry': i,
                                        'value': series2.values[j], 'last2avg': last2avg}, ignore_index=True)
    print(seas_dff.head(3))

    seas_dff_sub = seas_dff[seas_dff['Date'] > pd.Timestamp(2020, 1, 1)]
    seas_dff_sub = seas_dff_sub[seas_dff_sub['last2avg'] > 0]
    # seas_dff_sub.to_csv('seas_dff_sub.csv')
    return seas_dff_sub


def plt_decom(series, i):
    result = seasonal_decompose(series, model='additive')
    result.plot()
    pyplot.savefig('plot/'+i+'.png')
    pyplot.close('all')
    # pyplot.show()


def plt_hist(df):
    hist = px.histogram(df, x="percentage change (%)",
                        color_discrete_sequence=px.colors.sequential.Plasma,
                        width=400, height=300, nbins=20,
                        title='Histogram of percentage changes in weekly earnings since January 2020, by Industry')
    hist.update_layout(plot_bgcolor='white')
    hist.show()
    hist.write_html('hist_earnings.html')


def calc(df):
    df2 = pd.DataFrame(columns=['industry', 'percentage change (%)'], index=None)
    for i in df.columns[1:]:
        first = float(df[i][0])
        last = float(df[i][df.index[-1]])
        perc = (last - first) / first * 100
        data = {'industry': i, 'percentage change (%)': perc}
        df2 = df2.append(data, ignore_index=True)
    return df2


def plt_fil(df, title, melt):
    cols = []
    anti_cols = []
    for i in df.columns[1:]:
        first = float(df[i][0])
        last = float(df[i][df.index[-1]])
        if first < last:
            cols.append(i)
        else:
            anti_cols.append(i)
    cols.append('Date')
    avgWeeklyfil = df[cols]
    if melt == True:
        df = avgWeeklyfil.melt(id_vars=['Date'], var_name='industry')
    # title = 'Average weekly earnings in Canada by industry, monthly, unadjusted for seasonality--filtered for increased'
    fig = plt(df, title)
    #fig.write_html("avgWeeklyEarnings-increase.html")
    fig.show()
    print(anti_cols)



def plt_unfil(df, title, melt, write, fname):
    if melt == True:
        df = df.melt(id_vars=['Date'], var_name='industry')
    #title = 'Average weekly earnings in Canada by industry, monthly, unadjusted for seasonality'
    fig = plt(df, title)
    fig.show()
    if write == True:
        fig.write_html(fname)


def plt(df, title):

    fig = px.line(df, x='Date', y='value',
                  color='industry',
                  width=900, height=500,
                  color_discrete_sequence=px.colors.sequential.Plasma)
    fig.update_traces(mode='markers+lines')
    fig.update_layout(
        xaxis=dict(
            showgrid=False
        ),
        yaxis=dict(
            showgrid=False
        ),
        autosize=True,
        margin=dict(
            autoexpand=True,
            l=100,
            r=20,
            t=110,
        ),
        showlegend=False,
        plot_bgcolor='white',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    annotations = []
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                            xanchor='left', yanchor='bottom',
                            text=title,
                            font=dict(family='Arial',
                                      size=18,
                                      color='rgb(37,37,37)'),
                            showarrow=False))
    fig.update_layout(annotations=annotations)

    return fig


if __name__ == '__main__':
    main()