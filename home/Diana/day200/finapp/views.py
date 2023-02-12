from django.shortcuts import render
from .models import Incomes, Year, Month, Business

# Create your views here.
def index(request):
    """Home page of application"""
    return render(request, "finapp/index.html")


def stats(request):
    incomes = Incomes.objects.order_by("income")
    context = {"incomes": incomes}
    return render(request, "finapp/allstats.html", context)


################################################################################
def yearswithincome(request):
    l = Incomes.objects.values("year")
    s = []
    for i in l:
        s.append(i["year"])
    s = set(s)
    yy = []
    for y in s:
        yy.append(Year.objects.get(id=y))
    yy.sort(key=lambda x: x.year)
    mapper = {"YEARS": yy}
    return render(request, "finapp/yearslist.html", mapper)


def monthswithincome(request, year):
    m = Incomes.objects.filter(year=year)
    months = []
    for income in m:
        months.append(income.month)
    months = set(months)
    months = list(months)

    mapper = {"MONTHS": months, "year_id": year}
    return render(request, "finapp/monthslist.html", mapper)


def ylist(request):
    years = Year.objects.order_by("year")
    mapper = {"YEARS": years}
    return render(request, "finapp/yearslist.html", mapper)


def incomes(request, year, month):
    incs = Incomes.objects.filter(year=year)
    incs = filter(lambda x: x.month.month == month, incs)
    mapper = {"INCOMES": incs}
    return render(request, "finapp/inclist.html", mapper)
