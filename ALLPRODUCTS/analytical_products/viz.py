import streamlit as st
import plotly.express as px
class viz_class:
    def viz_app(df):
        # Add a title
        st.title("Data Visualization App")
        # Select chart type
        chart_type = st.selectbox("Select chart type:", options=['line', 'scatter', 'area', 'bar', 'box', 'histogram', 'pie', 'sunburst', 'heatmap'])
    
        # Select X-axis column
        x_column = st.selectbox("Select X-axis column:", options=list(df.columns))
        if x_column == '':
            st.warning("Please select an X-axis column")
        else:
            # Create a Plotly chart based on the selected type
            try:
                if chart_type == 'line':
                    fig = px.line(df, x=x_column)
                elif chart_type == 'scatter':
                    fig = px.scatter(df, x=x_column)
                elif chart_type == 'area':
                    fig = px.area(df, x=x_column)
                elif chart_type == 'bar':
                    fig = px.bar(df, x=x_column)
                elif chart_type == 'box':
                    fig = px.box(df, x=x_column)
                elif chart_type == 'histogram':
                    fig = px.histogram(df, x=x_column)
                elif chart_type == 'pie':
                    fig = px.pie(df, values=x_column)
                elif chart_type == 'sunburst':
                    fig = px.sunburst(df, path=[x_column])
                elif chart_type == 'heatmap':
                    fig = px.imshow(df.corr())
                elif chart_type == 'scatter_3d':
                    fig= px.scatter_3d(df, x=x_column, y='Index', z='Index')
        
                # Select Y-axis column if chart type allows it
                if chart_type in ['scatter', 'line', 'area', 'bar', 'box', 'scatter_3d']:
                    y_column = st.selectbox("Select Y-axis column (optional):", options=[''] + list(df.columns))
                    if y_column != '':
                        fig.update_layout(yaxis_title=y_column)
                        fig.update_traces(y=df[y_column])
        
                # Select color column if chart type allows it
                if chart_type in ['scatter', 'line', 'area', 'bar', 'box', 'scatter_3d']:
                    color_column = st.selectbox("Select color column (optional):", options=[''] + list(df.columns))
                    if color_column != '':
                        fig.update_traces(marker=dict(color=df[color_column]))
        
                # Select size column if chart type allows it
                if chart_type in ['scatter', 'line', 'area', 'bar']:
                    size_column = st.selectbox("Select size column (optional):", options=[''] + list(df.columns))
                    if size_column != '':
                        fig.update_traces(marker=dict(size=df[size_column]))
        
                # Select hover column if chart type allows it
                if chart_type in ['scatter', 'line', 'area', 'bar', 'box', 'scatter_3d']:
                    hover_column = st.selectbox("Select hover column (optional):", options=[''] + list(df.columns))
                    if hover_column != '':
                        fig.update_traces(hovertemplate=' '.join(['%{hovertext}', '%{x}',f'%{y_column}' if y_column else '', f'%{color_column}' if color_column else '', f'%{size_column}' if size_column else '', f'%{hover_column}' if hover_column else '']))
                if chart_type in ['scatter']:
                    symbol_column = st.selectbox("Select symbol column (optional):", options=[''] + list(df.columns))
                    if symbol_column != '':
                        fig.update_traces(mode='markers', marker=dict(symbol=df[symbol_column]))
            except ValueError as error:
                st.warning(error.args[0][40:50])
    
        # Display the chart
        st.plotly_chart(fig)
                                                             
