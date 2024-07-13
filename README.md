# Kairos

> [!IMPORTANT]
> App works best when installed locally!

## Getting Started 
To get started with Kairos, follow these steps:
## Tech Stack
- Langchain
- Streamlit
- Gemini API
- Jinja2 for prompt templating
- Bs4 & googlesearch api for scraping
- KeyBERT for keyword extraction
- Streamlit share for deployment
  
## Local Installation 
1. Clone the repository: `git clone https://github.com/sarthakkapila/kairos.git`
2. Go to main dir: `cd kairos`
3. Create virtual env: `python -m venv kairos`
4. Activate virtual env: `source kairos/bin/activate` (for windows): `kairos/Scripts/activate`
4. Install all dependencies: `pip install -r requirements.txt`

## Product Demo 
- [Kairos Demo Video](https://app.supademo.com/embed/clune6g8803vu4r8tlrbbf6nj)
- [Kairos Live Link](https://kairos-ai.streamlit.app/)

> [!IMPORTANT]
> Please reload the demo 1 or 2 times for it to work properly.

## High level system design of the app 
### Workflow of kairos

The high level workflow is divided into different steps.
The user selects a base model, for now Gemini-Pro & ollama (probably).
When provided with the api. The user is directed to workspace page where they input a prompt. 

### DecisonTaker 
The input prompt given by the user is processed and the DecisionTaken agent determines the course of action.
We have divided the DecisonTaker into 2 types of queries i.e. 
- Code-related 
- Non Code-related

Currently we have limited the non-code related queries.

### Planner
Kairos generates a step-by-step plan using Planner agent, which is then presented visually,
Step Formulation: Drawing from the objective and context, Kairos devises a series of broad steps to achieve the task.


### Keyword-Extractor
The prompt's keywords are extracted as the name suggests.
To extract the keywords we have employed BERT model which divides the prompt into nuances and find significance behind the words within.
Working of bert: the Bert model is used to extract the keywords and rank them based on their relevance to the user's prompt.
Kairos then pinpoints each part performs a research on it using Researcher Agent , retrieving information for task.


### Researcher
Researcher agent maintain search queries, which expands its knowledge base.
Based on the contextual keywords extracted above, Kairos creates helpful search queries that can be emplyed with the googlesearch-py.
Then the requests module is used to fetch the web pages of the queries.
Using the beautifulsoup library, we extract the content from the web pages for processing.

### Browser
Then, Kairos conducts internet searches based on queries, The info is then present in JSON format (For now) in browser tab. 

### Coder Agent
The Coder agent then utilizes the plan and acquired information to write code.
Then, the code generation module crafts code based on the planner, researcher, & taking in consider user prompts/specs. 
High level design -> 
Drawing from the planner, it constructs the foundational code, including classes fn etc.
Then the rest of the code including algos, data etc are added which were extrated from research, the knowledge repo, thus code is produced.

### Creator Agent
Finally, Kairos's Creator agent generates and executes Python code to create and organize project directory and & different files.

Following the code generation, Kairos initiates the creation of a Python script utilizing the os module.
Then it begins organizing the project files and folders generated previously during the coding phase of the project.

## Screenshots
<img width="938" alt="Screenshot 2024-04-06 at 11 01 44 PM" src="https://github.com/sarthakkapila/Kairos/assets/112886451/29e25360-5207-45ae-9a46-7e95608057dd">
<img width="997" alt="Screenshot 2024-04-06 at 11 02 08 PM" src="https://github.com/sarthakkapila/Kairos/assets/112886451/3ecff9dd-8a29-4c40-8020-09be12f95067">
<img width="1534" alt="Screenshot 2024-04-06 at 11 03 28 PM" src="https://github.com/sarthakkapila/Kairos/assets/112886451/2fcd2886-ed49-4f35-8cb5-f259f44bf9d5">
<img width="787" alt="Screenshot 2024-04-06 at 11 09 06 PM" src="https://github.com/sarthakkapila/Kairos/assets/112886451/38754847-f2b5-48b9-a907-f2560ff0347c">
<img width="704" alt="Screenshot 2024-04-06 at 11 08 29 PM" src="https://github.com/sarthakkapila/Kairos/assets/112886451/c205438e-0906-47f5-8be1-b43d1ef32f45">
<img width="725" alt="Screenshot 2024-04-06 at 11 08 41 PM" src="https://github.com/sarthakkapila/Kairos/assets/112886451/6b1ab81b-a280-4a73-9e7c-6f44edffdef6">
<img width="727" alt="Screenshot 2024-04-06 at 11 08 51 PM" src="https://github.com/sarthakkapila/Kairos/assets/112886451/28e6a7b3-e585-4042-b7e9-aea08ef4fe16">
<img width="817" alt="Screenshot 2024-04-06 at 11 09 28 PM" src="https://github.com/sarthakkapila/Kairos/assets/112886451/46b454b0-e2f6-4b87-be83-2675154817a5">
<img width="779" alt="Screenshot 2024-04-06 at 11 09 22 PM" src="https://github.com/sarthakkapila/Kairos/assets/112886451/b68dbb69-b626-41e8-8cc5-df002f51b8a3">
<img width="889" alt="Screenshot 2024-04-06 at 7 25 20 AM" src="https://github.com/sarthakkapila/Kairos/assets/112886451/ee1eceb6-7859-4793-9247-df9b1a00d220">
<img width="787" alt="Screenshot 2024-04-06 at 11 09 16 PM" src="https://github.com/sarthakkapila/Kairos/assets/112886451/31fa45f6-d05a-4977-ac12-2d4f8e1d0f7f">
