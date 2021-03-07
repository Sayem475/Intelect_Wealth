from django.contrib import admin
from IW_App.models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    

# admin.site.register(AboutUS, SomeModelAdmin)
# admin.site.register(TeamMember, SomeModelAdmin)
admin.site.register(IWLicense, SomeModelAdmin )
admin.site.register(IWAdvisor, SomeModelAdmin)
admin.site.register(OurOffers, SomeModelAdmin)
admin.site.register(BusinessAdvise, SomeModelAdmin)
# admin.site.register(ClientEducation, SomeModelAdmin)
admin.site.register(Contact, SomeModelAdmin)
admin.site.register(Security, SomeModelAdmin)
admin.site.register(TermsOfUse, SomeModelAdmin)
admin.site.register(Limitation, SomeModelAdmin)



# class AboutAdmin(admin.ModelAdmin):
# 	list_display = ['title']
# admin.site.register(AboutUS, SomeModelAdmin)

class TeamMemberAdmin(SummernoteModelAdmin):
	list_display = ['name', 'designation', 'image_tag']
	search_fields = ['name', 'designation']
	# prepopulated_fields={'slug':('name',)
	
admin.site.register(TeamMember, TeamMemberAdmin)  

class ClintFileInline(admin.TabularInline):
    model =  ClintFile
    readonly_fields = ('id',)
    extra = 5

class ClintAdmin(SummernoteModelAdmin):
	list_display = ['ce_title']
	inlines = [ClintFileInline]

admin.site.register(ClientEducation, ClintAdmin)




