\# AI Code Reviewer



An intelligent Python code quality and complexity analyzer built using Streamlit, Flake8, Black, and Radon.



\## Project Overview



AI Code Reviewer is a web-based Python application designed to help developers review and improve their Python source code.



The application allows users to upload a Python `.py` file and automatically performs multiple code analysis checks. It provides code quality results, formatting analysis, complexity measurements, an overall quality score, and improvement recommendations through an easy-to-use Streamlit interface.



\## Features



\- Upload Python `.py` files

\- Flake8 code quality analysis

\- Black code formatting analysis

\- Radon cyclomatic complexity analysis

\- Overall code quality score

\- Analysis summary

\- Improvement recommendations

\- Downloadable code analysis report

\- Simple and user-friendly Streamlit interface



\## Technologies Used



\- Python

\- Streamlit

\- Flake8

\- Black

\- Radon



\## How the Project Works



1\. Launch the Streamlit application.

2\. Upload a Python `.py` source file.

3\. The application analyzes the uploaded code using Flake8, Black, and Radon.

4\. Code quality and formatting results are displayed.

5\. Cyclomatic complexity is calculated using Radon.

6\. An overall code quality score is generated.

7\. Improvement recommendations are provided.

8\. A downloadable analysis report is generated.



\## Analysis Tools



\### Flake8



Flake8 is used to identify Python code quality and style issues, including common PEP 8 violations.



\### Black



Black is used to check Python code formatting and identify files that would benefit from automatic formatting.



\### Radon



Radon is used to analyze cyclomatic complexity and provide complexity grades for Python functions.



\## Project Structure



```text

AI-Code-Reviewer/

|

|-- app.py

|-- analyzer.py

|-- report\_generator.py

|-- requirements.txt

|-- README.md

|-- .gitignore

|

|-- sample\_codes/

|   |-- test\_code.py

|

|-- reports/

|

|-- 01\_Initial\_Code\_Quality\_Score\_44.png

|-- 02\_Flake8\_Code\_Quality\_Analysis.png

|-- radon\_complexity\_analysis.png

|-- AI\_Code\_Reviewer\_Analysis\_Report.png

