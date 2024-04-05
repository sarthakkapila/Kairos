# Kairos

## Getting Started
To get started with Kairos, follow these steps:

1. Clone the repository: `git clone https://github.com/sarthakkapila/kairos.git`
2. Go to main dir: `cd kairos`
3. Create virtual env: `python -m venv kairos`
4. Activate virtual env: `Source kairos/bin/activate` (for windows): `kairos/Scripts/activate`
4. Install dependencies: `pip install -r requirements.txt`

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


## Team members - 100X-Devs
- Sarthak Kapila (22107038)
- Shauray Dhingra (22107060)
- Karanveer Singh (22101003)