import streamlit as st
from pymongo import MongoClient

# MongoDB URI
# MONGO_URI = "mongodb+srv://jsheek93:cokeos1987@cluster0.7pdc1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MONGO_URI = "mongodb+srv://jsheek:episode1234@cluster0.7pdc1.mongodb.net/"

# MongoDB 연결
client = MongoClient(MONGO_URI)
db = client["myDatabase"]  # 데이터베이스 이름
collection = db["posts"]  # 컬렉션 이름

# Streamlit 앱 UI
st.title("MongoDB 연결 테스트")
st.write("Streamlit과 MongoDB 연동해보기히얏호우")

# 입력 폼
with st.form("entry_form"):
    title = st.text_input("글 제목")
    content = st.text_area("글 내용")
    submitted = st.form_submit_button("저장")

# 데이터 저장
if submitted:
    if title and content:
        post = {"title": title, "content": content}
        collection.insert_one(post)  # MongoDB에 데이터 삽입
        st.success("글이 성공적으로 저장되었습니다!")
    else:
        st.error("모든 필드를 입력해주세요!")

# 저장된 데이터 출력
st.write("### 저장된 글")
posts = collection.find().sort("_id", -1)  # 최신 데이터부터 출력
for post in posts:
    st.subheader(post["title"])
    st.write(post["content"])
    st.write("---")
