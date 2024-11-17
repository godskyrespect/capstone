import streamlit as st
from pymongo import MongoClient

# MongoDB 연결 설정
MONGO_URI = "mongodb://localhost:27017"  # MongoDB URI
client = MongoClient(MONGO_URI)
db = client["myDatabase"]  # 데이터베이스 이름
collection = db["posts"]  # 컬렉션 이름

# Streamlit 애플리케이션 시작
st.title("Streamlit와 MongoDB 연동")
st.write("사용자가 작성한 글을 MongoDB에 저장합니다.")

# 입력 폼
with st.form("entry_form"):
    title = st.text_input("글 제목", max_chars=100)
    content = st.text_area("글 내용")
    submit_button = st.form_submit_button("저장")

# 저장 버튼 클릭 시 MongoDB에 저장
if submit_button:
    if title and content:
        post = {
            "title": title,
            "content": content,
        }
        collection.insert_one(post)  # MongoDB에 저장
        st.success("글이 성공적으로 저장되었습니다!")
    else:
        st.error("제목과 내용을 모두 입력해주세요!")

# 저장된 글 표시
st.write("### 저장된 글")
posts = list(collection.find().sort("_id", -1))  # 최신 글부터 정렬
for post in posts:
    st.subheader(post["title"])
    st.write(post["content"])
    st.write("---")
