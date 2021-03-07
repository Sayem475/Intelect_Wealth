from django.urls import path, include
from . import views
from django.views import View
from .views import *
urlpatterns = [
    
    # HOME URLS  
    path('',Home.as_view(), name='Home'),    
    path('about/',About.as_view(), name='About'),    
    path('contact/',UserContact.as_view(), name='UserContact'),    
    path('search/', Search.as_view(), name='Search'),   
    path('executiveteam/',ExecutiveTeam.as_view(), name='ExecutiveTeam'),   
    path('joinus/',JoinUs.as_view(), name='JoinUs'),   
    #  INTELLECT WEALTH URLS 
    path('clientEducation/',ClientEducation.as_view(), name='ClientEducation'),    
   
    path('<int:id>/<slug:slug>/', Advise_Detail.as_view(), name='advise_detail'),    
    path('iwAdvisor/',IwAdvisor.as_view(), name='IwAdvisor'),    
    path('iwLicense/',IwLicense.as_view(), name='IwLicense'),    
    path('iwOffer/',IwOffer.as_view(), name='IwOffer'),    
    path('iwTeam/',IwTeam.as_view(), name='IwTeam'),    
    path('joinIW/',JoinIw.as_view(), name='JoinIw'),    
    path('talkIW/',TalkIw.as_view(), name='TalkIw'),   
    path('findAdvisor/',FindAdviser.as_view(), name='FindAdviser'),   
    #  FOOTER URLS 
    path('security/',SecurityPolicy.as_view(), name='Security'),    
    path('terms/',Terms.as_view(), name='Terms'), 
    #    REGISTRATION URLS 
    # path('registration/',Registration.as_view(), name='Registration'), 
    
    # SLUG FOR SEARCH RESULTS 
    path('<int:id>/<slug:slug>', SearchResult.as_view(), name='SearchResult'),
      
    
]
