import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re

# CSV 파일 읽기
csv_file_path = 'app/assets/dashboard_data.csv'
df = pd.read_csv(csv_file_path)

# 시간 형식 변환 함수
def convert_time(time_str):
    days = hours = minutes = 0
    day_match = re.search(r'(\d+)d', time_str)
    hour_match = re.search(r'(\d+)h', time_str)
    minute_match = re.search(r'(\d+)m', time_str)

    if day_match:
        days = int(day_match.group(1))
    if hour_match:
        hours = int(hour_match.group(1))
    if minute_match:
        minutes = int(minute_match.group(1))

    return days * 24 * 60 + hours * 60 + minutes

# 시간 데이터를 분 단위로 변환
df['time_since_prelaunched_minutes'] = df['time_since_prelaunched'].apply(convert_time)

# 타임스탬프를 datetime 형식으로 변환
df['timestamp'] = pd.to_datetime(df['timestamp'])

# 대시보드 구현
def app():
    st.title("Analytics Dashboard")

    # 원본 데이터 표시
    st.subheader("Original Data")
    st.dataframe(df)

    # 시간 경과와 좋아요 수의 관계 그래프
    st.subheader("Time Since Prelaunched vs. Liked Count")
    fig, ax = plt.subplots()
    ax.plot(df['time_since_prelaunched_minutes'], df['liked_count'], marker='o', linestyle='-')
    ax.set_xlabel("Time Since Prelaunched (minutes)")
    ax.set_ylabel("Liked Count")
    st.pyplot(fig)

    # 타임스탬프와 좋아요 수의 관계 그래프
    '''
    st.subheader("Timestamp vs. Liked Count")
    fig, ax = plt.subplots()
    ax.plot(df['timestamp'], df['liked_count'], marker='o', linestyle='-')
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Liked Count")
    st.pyplot(fig)
    '''