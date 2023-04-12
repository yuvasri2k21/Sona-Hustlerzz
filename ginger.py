import streamlit as st
from gingerit.gingerit import GingerIt as gt
from textblob import TextBlob as tb
st.title("SPELL AND GRAMMAR CORRECTOR")
inputword=st.text_area("Text")
parser = gt()
r=parser.parse(inputword)
corrected_word = r['result']
text1 = tb(corrected_word)
result1=text1.correct()
st.text_area(result1)