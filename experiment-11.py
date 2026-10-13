!pip install -q -U langchain langchain-core langchain-google-genai google-genai
----------------------------------------------------------------------------------------------
import os
from google.colab import userdata

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

print("All libraries imported successfully")
---------------------------------------------------------------------------------------------
import os

os.environ["GOOGLE_API_KEY"] = userdata.get("GEMINI_API_KEY")

print("Gemini API key configured")
----------------------------------------------------------------------------------------------
prompt = ChatPromptTemplate.from_template(
    "Write a very short story (2-3 sentences) about {topic}."
)
----------------------------------------------------------------------------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0
)
------------------------------------------------------------------------------------------
parser = StrOutputParser()

chain = prompt | llm | parser

print("LCEL chain created successfully")
--------------------------------------------------------------------------------------------
topics = [
    "a dragon and a knight",
    "a lost spaceship"
]

sample_stories = {
    "a dragon and a knight":
        "A brave knight met a friendly dragon. Together, they saved the kingdom.",
    "a lost spaceship":
        "A spaceship lost its way in space. The crew discovered a new planet and found a way home."
}

for topic in topics:
    story = sample_stories[topic]

    print("Topic:", topic)
    print("Story:", story)
    print()
