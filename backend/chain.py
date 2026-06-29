from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from backend.config import GROQ_API_KEY, MODEL_NAME, TEMPERATURE, MAX_TOKENS
from backend.prompt import referee_prompt

# LLM
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model_name=MODEL_NAME,
    temperature=TEMPERATURE,
    max_tokens=MAX_TOKENS
)

# Chain: prompt → llm → string output
referee_chain = referee_prompt | llm | StrOutputParser()


def get_verdict(person1: str, person2: str) -> str:
    return referee_chain.invoke({
        "person1": person1,
        "person2": person2
    })