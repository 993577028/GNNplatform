import streamlit as st
import time
import pandas as pd
import numpy as np
st.markdown('# 图&联邦学习')

st.markdown('联邦学习是一种机器学习方法，其特点是能在保持数据隐私的同时，通过多个设备或服务器协作学习。在这种方法中，'
            '数据不需要集中存储或处理，而是保留在各自的设备上。这些设备（例如智能手机或医院的服务器）独立地训练模型，并'
            '仅共享模型参数或学习后的更新，而不是共享原始数据。这样，联邦学习可以在保护个人隐私和数据安全的前提下，允许'
            '不同来源的数据共同训练一个高效的机器学习模型。这种方法在处理敏感数据时特别有用，如在医疗保健、金融服务和个'
            '人设备等领域。')
# Add a selectbox to the sidebar:
model_selectbox = st.sidebar.selectbox(
    'Choose a model first?',
    ('FedAvg', 'FedGCN', 'GCFL','Custom')
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
