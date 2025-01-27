from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
# from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)

llm=Ollama(model="llama3.2")

prompt1=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me an essay about {sports} in 100 words")
add_routes(
    app,
    prompt1|llm,
    path="/poem"
    
)
add_routes(
    app,
    prompt2|llm,
    path="/essay"
)

if __name__=="__main__":
    
    uvicorn.run(app,host="localhost",port=8000)