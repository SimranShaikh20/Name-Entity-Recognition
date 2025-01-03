import streamlit as st
import spacy_streamlit as spt
import spacy

# Load the Spacy language model
nlp = spacy.load('en_core_web_sm')

st.title('Spacy Streamlit App')

def main():
    menu = ['Home', 'NER']
    choice = st.sidebar.selectbox('Menu', menu)
    
    if choice == 'Home':
        st.subheader('Word Tokenization')
        st.write('Welcome to Spacy Streamlit App')
        
        # Input text for tokenization
        raw_text = st.text_area('Text Tokenize', 'Type Here')
        if st.button('Tokenize'):
            if raw_text.strip():  # Check if the input text is not empty
                docx = nlp(raw_text)
                spt.visualize_tokens(docx, attrs=['text', 'pos_', 'dep_'])
            else:
                st.warning("Please enter some text for tokenization.")
    
    elif choice == 'NER':  # Correctly handle 'NER' choice
        st.subheader('Named Entity Recognition')
        
        # Input text for Named Entity Recognition
        raw_text = st.text_area('Text for NER', 'Type Here')
        if st.button('Show Entities'):
            if raw_text.strip():  # Check if the input text is not empty
                docx = nlp(raw_text)
                spt.visualize_ner(docx, labels=nlp.get_pipe('ner').labels)
            else:
                st.warning("Please enter some text for NER.")

# Run the main function
if __name__ == '__main__':
    main()
