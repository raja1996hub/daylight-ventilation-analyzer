import os
from dotenv import load_dotenv

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI  # Updated import from langchain-community

# 🔐 Load environment variables from .env
load_dotenv()

# 🧠 Define analysis logic
def analyze_description(description: str) -> str:
    # Load the prompt template from file
    with open("prompt_template.txt", "r", encoding="utf-8") as f:
        template_str = f.read()

    # Create a LangChain prompt
    prompt = PromptTemplate(
        input_variables=["description"],
        template=template_str
    )

    # Initialize the LLM (ChatGPT 4 via OpenAI)
    llm = ChatOpenAI(
        temperature=0.4,
        model="gpt-4",
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    # Set up a LangChain LLMChain
    chain = LLMChain(llm=llm, prompt=prompt)

    # Run the chain with user input
    return chain.run(description=description)
