import streamlit as st
st.title("Deep Impact")
st.text_input('이름을 입력하세요!', max_chars=5)   
st.text_input('오늘 하루 어떠셨나요?')  
st.text("오늘 하루 일로 인해 많이 피곤하셨군요...")
st.text('당신의 기분 전환을 위해 추천된 그림은 입니다...')   
from PIL import Image
img = Image.open("밤의 테라스.jpeg")
st.image(img, width=400, caption="Image example: Vincent Willem van Gogh(:빈센트 반 고흐)\n오늘 하루도 수고한 당신을 위한 밤의 테라스")