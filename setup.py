from setuptools import setup, find_packages

# read readme.md for longer description
with open('README.md', 'r', encoding='utf-8') as f:
    long_description=f.read()

setup(
    name='text2sql_agent',
    version='0.1.0',
    author='Durga Sandeep Saluru',
    author_email='sandeepsaluru99@gmail.com',
    description='A framework-free Text2SQL agent for converting natural language queries into SQL',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DurgaSandeep25/Text2SQL-Agent",
    packages=find_packages(where='src'),
    package_dir={"":"src"},
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=[
        'sqlalchemy',
        'scikit-learn',
    ],
    extras_require={
        "dev" : ["pytest"],
        "deploy":["fastapi", 'uvicorn', 'pydantic']
    }
)
