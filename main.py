import streamlit as st
import functions

st.set_page_config(layout='wide')
st.title(":green[_Password_] Generator", text_alignment = "center")

st.text("\n")
st.text("\n")
st.text("\n")

l = st.text_input("Enter length: ", width = 100)

if l:
    l = int(l)
    if l < 4:
        st.error("Password length must be greater than or equal to 4.")
    else:
        st.subheader("COMPONENTS")
        with st.container(border = True, width = 400):
            col1, col2 = st.columns(2,width = 400)
            with col1:
                u_checkbox = st.checkbox("Uppercase")
                l_checkbox = st.checkbox("Lowercase")
            with col2:
                n_checkbox = st.checkbox("Numbers")
                ss_checkbox = st.checkbox("Special Characters")

        gen = 0
        check = 0
        selected = []

        if st.button("GENERATE", type = "primary", icon = "⚡️"):

            if not any([u_checkbox, l_checkbox, n_checkbox, ss_checkbox]):
                st.error("Please select at least one component.")

            else:

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












