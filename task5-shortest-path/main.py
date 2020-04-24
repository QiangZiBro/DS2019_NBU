# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

# 1.准备数据
places = {
    '山东': [117.000923, 36.675807],
    '河北': [115.48333, 38.03333],
    '吉林': [125.35000, 43.88333],
    '黑龙江': [127.63333, 47.75000],
    '辽宁': [123.38333, 41.80000],
    '内蒙古': [111.670801, 41.818311],
    '新疆': [87.68333, 43.76667],
    '甘肃': [103.73333, 36.03333],
    '宁夏': [106.26667, 37.46667],
    '山西': [112.53333, 37.86667],
    '陕西': [108.95000, 34.26667],
    '河南': [113.65000, 34.76667],
    '安徽': [117.283042, 31.86119],
    '江苏': [119.78333, 32.05000],
    '浙江': [120.20000, 30.26667],
    '福建': [118.30000, 26.08333],
    '广东': [113.23333, 23.16667],
    '江西': [115.90000, 28.68333],
    '海南': [110.35000, 20.01667],
    '广西': [108.320004, 22.82402],
    '贵州': [106.71667, 26.56667],
    '湖南': [113.00000, 28.21667],
    '湖北': [114.298572, 30.584355],
    '四川': [104.06667, 30.66667],
    '云南': [102.73333, 25.05000],
    '西藏': [91.00000, 30.60000],
    '青海': [96.75000, 36.56667],
    '天津': [117.20000, 39.13333],
    '上海': [121.55333, 31.20000],
    '重庆': [106.45000, 29.56667],
    '北京': [116.41667, 39.91667],
    '台湾': [121.30, 25.03],
    '香港': [114.10000, 22.20000],
    '澳门': [113.50000, 22.20000],
}
logs = []
lats = []
names = []
for k, v in places.items():
    names.append(k)
    logs.append(v[0])
    lats.append(v[1])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# 2 画图三部曲
trace = list()
trace.append(
    go.Scattermapbox(
        mode="markers",
        text=names,
        lon=logs,
        lat=lats,
        marker={'size': 10},
        # marker_color='red'
    )
)

fig = go.Figure(data=trace)
fig.update_layout(
    margin={'l': 3, 't': 3, 'b': 3, 'r': 3},
    mapbox={
        'center': {'lon': places['河南'][0], 'lat': places['河南'][1]},
        'style': "stamen-terrain",
        'zoom': 3
    },
)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    html.H1(id="title", children="中国地图"),  # 1
    dcc.Graph(  # 2
        id='example-graph',
        figure=fig  # 地图从这里传入
    ),
    html.Div(id="div", children="")  # 3

])


def solve_shortest_path():
    print("shortest path solving")
    return None


two_points = []  # 需要选择两个点
SELECTED = ""


def selectPoint(point, double_points):
    if len(double_points) == 1 and double_points[0] == point:
        return
    else:
        double_points.append(point)
        print("Points you selected:{}".format(point))


@app.callback(
    Output('div', 'children'),
    [Input('example-graph', 'clickData')])
def display_click_data(clickData):
    global two_points, SELECTED
    if clickData:
        point_dict = clickData['points'][0]
        lon = point_dict['lon']
        lat = point_dict['lat']
        text = point_dict['text']

        selectPoint([lon, lat], two_points)
        SELECTED += "{}:({},{})   ".format(text, lon, lat)
        MSG = "您选择了" + SELECTED

        if len(two_points) == 2:
            solve_shortest_path()
            two_points = []
            SELECTED = ""

        return MSG
    else:
        return "请选择两个点"


if __name__ == '__main__':
    app.run_server(debug=True, port=8052)
