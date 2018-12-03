from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from stations.models import Company, Station


def hello(request):
    return HttpResponse("hello")


def company_name(request, company_id):
    c = get_object_or_404(Company, pk=company_id)
    # c = Company.objects.get(pk=company_id)
    # return HttpResponse("Company " + str(company_id) + " is " + c.name)
    return render(request, 'company_details.html', {'company': c})

def company_index(request):
    companies = Company.objects.all()
    return render(request, 'company_index.html', {'companies': companies})
