# 导入必要的库
import hydralit_components as hc  # 导入Hydralit组件库

import webbrowser

# import platform  # 导入platform库，用于获取系统平台信息
# import pandas as pd  # 导入pandas库，用于数据处理
# import requests  # 导入requests库，用于发送HTTP请求
import streamlit as st  # 导入Streamlit库，用于创建Web应用
# import streamlit_analytics
from streamlit_modal import Modal  # 导入streamlit_modal库，用于创建模态窗口
# import streamlit_lottie  # 导入streamlit_lottie库，用于加载Lottie动画
# import time  # 导入time库，用于时间相关操作
# import json  # 导入json库，用于处理JSON数据

# 导入自定义页面函数
from navigation.start import start_page  # 导入
# from navigation.contact import contact_page  # 导入contact_page函数
from navigation.home import home_page  # 导入home_page函数
from navigation.setting import setting_page  # 导入resource_page函数
from utils.components import footer_style, footer  # 导入自定义组件

# 尝试从streamlit导入rerun函数
try:
    from streamlit import rerun as rerun
except ImportError:
    # 针对streamlit版本<1.27进行条件导入
    from streamlit import experimental_rerun as rerun

import os  # 导入os库，用于操作系统相关功能


# # 定义加载Lottie文件的函数
# def load_lottiefile(filepath: str):
#     with open(filepath, "r") as f:
#         return json.load(f)


# 设置页面配置
st.set_page_config(
    page_title='声华SingHeart',  # 设置页面标题
    page_icon="images/logo蓝底新.png",  # 设置页面图标
    initial_sidebar_state="auto"  # 设置初始侧边栏状态为展开
)

# # 初始化会话状态中的'lottie'变量
# if 'lottie' not in st.session_state:
#     st.session_state.lottie = False

# 如果会话状态中的'lottie'变量为False
# if not st.session_state.lottie:
#     lottfinder = load_lottiefile(".streamlit/TFinder_logo_animated.json")  # 加载Lottie动画文件
#     st.lottie(lottfinder, speed=1.3, loop=False)  # 显示Lottie动画
#     time.sleep(2)  # 等待2秒
#     st.session_state.lottie = True  # 将会话状态中的'lottie'变量设置为True
#     rerun()  # 重新运行应用

max_width_str = f"max-width: {75}%;"  # 设置最大宽度为75%

# 使用markdown设置页面样式
st.markdown(f"""
        <style>
        .appview-container .main .block-container{{{max_width_str}}}
        </style>
        """,
            unsafe_allow_html=True,
            )

# 使用markdown设置页面样式
st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;

                }
        </style>
        """, unsafe_allow_html=True)

# 页脚
st.markdown(footer_style, unsafe_allow_html=True)  # 使用markdown设置页脚样式

# 导航栏
# 导航栏
HOME = '首页'
START = '开始转换'
SETTING = '参数设置'


# 定义选项卡
tabs = [
    HOME,
    START,
    SETTING,
]
#
# 定义选项数据
option_data = [
    {'icon': "🏠", 'label': HOME},
    {'icon': "🖥️", 'label': START},
    {'icon': "📑", 'label': SETTING},
]

# 定义主题样式
over_theme = {'txc_inactive': 'black', 'menu_background': '#D6E5FA', 'txc_active': 'white', 'option_active': '#749BC2'}
font_fmt = {'font-class': 'h3', 'font-size': '50%'}

# ----------------------------------------生成导航--------------------------------------------------------
chosen_tab = hc.option_bar(
    option_definition=option_data,
    title='',
    key='PrimaryOptionx',
    override_theme=over_theme,
    horizontal_orientation=True)
# 显示问候信息
st.success("欢迎来到声华SingHeart！让你的声音成为艺术！融合高效架构算法，精准挖掘音频信息，智能塑造声音轨迹2024,Singheart助力歌声音色转换迈向端到端合成新时代")
# 根据选择的选项卡显示相应页面
if chosen_tab == HOME:
    home_page()
elif chosen_tab == START:
    start_page()
elif chosen_tab == SETTING:
    setting_page()


# ---------------------------#页面之下---------------------------------------------------------
# 为了美观，添加空白行
# for i in range(15):
#     st.markdown('#')
# st.markdown(footer, unsafe_allow_html=True)  # 使用markdown设置页脚

# streamlit_analytics.start_tracking()

# 显示侧边栏中的logo
st.sidebar.image("images/lo800.png")

# 侧边栏帮助标题

with st.sidebar.expander("关于我们"):
    st.subheader("深藏blu战队")  # 响应元素子标题
    st.write('成立于2023年12月，致力于歌声音色转化算法构建和定制化音色服务，团队致力于整合优化业内相关算法，提供低门槛，效果清晰自然音色高度仿真的综合音色转化服务')  # 对于单个基序：允许使用IUPAC代码
with st.sidebar.expander("获得帮助"):
    if st.button('打开教程'):
        webbrowser.open_new_tab('https://blog.csdn.net/dakeaia/article/details/137719731')
with st.sidebar.expander("联系我们"):
    st.subheader("联系方式：")  # 响应元素子标题
    st.write('邮箱:SingHeart@163.com')
    st.write('电话：19968447505')


# 侧边栏更多标题
st.sidebar.title("More")
# 侧边栏中的链接：报告错误
st.sidebar.markdown(
    "[反馈bug 🐞](https://github.com/da-keai/-SingHeart/issues/1)")
# 侧边栏中的链接：有问题
st.sidebar.markdown(
    "[提问题 🤔](https://github.com/da-keai/-SingHeart/issues/2)")
# 侧边栏中的链接：功能请求
st.sidebar.markdown(
    "[功能请求 💡](https://github.com/da-keai/-SingHeart/issues/3)")

# streamlit_analytics.stop_tracking()
# views = streamlit_analytics.main.counts["total_pageviews"]


# 创建模态窗口
modal = Modal(key="TFinder Key", title="欢迎您来到SingHeart声华", padding=50, max_width=900)

# 初始化会话状态中的'popup_closed'变量
if 'popup_closed' not in st.session_state:
    st.session_state.popup_closed = False

# 如果会话状态中的 'popup_closed' 变量为 False
if not st.session_state.popup_closed:
    with modal.container():  # 使用模态框容器
        st.markdown('')  # 空的 Markdown
        st.markdown(
            'SingHeart声华将严格遵守相关法律法规，保护用户的个人隐私和数据安全')
        # st.error("⚠ NCBI 服务器维护，请勿使用提取工具")

        value = st.checkbox(
            "勾选此框，即表示您同意SingHeart声华数据使用政策")  # 同意数据使用政策的复选框
        if value:
            st.button('关闭')  # 关闭按钮
            st.session_state.popup_closed = True  # 将会话状态中的 'popup_closed' 变量设置为 True

