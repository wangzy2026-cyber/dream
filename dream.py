import streamlit as st
from openai import OpenAI

# 1. 页面配置
st.title("🔮 王公解梦")

# 2. 自动从 Secrets 获取灵力（不再显示在左侧）
# 只要你在 Streamlit Cloud 的 Secrets 里填了 API_KEY 和 BASE_URL，这里就能直接运行
try:
    client = OpenAI(
        api_key = st.secrets["API_KEY"],
        base_url = st.secrets.get("BASE_URL", "https://api.deepseek.com")
    )
except Exception as e:
    st.error("王公提示：Secrets 配置未读取成功，请检查后台设置。")
    st.stop()

# 3. 主界面：直接输入梦境
dream_input = st.text_area("输入你的梦境：", height=200, placeholder="昨晚梦到了什么？")

if st.button("开始解梦", type="primary"):
    if not dream_input:
        st.warning("请先描述你的梦境。")
    else:
        with st.spinner("王公正在感应..."):
            try:
                response = client.chat.completions.create(
                    model="deepseek-chat", 
                    messages=[
                        {"role": "system", "content": "你是一位专业的解梦专家，名字叫王公。请简明扼要地解析用户梦境的含义。"},
                        {"role": "user", "content": dream_input}
                    ]
                )
                st.markdown("---")
                st.subheader("王公解释：")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"解析失败：{e}")
