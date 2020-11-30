import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.io as pio
from matplotlib import pyplot
import matplotlib.pyplot as plt

data = pd.read_csv('WHO-COVID-19-global-data.csv')
groupby = data.groupby('Country').max().reset_index()
print(groupby.head())

#column drop by cases
cases = groupby.drop(columns=['Country_code', 'Cumulative_deaths', 'WHO_region', 'New_cases', 'New_deaths'])
print(cases.head())

#column drop by deaths
deaths = groupby.drop(columns=['Country_code', 'Cumulative_cases', 'WHO_region', 'New_cases', 'New_deaths'])
print(deaths.head())



casesmap = go.Figure(data = go.Choropleth(locations = cases['Country'],
                                         z = cases['Cumulative_cases'].astype(int),
                                         locationmode = 'country names',
                                         colorscale = 'matter',
                                         colorbar_title = 'COVID cases in world map'))
casesmap.update_layout(title_text = 'COVID case counts',
                      geo = dict(showframe=False,
                                 showcoastlines=False),

                      annotations = [dict(x=0.5,
                                          y=0.1,
                                          text='COVID cases world wide',
                                          showarrow = False)])



#pyplot.show()
plot(casesmap)
