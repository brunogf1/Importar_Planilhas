from django.shortcuts import render, redirect
from openpyxl import load_workbook
from .models import Produto
from .forms import UploadExcelForm
from django.core.paginator import Paginator

# Create your views here.


def importar_produtos(request):
    # Inicializa o formulário para a requisição GET ou se o formulário estiver inválido no POST
    form = UploadExcelForm()

    if request.method == 'POST':
        form = UploadExcelForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo_excel = request.FILES['arquivo_excel']
            wb = load_workbook(arquivo_excel)
            sheet = wb.active

            # Limpa os produtos antigos (opcional)
            Produto.objects.all().delete()

            # Itera pelas linhas da planilha e cria os produtos
            for row in sheet.iter_rows(min_row=2, values_only=True):
                Produto.objects.create(
                    SKU=row[0],
                    Produto=row[1],
                    Dados_Complementares=row[2],
                    UM=row[3],
                    Categoria=row[4],
                )

            return redirect('lista_produtos') 
        
    return render(request, 'produtos/importar_produtos.html', {'form': form})

def lista_produtos(request):
    produtos_list = Produto.objects.all()
    paginator = Paginator(produtos_list, 50)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'produtos/lista_produtos.html', {'page_obj': page_obj})
