import streamlit as st

tabs = ["Presentation", "Graphs"]
active_tab = st.sidebar.radio("Select a tab", tabs)

if active_tab == "Presentation":
    st.title("Presenation")
    option = st.selectbox(
        ' ',
        ('About', 'Graphs', 'Outlook', "Citation"))

    if option == "About":
        st.markdown('# About')
        st.markdown('### Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing layouts and visual mockups.')
    elif option == "Graphs":
        st.markdown('# Graphs ')
    elif option == "Outlook":
        st.markdown('# Outlook')
    elif option == "Citation":
        st.markdown('# Citation')
