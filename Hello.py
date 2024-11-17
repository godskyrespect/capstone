import streamlit as st
 
st.set_page_config(
    page_title="Hello, Infomatics Class!",
    page_icon="👋",
)
 
st.write("# 정보수업 오리엔테이션 사이트 👋")
 
st.sidebar.success("메뉴를 선택하세요.")
 
st.markdown(
    """
    시작하기에 앞서!!!! 이걸 어떻게 만들었냐면... 
    👈 좌측 사이드바에서 메뉴를 고르세요!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)