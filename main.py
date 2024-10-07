import streamlit as st
from Scrape import scrape_website,split_dom_content,clean_body_content,extract_body_content
from parse import parse_with_ollama
st.title("Web Scarper")
url = st.text_input("Enter the Website URL:")

if st.button("Scrape Site"):
    st.write("Scrapping the Website")
    result = scrape_website(url)
    print(result)
    body_content = extract_body_content(result)
    clean_content = clean_body_content(body_content)

    st.session_state.dom_content = clean_content

    with st.expander("View Dom Content"):
        st.text_area("DOM Content :",clean_content,height=100)

if "dom_content" in st.session_state:
    parse_dec = st.text_area("Describe what you want to parse")

    if st.button("Parse_Content"):
        if parse_dec:
            st.write("Parsing the content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks,parse_dec)
            st.write(result)