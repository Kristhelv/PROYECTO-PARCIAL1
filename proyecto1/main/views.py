from multiprocessing import context
from django.shortcuts import render
from django.contrib import messages
from .models import (
		UserProfile,
		Blog,
		Portfolio,
		Testimonial,
		Certificate
	)
#Se importan diferentes librerias de Django.
from django.views import generic
from . forms import BlogForm, ContactForm, CreateUserForm, ReviewForm
#Se importan diferentes librerias de Django.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect


#Se lleva a cabo un ciclo en el cual se colocaran parametros para el inicio de sesion.
def registerPage(request):
	#Se lleva a cabo un ciclo if para poner los parametros.
	#Si la informacion se autentica retorna al home.
	if request.user.is_authenticated:
		return redirect("main:home")
		#Si no lo lleva al metodo POST
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
                #Se coloca el retorno.
				return redirect('main:login')
			

		context = {'form':form}
		return render(request, 'main/register.html', context)
#Se lleva a cabo otro ciclo para lo que es el login a la pagina.
def loginPage(request):
	#Se lleva a cabo un ciclo if con parametros dentro.
	#Si la informacion se autentica retorna al home.
	if request.user.is_authenticated:
		return redirect("main:home")
		#Si no lo lleva al metodo POST
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)
#Si la informacion se autentica retorna al home.
			if user is not None:
				login(request, user)
				return redirect("main:home")
				#Si no que le suelte el siguiente mensaje.
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'main/login.html', context)
#Se lleva a cabo otro ciclo para lo que es el logout a la pagina.
def logoutUser(request):
	logout(request)
	return redirect('main:login')


#se crea la clase IndexView y algunos parametros dentro de la misma.
class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		testimonials = Testimonial.objects.filter(is_active=True)
		certificates = Certificate.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)
		
		context["testimonials"] = testimonials
		context["certificates"] = certificates
		context["blogs"] = blogs
		context["portfolio"] = portfolio
		return context

#se crea la clase ContactView y algunos parametros dentro de la misma.
class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)
#se crea la clase BlogAddInfo y algunos parametros dentro de la misma.
class BlogAddInfo(generic.FormView):
	template_name = "main/blogaddinfo.html"
	form_class = BlogForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you for contribute with the page :)')
		return super().form_valid(form)

class ReviewAddInfo(generic.FormView):
	template_name = "main/reviewaddinfo.html"
	form_class = ReviewForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you for contribute with the page :)')
		return super().form_valid(form)
#se crea la clase PortfolioView y algunos parametros dentro de la misma.
class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "main/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)

#se crea la clase PortfolioDetailView y algunos parametros dentro de la misma.
class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "main/portfolio-detail.html"
#se crea la clase BlogView y algunos parametros dentro de la misma.
class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)

#se crea la clase BlogDetailView y algunos parametros dentro de la misma.
class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"