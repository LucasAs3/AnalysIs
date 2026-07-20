# Automate the retrieval and email delivery of system reports.
from Functions.OpenPopUp import open_pop_up
from Functions.Managers.FileManager import get_file_type, support_file_extension
from Functions.Readers.PDFReader import pdf_reader
from Functions.Ai.ai import do_a_document_analyze
from Functions.Render.PrintAnalyze import print_analyze
from Functions.Dashbord.graph_generator import create_metrics_chart
from Functions.PDFCreator.pdr_create import pdf_creator
from Functions.Readers.XLSXReader import excel_reader

file_path = open_pop_up()
extension = get_file_type(file_path)

if not file_path:
    print("nenhum arquivo selecionado")
    exit()

if not support_file_extension(file_path):
    print("extensão do arquivo não suportada")
    exit()

extension = get_file_type(file_path)

if(extension == "pdf"):
    doc = pdf_reader(file_path)
    analyze = do_a_document_analyze(doc)
    metrics_path = create_metrics_chart(analyze)
    pdf_creator(analyze, metrics_path)

if(extension == 'xlsx'):
    doc = excel_reader(file_path)
    analyze = do_a_document_analyze(doc)
    metrics_path = create_metrics_chart(analyze)
    pdf_creator(analyze, metrics_path)
