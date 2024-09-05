import streamlit as st  # type: ignore
from langchain_core.output_parsers import StrOutputParser # type: ignore
from langchain_core.prompts import ChatPromptTemplate # type: ignore
from langchain_community.llms import Ollama # type: ignore


import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

## Langsmith Tracking

os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Q&A Chatbot With Ollama"

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helful assistant. Please response to the user queries"),
        ("user", "Question:{question}")
    ]
)

def generate_response(question,engine,temperature,max_tokens):
    llm=Ollama(model=engine)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

## Title of the app
st.title("Enhanced Q&A Chatbot With Ollama")
    
## Sidebar for settings
st.sidebar.title("Settings")
    
## Drop down to select various  models of ollama
engine= st.sidebar.selectbox("Select an Ollama model",["llama3.1"])


    
## Adjust response parameter
temperature = st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max Tokens", min_value=50,max_value=300,value=150)
    
## Main interface 
st.write("Go ahead and ask the question")
user_input=st.text_input("You:")

if user_input:
    response=generate_response(user_input, engine, temperature,max_tokens)
    st.write(response)
    
else:
    st.write("Please provide the user input")
    

    
    
                                 
