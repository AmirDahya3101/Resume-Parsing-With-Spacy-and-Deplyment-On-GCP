import streamlit as st
import docx2txt
# from tika import parser
import os
import spacy
import pandas as pd
# import docx2txt
# from PIL import Image 
# from PyPDF2 import PdfFileReader
import pdfplumber
# from pathlib import Path

# def read_pdf(file):
# 	pdfReader = PdfFileReader(file)
# 	count = pdfReader.numPages
# 	all_page_text = ""
# 	for i in range(count):
# 		page = pdfReader.getPage(i)
# 		all_page_text += page.extractText()
# 	return all_page_text

def pred(text):
    output={}
    nlp=spacy.load("model")
    text=text.replace('\n',' ')
    doc = nlp(text)
    for ent in doc.ents:
        print(f'{ent.label_.upper():{30}}-{ent.text}')
        output[ent.label_.upper()]=ent.text
    return output


st.title("Resume Parser with Spacy")
st.subheader("Upload your resume here!")
uploaded_file = st.file_uploader("Upload Files",type=['pdf','docx'])
if uploaded_file is not None:
    if st.button("Process"):
        if uploaded_file.type=='application/pdf':
            file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
            with pdfplumber.open(uploaded_file) as pdf:
                ext_txt = str()
                # st.write(len(pdf.pages))
                for i in range(len(pdf.pages)):
                    page = pdf.pages[0]
                    ext_txt += page.extract_text()
                op = pred(ext_txt)
                st.write(op)
        if uploaded_file.type=='application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
            raw_text = docx2txt.process(uploaded_file)
            op = pred(raw_text)
            st.write(op)







