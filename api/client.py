import requests
import streamlit as st

def get_ollama_response(input_text1):
    response=requests.post("http://localhost:8000/poem/invoke",json={'input':{'topic':input_text1}})
    return response.json()['output']

def get_ollama_response2(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",json={'input':{'sports':input_text}})
    return response.json()['output']

st.title('Langchain Demo With LLAMA2 API')
input_text=st.text_input("Write an essay on sports:")
input_text1=st.text_input("Write a poem on")



if input_text1:
    st.write(get_ollama_response(input_text1))
    
if input_text:
    st.write(get_ollama_response2(input_text))