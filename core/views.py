from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order, OrderFile
from django.contrib.auth.decorators import login_required
from datetime import date

@login_required
def index(request):
	form = OrderForm()
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			order = form.save(commit=False)
			order.user = request.user
			order.save()
			return redirect('core:files', order_id=order.id)
	context = {
		'form': form,
		'from_year': date.today().year,
		'to_year': date.today().year + 10,
	}
	return render(request, 'index.html', context)

@login_required
def upload_files(request, order_id):
	try:
		order = Order.objects.get(id=order_id)
		if request.method == 'POST':
			for f in request.FILES.getlist('files'):
				try:
					orderfile = OrderFile.objects.get(order=order)
					orderfile.file = f
					orderfile.save()
				except OrderFile.DoesNotExist:
					OrderFile.objects.create(order=order, file=f)
			return redirect('core:orders')
	except Order.DoesNotExist:
		pass
	return render(request, 'files.html')

@login_required
def orders(request):
	orders = Order.objects.all().order_by('-created_on')
	context = {
		'orders': orders
	}
	return render(request, 'orders.html', context)