from setuptools import find_packages,setup

setup(
    name = "mcqgenerator",
    version  = '0.0.1',
    author = "Areeba Abid",
    author_email = 'aareeba006@gmail.com',
    install_requires = ["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages = find_packages()
)