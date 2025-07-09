from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOPenAI
from langchain_anthropic import ChatAnthopic 

load_dotenv()

llm = ChatOPenAI(model='gpt-4o-mini')
llm2 = ChatAnthopic(model='claude-3-5-so')

