
from langchain_ollama import ChatOllama
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()
HF_TOKEN=os.getenv("HF_TOKEN")

class TranslateRequest(BaseModel):
    text:str
    provider: str="ollama"

@app.post("/translate")
def ask_question(data:TranslateRequest):

    print("INPUT FROM STREAMLIT:", data.text)
    
    translate_template=PromptTemplate(
        input_variables=["text"],
        template="""
        You are a professional translator.
        Translate the following text into German, French and Persian.

        Rules:
        - Use natural translations used by native speakers.
        - Do not translate word by word.
        - Understand the meaning from the context.
        - Preserve the original meaning and tone.
        - Choose the most common and natural expression in each language.
        - Avoid awkward or overly literal translations.
        - For Persian, use natural modern Persian.
        - Give only the translations. Do not add explanations.
        - For Persian, prefer simple and natural spoken Persian when appropriate.

        text:
        {text}

        use exactly this format:

        German:
        <translation>

        French:
        <translation>

        Persian:
        <translation>

        """
    )
 
    

    def get_llm(provider ="ollama"):
        if provider == "huggingface":
            llm=HuggingFaceEndpoint(
            repo_id="Qwen/Qwen2.5-7B-Instruct",
            huggingfacehub_api_token=HF_TOKEN,
            temperature=0,
            )
            return ChatHuggingFace(llm=llm)
        
        elif provider =="ollama":
            return  ChatOllama(
                model="qwen2.5:3b",
                temperature=0,
    ) 

    chat=get_llm(data.provider)

    chain= translate_template|chat|StrOutputParser()   

    translate_text=chain.invoke({"text": data.text})

    return translate_text
