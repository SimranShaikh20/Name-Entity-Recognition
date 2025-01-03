import streamlit as st
import spacy_streamlit as spt
import spacy
nlp=spacy.load('en_core_web_sm')

st.title('Spacy Streamlit App')
def main():
    menu=['Home','NER']
    choice=st.sidebar.selectbox('Menu',menu)
    if choice=='Home':
        st.subheader('Word Tokenization')
        st.write('Welcome to Spacy Streamlit App')
        raw_text=st.text_area('Text Tokenize','Type Here')
        docx=nlp(raw_text)
        if st.button('Tokenize'):
            spt.visualize_tokens(docx,attrs=['text','pos_','dep_'])
    else:
        choice=='NER'   
        st.subheader('Named Entity Recognition')
        raw_text=st.text_area('Text To Tokenize','Type Here')
        docx=nlp(raw_text)
        spt.visualize_ner(docx,labels=nlp.get_pipe('ner').labels)
                