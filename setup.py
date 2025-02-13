from setuptools import setup, find_packages

# Configuração do pacote usando setuptools
setup(
    # Nome do pacote
    name='brazil-cep-query',
    
    # Versão do pacote
    version='0.1.0',
    
    # Autor do pacote
    author='Your Name',
    
    # Email do autor
    author_email='your.email@example.com',
    
    # Descrição curta do pacote
    description='A Python application for querying postal codes (CEPs) in Brazil.',
    
    # Descrição longa do pacote, lida do arquivo README.md
    long_description=open('README.md').read(),
    
    # Tipo de conteúdo da descrição longa
    long_description_content_type='text/markdown',
    
    # URL do repositório do projeto
    url='https://github.com/yourusername/brazil-cep-query',
    
    # Pacotes a serem incluídos na distribuição
    packages=find_packages(where='src'),
    
    # Diretório base dos pacotes
    package_dir={'': 'src'},
    
    # Dependências necessárias para o pacote
    install_requires=[
        'requests',
        'Flask',
        'flask-cors',
    ],
    
    # Classificadores que fornecem metadados sobre o pacote
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    
    # Versão mínima do Python necessária
    python_requires='>=3.6',
)