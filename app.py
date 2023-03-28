import streamlit as st
import pandas as pd

"""
# フリマ分析アプリ!!!

"""

# CSVファイルの読み込み
uploaded_file = st.file_uploader("ファイルを選択してください ※csvのみ", type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if st.checkbox('データを表示'):
        st.write(df)

    if st.checkbox('グラフ表示'):
        # 列の選択
        columns = df.columns
        selected_columns = st.multiselect('表示する列を選択してください', columns)

        if selected_columns:
            # 型の混在していない列を選択
            numeric_columns = df[selected_columns].select_dtypes(['float', 'int']).columns

            # チャートの表示
            st.bar_chart(df[numeric_columns])
        else:
            st.warning('列が選択されていません。')
