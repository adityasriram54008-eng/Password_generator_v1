import streamlit as st
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

    gen = 0
    check = 0
    selected = []

    if st.button("GENERATE", type = "primary"):
        if u_checkbox:
            check += 1
            selected.append("uc")
            gen = functions.get_ul(gen)
        if l_checkbox:
            check += 1
            selected.append("lc")
            gen = functions.get_ll(gen)
        if n_checkbox:
            check += 1
            selected.append("n")
            gen = functions.get_n(gen)
        if ss_checkbox:
            check += 1
            selected.append("sc")
            gen = functions.get_ss(gen)

        if check == gen:
            while gen < l:
                    gen = functions.randomizer(selected,gen)

        dis = functions.display()
        st.write(dis)












