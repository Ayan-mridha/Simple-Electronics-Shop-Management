from django.shortcuts import render
from Practical_App2.models import *
def homepage(request):
    
    
    
    
    return render(request, "homepage.html")
def add_salepage(request):
    if request.method == "POST":
        p_name = request.POST.get("p_name")
        catagory = request.POST.get("catagory")
        unit_price = float(request.POST.get("unit_price"))
        quantity = int(request.POST.get("quantity"))
        discount_price = float(request.POST.get("discount"))
        tax_percentise = float(request.POST.get("tax_percent"))
        sell_date = request.POST.get("sale_date")
        initial_price = float(unit_price*quantity)
        dis_price = float(initial_price*discount_price/100)
        tax_price = float(initial_price*tax_percentise/100)
        total_price = float(initial_price+tax_price-dis_price)
        
        data=saleModel(
            Product_Name=p_name,
            Catagory= catagory,
            unit_price=unit_price,
            quantity=quantity,
            discount_percent=discount_price,
            tax_percent = tax_percentise,
            total_price = total_price,
            sale_date = sell_date,
        )
        data.save()
        
    return render(request, 'add_salepage.html')


def salesData(request):
    
    data=saleModel.objects.all()
    
    context={
        'data':data
    }
    
    return render(request,"sale_listpage.html",context)