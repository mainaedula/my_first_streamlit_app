import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd
import altair as alt

st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)

st.code(
'''
x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last

x_axis = np.arange(0,x_limit,1)

# Create a random array of data that we will use for our y values

y_data = np.random.rand(100)


df = pd.DataFrame({'x': x_axis,
                     'y': y_data})

st.write(df)

''',language='python')

x_limit = 100

x_axis = np.arange(0,x_limit,1)

y_data = np.random.rand(100)


df = pd.DataFrame({'x': x_axis,
                     'y': y_data})

st.write(df)


st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)

st.code(
''' 
scatter = alt.Chart(df).mark_point().encode(
    x='x', y='y'
)

st.altair_chart(scatter, use_container_width=True)
''',language='python')

scatter = alt.Chart(df).mark_point().encode(
    x='x', y='y'
)

st.altair_chart(scatter, use_container_width=True)


st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)


st.markdown("""
The 5 changes I made were:
- Data points are orange in color
- Selector changes point color to red when clicked
- Interactive so you can zoom in and out
- Tooltip that shows x and y values upon hover
- Added title 
""")


selector = alt.selection(type="single", empty='none')

scatter = alt.Chart(df, title = "First streamlit scatter plot").mark_point().encode(
    x='x', y='y', 
    color= alt.condition(
        selector, # replace the previous condition with the selector
        alt.value("darkred"),
        alt.value("orange")),
    tooltip = ['x','y']
).add_selection(
    selector
    ).interactive()

st.altair_chart(scatter, use_container_width=True)

st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)

st.markdown("""
The 2 changes I made were:
- Added title
- Added tooltip showing data for each bar upon hover
"""
)

source = pd.read_json("wheat.json")

chart1 = alt.Chart(source).mark_bar().encode(
    x='year:O',
    y="wheat:Q",
    # The highlight will be set on the result of a conditional statement
    color=alt.condition(
        alt.datum.year == 1810,  # If the year is 1810 this test returns True,
        alt.value('orange'),     # which sets the bar orange.
        alt.value('steelblue')   # And if it's not true it sets the bar steelblue.
    )
).properties(width=600)

st.altair_chart(chart1, use_container_width=True)



chart2 = alt.Chart(source, title = "Wheat Production from 1565-1820").mark_bar().encode(
    x='year:O',
    y="wheat:Q",
    # The highlight will be set on the result of a conditional statement
    color=alt.condition(
        alt.datum.year == 1810,  # If the year is 1810 this test returns True,
        alt.value('orange'),     # which sets the bar orange.
        alt.value('steelblue')   # And if it's not true it sets the bar steelblue.
    ),
    tooltip = ['year', 'wheat']
).properties(width=600)

st.altair_chart(chart2, use_container_width=True)

