# Bring in deps
import os 
from apikey import apikey 

# application framework
import streamlit as st 
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
from langchain_community.utilities import WikipediaAPIWrapper 

os.environ['OPENAI_API_KEY'] = apikey

# App framework
st.title('ScriptGPT')
prompt = st.text_input('Enter prompt from your video script here') 

# Prompt template - create new prompt template.
# the topic will be passed to the template
title_template = PromptTemplate(
    input_variables = ['topic'], 
    template='write me a youtube video title about {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title', 'wikipedia_research'], 
    template='write me a youtube video script based on this title TITLE: {title} while leveraging this wikipedia reserch:{wikipedia_research} '
)

# Memory 
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')


# Llms
llm = OpenAI(temperature=0.9) 
#create chain for title template 
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)

# simple sequential chain only outputs the last output on the chain.
# sequential_chain = SimpleSequentialChain(chains = [title_chain, script_chain], verbose=True)

# sequential chain fixes the issue.
# sequential_chain = SequentialChain(chains = [title_chain, script_chain], input_variables=['topic'], output_variables=['title, script'], verbose=True)    


wiki = WikipediaAPIWrapper()

# Show stuff to the screen if there's a prompt
if prompt: 
    # response = sequantial_chain.run(topic=prompt)
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt) 
    script = script_chain.run(title=title, wikipedia_research=wiki_research)

    st.write(title) 
    st.write(script) 

# insert chat history
    with st.expander('Title History'): 
        st.info(title_memory.buffer)

    with st.expander('Script History'): 
        st.info(script_memory.buffer)

    with st.expander('Wikipedia Research'): 
        st.info(wiki_research)