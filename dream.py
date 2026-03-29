import streamlit as st
from openai import OpenAI

# 1. 页面标题
st.title("🔮 王公解梦")

# 2. 侧边栏配置（只需输入一次 API Key）
with st.sidebar:
    api_key = st.text_input("输入 API Key", type="password")
    base_url = st.text_input("API 代理地址", value="https://api.deepseek.com")

# 3. 输入梦境
dream_input = st.text_area("输入你的梦境：", height=200, placeholder="昨晚梦到了什么？")

# 4. 点击出结果
if st.button("开始解梦", type="primary"):
    if not api_key:
        st.error("请先在左侧输入 API Key")
    elif not dream_input:
        st.warning("请输入梦境描述")
    else:
        with st.spinner("正在解析..."):
            try:
                client = OpenAI(api_key=api_key, base_url=base_url)
                response = client.chat.completions.create(
                    model="deepseek-chat", 
                    messages=[
                        {"role": "system", "content": "你是一位专业的解梦专家，名字叫王公。请简明扼要地解析用户梦境的含义。"},
                        {"role": "user", "content": dream_input}
                    ]
                )
                # 直接输出解释内容
                st.markdown("---")
                st.subheader("王公解释：")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"解析出错：{e}")
