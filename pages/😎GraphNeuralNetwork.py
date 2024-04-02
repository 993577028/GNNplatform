import streamlit as st
import numpy as np
import pandas as pd
import time

def ok():
    st.write('running--')

st.markdown('# GNN训练')
st.markdown('图神经网络（Graph Neural Network，简称GNN）是一种专门处理图结构数据的深度学习模型。在这种网络中，'
            '数据被表示为图（Graph），图中的节点（Node）和边（Edge）分别代表实体和实体间的关系。图神经网络通过节点'
            '和它们的邻居间的信息传递和聚合机制，能够有效捕捉和学习图结构数据的复杂关系和模式')
# Add a selectbox to the sidebar:
model_selectbox = st.sidebar.selectbox(
    'Choose a model first?',
    ('GCN', 'GAT', 'GIN','Custom')
)

option = st.selectbox(
    'Choose a dateset to train ',
    ('Cora', 'CiteSeer', 'Pubmed'))

st.write('You selected:', option)

if model_selectbox == 'Custom':
    uploaded_file = st.file_uploader("Choose a model you like")

if(st.button('start run')):
    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(50):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {2*i + 2}')
        bar.progress(2*i + 2)
        time.sleep(0.1)
    st.write('finished running')
    chart_data = pd.DataFrame(
         np.random.randn(100, 1),
         columns=['Cora'])

    st.line_chart(chart_data)
    st.write(option,'Test ACC: 87.88')
# import pandas as pd
# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })
# df
#
# dataframe = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))
#
# st.dataframe(dataframe.style.highlight_max(axis=0))
# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])
#
# st.line_chart(chart_data)

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])
#
# st.map(map_data)

# st.text_input("Your name", key="name")
#
# # You can access the value at any point with:
# st.session_state.name
#


# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })
#
# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])
#
# 'You selected: ', option



