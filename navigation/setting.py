import streamlit as st

TEST = "TFinder makes it easy to extract gene regulatory regions by simply providing the gene name or its Gene ID " \
       "(<strong>Fig.1 Step 1.1, Fig.2, Fig.3</strong>). We have added an option to check if the gene is accessible for each species (\"Check genes availability\" button <strong>Fig.2</strong>). Since the ID gene already takes in account the species, it is not necessary to configure the species analyzed. This also implies that you are not limited to the five species proposed by the program. However, if you use the gene name, then the species will be required (<strong>Fig.1 Step 1.1 and 1.2</strong>). TFinder allows mixing of gene name and gene ID. Please select the desired species. You can therefore easily compare the same regulatory region of 2 or more different species with the gene ID for the same gene."


def setting_page():

    slider1 = st.slider(label="变调数值", min_value=0.0, max_value=1.0, value=0.5, step=0.01,
                        help="范围：0~1，默认值：0.5")
    slider2 = st.slider(label="重采样值", min_value=0, max_value=48000, value=40000, step=50,
                        help="范围：0~48000，默认值：40000")
    slider3 = st.slider(label="中值滤波", min_value=0.0, max_value=7.0, value=3.0, step=0.1,
                        help="范围：0~7，默认值：3")
    slider4 = st.slider(label="包络比例", min_value=0.0, max_value=1.0, value=0.0, step=0.01,
                        help="范围：0~1，默认值：0")
    slider5 = st.slider(label="检索特征占比", min_value=0.0, max_value=1.0, value=0.75, step=0.01,
                        help="范围：0~1，默认值：0.75")
    slider6 = st.slider(label="防止电音撕裂", min_value=0.0, max_value=0.5, value=0.0, step=0.01,
                        help="范围：0~0.5，默认值：0")

    # updown_slide = st.slider("🔹 :blue[**不懂**] 大可爱",
    #                          -10000, 10000, (-2000, 2000), step=100,label="dakeai")


