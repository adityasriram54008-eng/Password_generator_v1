import streamlit as st
import functions

st.set_page_config(layout='wide')
st.title(":green[_Password_] Generator", text_alignment = "center")

st.header(":green[_Instructions_]:")

st.text("1. Enter a password length of at least 4 characters.")
st.text("2. Enter only a positive whole number for the password length i.e  >=4.")
st.text("3. Select at least one character type to include in your password.")
st.text("4. The number of selected character types must not exceed the password length.")

st.header(":green[_How It Works_]:")

st.subheader("Step 1: Choose the Length")
st.text("Enter the desired password length.")

st.subheader("Step 2: Select Components")
st.text("Choose the character types you want to include in your password.")

st.subheader("Step 3: Generate")
st.text("The generator first adds one character from each selected type.")
st.text("It then randomly selects additional characters until the password reaches the requested length.")

st.text("\n")
st.text("\n")

with st.container(gap="small"):
    st.subheader(":green[_Enter Length_]:")
    l = st.text_input("", width=100, key = "len")

if l:
    v = True
    for i in l:
        if not i.isdecimal():
            v = False
            break

    if v:
        l = int(l)
        if l < 4:
            st.error("Password length must be greater than or equal to 4.")
        else:
            st.subheader(":green[_COMPONENTS_]")
            with st.container(border = True, width = 400):
                col1, col2 = st.columns(2,width = 400)
                with col1:
                    u_checkbox = st.checkbox("Uppercase", key = "uc")
                    l_checkbox = st.checkbox("Lowercase", key = "lc")
                with col2:
                    n_checkbox = st.checkbox("Numbers", key = "nc")
                    ss_checkbox = st.checkbox("Special Characters", key = "sc")

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

                    while gen < l:
                        gen = functions.randomizer(selected,gen)

                    functions.write_("\n")

                    dis = functions.display()
                    st.write(dis)
    else:
        st.error("Length should be an integer >= 4")