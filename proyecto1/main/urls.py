from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


app_name = "main"
#se lleva a cabo los url de los diferentes apartados.
urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('accounts/login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),

	path('', views.IndexView.as_view(), name="home"),
	path('contact/', views.ContactView.as_view(), name="contact"),
	path('blogaddinfo/', login_required(views.BlogAddInfo.as_view()), name='blogaddinfo'),
	path('reviewaddinfo/', login_required(views.ReviewAddInfo.as_view()), name='reviewaddinfo'),
	path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
	path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
	path('blog/', views.BlogView.as_view(), name="blogs"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
	]