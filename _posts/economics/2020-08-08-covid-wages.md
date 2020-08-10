---
layout: blog
istop: false
title: "The Covid19 Earnings Increase"
background-image: /static/img/posts/avgEarningsCovid.png
date:  2020-08-08 21:21:35
category: macro-economics
tags:
- macro-economics
- covid19
---

Here's the graph that shows average earnings in early 2020, during the Covid19 pandemic. 

<iframe id="graph1" title="Graph Satu" height="510" width="910" src="/plot/covid-consumer/avgWeeklyEarnings_seas.html"> </iframe>

<iframe id="hist_earnings" title="Graph Dua" height="300" width="400" src="/plot/covid-consumer/hist_earnings.html"> </iframe>

This below table shows that some industries experiences markedly higher earnings comparing between Jan 2020 and April 2020. 

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>industry</th>
      <th>percentage change (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Arts, entertainment and recreation  [71]</td>
      <td>20.930486</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Other services (except public administration)  [81]</td>
      <td>13.888404</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Accommodation and food services  [72]</td>
      <td>11.866031</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Real estate and rental and leasing  [53]</td>
      <td>11.469977</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Service producing industries  [41-91N]11</td>
      <td>10.996668</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Finance and insurance  [52]</td>
      <td>10.635954</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Educational services  [61,611]</td>
      <td>9.344954</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Trade  [41-45N]12</td>
      <td>8.978605</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Industrial aggregate excluding unclassified businesses  [11-91N]7 8</td>
      <td>8.463375</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Information and cultural industries  [51]</td>
      <td>6.718517</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Health care and social assistance  [62]</td>
      <td>6.009989</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Public administration  [91]</td>
      <td>3.538237</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Administrative and support, waste management and remediation services  [56]</td>
      <td>3.076553</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Management of companies and enterprises  [55,551,5511]</td>
      <td>1.684338</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Transportation and warehousing  [48-49]</td>
      <td>1.154531</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Construction  [23]</td>
      <td>-0.219625</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Professional, scientific and technical services  [54,541]</td>
      <td>-0.488498</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Goods producing industries  [11-33N]9</td>
      <td>-1.743873</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Manufacturing  [31-33]</td>
      <td>-2.379657</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Mining, quarrying, and oil and gas extraction  [21]</td>
      <td>-2.529256</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Utilities  [22,221]</td>
      <td>-6.120585</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Forestry, logging and support  [11N]10</td>
      <td>-9.167047</td>
    </tr>
  </tbody>
</table>


However, the seasonality of the data might be causing this issue. For example, construction has the 
<a href="/plot/covid-consumer/plot/Construction.png" data-lightbox="iframe">lowest earnings in January</a>, and the 
highest in the fall. Accommodation and food services <a href="/plot/covid-consumer/plot/Accommodation and food services.png" 
data-lightbox="iframe">hits th peak in year end</a>, and finds the environment quietest in January. Educational Services 
 on another hand, perhaps quite surprisingly, <a href="/plot/covid-consumer/plot/Educational services.png" 
data-lightbox="iframe">does the best around spring</a>. 



<iframe id="differenced-avgWeeklyEarnings" height="410" width="810" title="Differenced Average Weekly Earnings Graph" src="/plot/covid-consumer/seas_dff_sub.html"> </iframe>



