import plotly as py
import plotly.graph_objects as go


class BarChart:
    def __init__(self, data):
        self.data = data

    def draw(self, barmode, filename):
        fig = go.Figure(
            data=[
                go.Bar(
                    name=element.get("name"),
                    x=element.get("x_axis"),
                    y=element.get("y_axis"),
                )
                for element in self.data
            ]
        )

        fig.update_layout(barmode=barmode)

        py.offline.plot(fig, filename=filename)
