from django.shortcuts import render
from theme.templates.paths import Paths as path

def home(request):

    language = [
        {"name" : "Python", "porce" : "75,100"},
        {"name" : "Java", "porce" : "50,100"},
        {"name" : "SQL", "porce" : "30,100"},
        {"name" : "TypeScript", "porce" : "40,100"},

    ]
    frameworks = [
        {"name" : "React N", "porce" : "40,100"},
        {"name" : "Django", "porce" : "75,100"},
        {"name" : "TailWind", "porce" : "60,100"},
        {"name" : "Pandas", "porce" : "65,100"},
    ]


    skills = [
        {"data_science": "Coleta e scraping de dados", "dev":"Mapeamento de processos" },
        {"data_science": "Tratamento e limpeza de dados", "dev":"Estruturação de back-end" },
        {"data_science": "Análise exploratória de dados", "dev":"Estruturação de interfaces e componentes" },
        {"data_science": "Visualização de dados", "dev":"Atenção à aplicação de principios de arquitetura de software" },
        {"data_science": "Automação de processos e rotinas", "dev":"Atenção à clareza e coesão de código" },
    ]



    texts =[
        {"title": "As vezes dar dois passos para traz é a melhor decisão.", 
         "text": """Muitas vezes, na labuta e na tentativa constante de solucionar um problema, 
         deixamos passar despercebido que estamos olhando apenas um nó em meio a um emaranhado de questões. 
         Dar alguns passos para trás nos permite enxergar a dimensão do problema e entender onde devemos focar nossas energias."""},

    ]

    projects = [
        {"gitHub":"https://github.com/Deiner-S/Site-Curriculo",
         "title":"Site",
         "text":"aijsdnundqinwc8aynscam asnmq8wndquwncqayc  qwunas8c q qwudnq09wdpaia  q9oimc9 iuwpmamasidmp9aid9awd"},

        {"gitHub":"https://github.com/Deiner-S/app_AT",
         "title":"App Agro Terra",
         "text":"aijsdnundqinwc8aynscam asnmq8wndquwncqayc  qwunas8c q qwudnq09wdpaia  q9oimc9 iuwpmamasidmp9aid9awd"},

        {"gitHub":"Diário Escolar",
         "title":"teste",
         "text":"aijsdnundqinwc8aynscam asnmq8wndquwncqayc  qwunas8c q qwudnq09wdpaia  q9oimc9 iuwpmamasidmp9aid9awd"},

        {"gitHub":"Opções binárias",
         "title":"teste",
         "text":"aijsdnundqinwc8aynscam asnmq8wndquwncqayc  qwunas8c q qwudnq09wdpaia  q9oimc9 iuwpmamasidmp9aid9awd"},


    ]

    formacoes = [
        {"title":"Instituto Federal de Ciências e Tecnologia de Goiás",
         "data":"MARÇO DE 2016 - MARÇO DE 2019",
         "text":"Técnico em Manutenção e Suporte em Informática"},

        {"title":"Universidade Estácio de Sá ",
         "data":"JULHO DE 2023 - DEZEMBRO DE 2025",
        "text":"Tecnólogo em Análise e Desenvolvimento de Sistemas"}
    ]

    experiencias = [
        {"cargo":"ANALISTA ADMINISTRATIVO",
         "data":"SETEMBRO DE 2024 - ATUAL",
         "empresa":"Universidade Federal de Uberlândia",
         "descricao":"""Atualmente designado ao setor de livraria da Editora UFU, 
         atuando na elaboração de relatórios financeiros e operacionais a partir de dados de vendas e emissão de notas fiscais. 
         Responsável pelo controle e acompanhamento de todo o fluxo do livro físico na livraria, com aplicação pontual de automação e 
         mapeamento de processos."""},
    ]

    contacts = [
        {"text":"linkedin","link":"www.linkedin.com/in/deiner-rodrigues-1b93b63a3"},
        {"text":"GitHub","link":"https://github.com/Deiner-S"},
        {"text":"deiner.souza@outlook.com","link":"mailto:deiner.souza@outlook.com?subject=Interesse%20em%20contratação"},
        {"text":"(34) 9-9967-0813","link":"https://wa.me/5534999670813"},
        
    ]
         


    return render(request, path.HOME,{
                                      "texts":texts, 
                                      "skills":skills, 
                                      "contacts":contacts,
                                      "language":language, 
                                      "projects":projects, 
                                      "formacoes":formacoes, 
                                      "frameworks":frameworks, 
                                      "experiencias":experiencias,
                                      })