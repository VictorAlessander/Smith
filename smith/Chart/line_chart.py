import plotly as py
import plotly.graph_objects as go


class LineChart:
    def __init__(self, data):
        self.data = data

    def draw(self, chart_name, filename):
        content = []
        for element in self.data:
            trace = go.Scatter(
                x=element.get("x_axis"),
                y=element.get("y_axis"),
                name=element.get("name"),
            )

            content.append(trace)

        layout = go.Layout(title=chart_name)

        fig = go.Figure(data=content, layout=layout)

        py.offline.plot(fig, filename=filename)
