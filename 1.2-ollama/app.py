import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set")

os.environ["OPENAI_API_KEY"] = openai_api_key

from langchain_community.llms import Ollama 
import streamlit as st 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true" 
os.environ["LANGCHAIN_PROJECT" ]=os.getenv( "LANGCHAIN_PROJECT")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are helpful assistant. Please respond to the question asked."),
        ("user","Question:{question}")
    ]
)

st.title("Langchain demo")
input_text=st.text_input("What question you have in mind?")
llm=Ollama(model="gemma:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))