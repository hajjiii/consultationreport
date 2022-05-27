from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def consultation(request):
    return render(request,"pdf_convert/consultation.html")

def pdf_report_create(request):
    template_path = 'pdf_convert/pdfreport.html'
    context ={}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="CR_{Pt Last Name}_{Pt FirstName}_{dob}.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response