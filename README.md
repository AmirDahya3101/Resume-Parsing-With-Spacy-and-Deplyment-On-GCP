# Capstone-Resume-Parser-Group1
Building a Resume Parser in Python using NLP (SpaCy library) and deploying the model on a GCP using Streamlit application.

# INTRODUCTION
Resume parsing is the process of converting a resume into a structured format for easy management and analysis. With the increasing use of technology in the recruitment process, resumes are being received in large volumes, making it difficult for recruiters to manually read and sort through them. This is where resume parsing comes into play, as it helps to automate the process and streamline the recruitment process.

# PROJECT OBJECTIVE
The objective of this project is to build a resume parser using Natural Language Processing (NLP) techniques and the SpaCy library in Python. The parser will extract relevant information such as education, work experience, and skills from resumes in an organized manner. Additionally, the model will be deployed on the Google Cloud Platform (GCP) using the Streamlit application, making it accessible and user-friendly for recruiters.

# PROJECT DESCRIPTION
## PROBLEM STATEMENT:
The recruitment process can be time-consuming and tedious, especially when dealing with a large volume of resumes. Recruiters often struggle with manually sorting through resumes, looking for relevant information, and matching the candidate's skills with the requirements of the job. This leads to a longer recruitment process, which can impact the business's overall productivity.

## PROJECT SIGNIFICANCE:
The resume parser project will provide a solution to the problem of manual resume sorting, enabling recruiters to quickly and efficiently sort through resumes and identify the most suitable candidates. This will result in a more streamlined recruitment process, reducing the time and effort required and ultimately increasing the productivity of the business.

## PROPOSED SOLUTION:
The proposed solution is to build a resume parser using NLP techniques and the SpaCy library in Python. The parser will extract relevant information such as education, work experience, and skills from resumes in a structured format. Additionally, the model will be deployed on the GCP using the Streamlit application, making it accessible and user-friendly for recruiters.

## STEPS INVOLVED IN THE PROJECT:
1.	Developing a Python-based NLP model that can extract key information (or entities) from resumes using Spacy
2.	Training the model using a large dataset of resumes
3.	Building a web-based application using a web framework (e.g., Flask, Django) that can accept resumes in various formats (e.g., PDF, Word, etc.) and parse the information using the trained model
4.	Integrating the application with a cloud-based platform (such as Google Cloud Platform) for deployment
5.	Providing an easy-to-use interface for recruiters to access the parsed information and match it with the job requirements

## KNOWLEDGE/SKILLS/TECH NEEDED:
1. Knowledge of natural language processing (NLP) concepts such Tokenization, Lemmatization, Parts-of-Speech Tagging etc.
2. Python programming language
3. SpaCy library
4. Google Cloud Platform (GCP)
5. Streamlit application
6. Data cleaning and preprocessing techniques
7. Basic knowledge of machine learning algorithms and deployment processes.

## COMPARISON TO EXISTING SOLUTIONS:
There are a number of existing resume parsing solutions on the market, but our solution stands out in its use of the Spacy NLP library. Spacy is a widely used library in the NLP community and is known for its speed and accuracy. Additionally, our solution will be deployed as a web-based application, making it end-to-end data science project.

## EVALUATION METRICS:
•	Accuracy of resume entity extraction
•	Time taken for the information extraction process
•	Number of resumes parsed

## MEASUREMENT OF SUCCESS:
The success of the solution will be measured by how well it can automate the resume review process and how much time and resources it can save for recruiters.

## EVALUATION AND FEASIBILITY:
The solution will be evaluated by testing it on a sample set of college student resumes and receiving feedback from our faculty. The feasibility of the solution is high as it is based on proven technologies and techniques.

## ESTIMATED IMPACT:
The impact of this solution is expected to be significant as it will significantly speed up the hiring process and increase efficiency for HR departments and recruiters. Additionally, it will make the job application process more efficient and streamlined for job seekers.

## DATA SOURCE: 
For the purpose of training, 220 resumes were downloaded from an online jobs platform. These documents were uploaded to Dataturks online annotation tool and manually annotated. The tool automatically parses the documents and allows for us to create annotations of important entities we are interested in and generates JSON formatted training data with each line containing the text corpus along with the annotations. The above dataset consisting of 220 annotated resumes can be found here.
