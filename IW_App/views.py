from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from IW_App.models import *
from django.db.models import Q
from django.contrib import messages


# HOME TEMPLATES VIEWS 
class Home(View):
    def get(self, request):
        return render(request, 'Home/home.html')
    
class About(View):
    def get(self, request):
        team = TeamMember.objects.all()
        context = {
                'team':team
        }
        return render(request, 'Home/about.html', context)
    
class UserContact(View):
    def get(self, request):
        return render(request, 'Home/contact.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(
                first_name = first_name,
                last_name = last_name,
                email = email,
                phone = phone,
                message = message
            )
        print(contact)
        contact.save()
        messages.success(request, ' Your message has been sent Successfully...')
        return render(request, 'Home/contact.html')

    
    
class Search(View):
    def get(self, request):
        query = request.GET['query']
        if len(query)>50:
            result = []
            messages.error(request, 'Sorry Keyword is too long')
        elif len(query)==0:
            result = []
            messages.warning(request, 'Sorry invalid keyword')
        elif query!=query:
            result = []
            messages.warning(request, 'Sorry your querry didnt match!')
        else:
            
            lookups= Q(name__icontains=query) | Q(team_desc__icontains=query) 

            result= TeamMember.objects.filter(lookups).distinct()
            
        context={'result':result, 'query':query
        }

        return render(request, 'Home/search.html', context)
 
  # For search detail    
class SearchResult(View):
    def get(self, request, id, slug):
        member = get_object_or_404(TeamMember, id=id, slug=slug)
        context = {
            'member': member
        }
        return render(request, 'Home/searchresults.html', context )
    
class JoinUs(View):
    def get(self, request):
        return render(request, 'Home/joinus.html')
    
class ExecutiveTeam(View):
    def get(self, request):
        ex_team = TeamMember.objects.all()
        context = {
                'ex_team':ex_team
        }
        return render(request, 'Home/executiveteam.html', context)
    
# REGISTRATION & LOGIN TEMPLATE VIEWS  
class Registration(View):
    def get(self, request):
        return render(request, 'Registration/registration.html') 

# INTELLECT WEALTH TEMPLATES VIEWS      
class ClientEducation(View):
    def get(self, request):
        # title = ClientEducation.objects.all()
        files = ClintFile.objects.all()
        context={
            'files':files
        }
        return render(request, 'IW/clientEducation.html', context)
    
class IwAdvisor(View):
    def get(self, request):
        advisor = IWAdvisor.objects.all()
        context = {

                'advisor':advisor
        }
        return render(request, 'IW/iwAdvisor.html', context)
    
class IwLicense(View):
    def get(self, request):
        license = IWLicense.objects.all()
        context={
            'license': license
        }
        return render(request, 'IW/iwLicense.html', context)
    
class IwOffer(View):
    def get(self, request):
        iw_offer = OurOffers.objects.all()
        context = {
                'iw_offer':iw_offer
        }
        return render(request, 'IW/iwOffer.html', context)
    
class IwTeam(View):
    def get(self, request):
        i_teams = BusinessAdvise.objects.all()
        context = {
                'i_teams': i_teams
        }

        return render(request, 'IW/iwTeam.html', context)

#for business advise details page###
class Advise_Detail(View):
    def get(self, request, id, slug):
        advise = get_object_or_404(BusinessAdvise, id=id, slug=slug)
        
        context = {
               'advise': advise
                   }
        return render(request,'IW/iwAdvise.html', context)
    
class JoinIw(View):
    def get(self, request):
        return render(request, 'IW/joinIW.html')
    
class TalkIw(View):
    def get(self, request):
        return render(request, 'IW/talkIW.html')
    
class SecurityPolicy(View):
    def get(self, request):
        limitaion = Limitation.objects.all()
        security = Security.objects.all()
        context = {
                'security':security,
                'limitaion': limitaion
        }
        return render(request, 'Footer/security.html',context)
    
class Terms(View):
    def get(self, request):
        terms = TermsOfUse.objects.all()
        context = {
                'terms': terms
        }
        return render(request, 'Footer/terms.html', context)
    
class FindAdviser(View):
    def get(self, request):
        return render(request, 'IW/find_advisor.html')