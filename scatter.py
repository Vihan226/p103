import pandas as pd
import plotly.express as px


df = pd.read_csv("data.csv")

#scatter method takes parameters such as the data, value for x and y, color and
# size for the markers



fig=px.scatter(df,x="More cases",y="Cases at starting of Corona",size="Percentage",color="Country",size_max=60)
fig.show()