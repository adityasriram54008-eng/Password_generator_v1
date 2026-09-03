import streamlit as st
import random as rd
import functions

st.set_page_config(layout='wide')
st.title("Password Generator")

l = st.text_input("Enter length")

if l:
    l = int(l)

    st.subheader("COMPONENTS")
    u_checkbox = st.checkbox("Uppercase", key = "uc")
    l_checkbox = st.checkbox("Lowercase", key = "lc")
    n_checkbox = st.checkbox("Numbers", key = "nc")
    ss_checkbox = st.checkbox("Special Characters", key ="ss")

    if st.button("GENERATE", type = "primary"):
        if u_checkbox:
            functions.get_ul(l)
        if l_checkbox:
            functions.get_ll(l)
        if n_checkbox:
            functions.get_n(l)
        if ss_checkbox:
            functions.get_ss(l)
        dis = functions.display()
        st.write(dis)












