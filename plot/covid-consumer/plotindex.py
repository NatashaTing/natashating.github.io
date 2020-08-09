import pandas as pd
import plotly.express as px


def main():
    avgWeekly = pd.read_csv('avgWeekly.csv', index_col=None, thousands=',')
    # plt_unfil(avgWeekly)
    # plt_fil(avgWeekly)
    calcdf = calc(avgWeekly)
    plt_hist(calcdf)
    calcdf = calcdf.sort_values(by='percentage change (%)', ascending=False)
    calcdf.reset_index(drop=True, inplace=True)
    html = calcdf.to_html()
    print('done')


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


def plt_fil(df):
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
    df = avgWeeklyfil.melt(id_vars=['Date'], var_name='industry')
    title = 'Average weekly earnings in Canada by industry, monthly, unadjusted for seasonality--filtered for increased'
    fig = plt(df, title)
    fig.write_html("avgWeeklyEarnings-increase.html")
    print(anti_cols)



def plt_unfil(df):
    df1 = df.melt(id_vars=['Date'], var_name='industry')
    title = 'Average weekly earnings in Canada by industry, monthly, unadjusted for seasonality'
    fig = plt(df1, title)
    fig.show()
    fig.write_html("avgWeeklyEarnings-all.html")



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