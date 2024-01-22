import pandas as pd
import plotly.express as px
import random

colors_list = ['indianred']

class DataFrameGeneral():

    def __init__(self, df) -> None:
        self.df_1 = df
        self.df_2 = None
        self.df_3 = None

    def profiler_start(self):
        df_1 = self.df_1
        attributes_dict = dict()
        for i in df_1.columns:
            attributes_dict[i] = {'count': df_1[i].count(),
                                'null_values': df_1[i].isnull().sum(),
                                'unique_values': df_1[i].drop_duplicates().count()}
            if str(df_1[i].dtype).startswith('int') or str(df_1[i].dtype).startswith('float'):
                attributes_dict[i].update({"mean": df_1[i].mean(), "std": df_1[i].std(), 'min':df_1[i].min(), 'max':df_1[i].max()})
                plotly_figure = px.histogram(df_1, x=i, width=300, height=200, template='simple_white', text_auto=True, color_discrete_sequence=[random.choice(colors_list)])
                plotly_figure.update_yaxes(visible=False, showticklabels=False).update_xaxes(
                visible=False, showticklabels=False).update_layout(margin=dict(l=0, r=0, t=0, b=0),paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)')
                attributes_dict[i].update({"histogram":plotly_figure})
            else:
                values_counter = df_1[i].value_counts() / df_1[i].notnull().sum()
                values_counter = values_counter.to_frame().reset_index().rename(columns={'count':'value'})
                other_sum = values_counter[values_counter[values_counter.columns[1]] < 0.1][values_counter.columns[1]].sum()
                chart_df = values_counter[values_counter['value'] > 0.1]
                if chart_df.shape[0] != 0:
                    if other_sum > 0:
                        append_df = pd.DataFrame([['Other Values', other_sum]], columns=[chart_df.columns[0],chart_df.columns[1]])
                        chart_df = pd.concat([chart_df, append_df])
                    attributes_dict[i].update({"histogram_table": chart_df})
                    plotly_figure = px.pie(chart_df, values=chart_df.columns[1], names=chart_df.columns[0],
                                        template='simple_white',width=300, height=200)
                    plotly_figure.update_layout(margin=dict(l=0, r=0, t=0, b=0),paper_bgcolor='rgba(0,0,0,0)',
                    )
                    attributes_dict[i].update({"histogram":plotly_figure})
                self.profiler = attributes_dict

class DataFrameModif(DataFrameGeneral):
    pass

class DataFrameFilter(DataFrameGeneral):
    pass