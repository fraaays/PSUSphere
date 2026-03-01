from django.shortcuts import render

from django.views.generic.list import ListView


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student, College, Program
from studentorg.forms import OrganizationForm, OrgMemberForm, StudentForm, CollegeForm, ProgramForm
from django.urls import reverse_lazy

from django.db.models import Q
from django.utils import timezone
    

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["organization_count"] = Organization.objects.count()
        context["program_count"] = Program.objects.count()
        return context
    
class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5
    ordering = ["college__college_name","name"]
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
        return qs
    
class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')
    
class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')
    
class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'OrgMember'
    template_name = 'OrgMember_list.html'
    paginate_by = 5
    def get_ordering(self):
        allowed = ["student__lastname",
                   "date_joined",]
        
        sort_by = self.request.GET.get("sort_by")

        if sort_by in allowed:
            return sort_by

        return "student__lastname"
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(student__lastname__icontains=query) |
                Q(student__firstname__icontains=query) |
                Q(organization__name__icontains=query) |
                Q(date_joined__icontains=query)
            )
        return qs

class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'OrgMember_form.html'
    success_url = reverse_lazy('OrgMember-list')
    
class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'OrgMember_form.html'
    success_url = reverse_lazy('OrgMember-list')
    
class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'OrgMember_del.html'
    success_url = reverse_lazy('OrgMember-list')

class StudentList(ListView):
    model = Student
    context_object_name = 'Student'
    template_name = 'Student_list.html'
    paginate_by = 5
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(student_id__icontains=query) |
                Q(lastname__icontains=query) |
                Q(firstname__icontains=query) |
                Q(middlename__icontains=query) |
                Q(program__prog_name__icontains=query) |
                Q(program__college__college_name__icontains=query)
            )
        return qs

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'Student_form.html'
    success_url = reverse_lazy('Student-list')
    
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'Student_form.html'
    success_url = reverse_lazy('Student-list')
    
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'Student_del.html'
    success_url = reverse_lazy('Student-list')
    
class CollegeList(ListView):
    model = College
    context_object_name = 'College'
    template_name = 'College_list.html'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(college_name__icontains=query)
            )
        return qs

class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'College_form.html'
    success_url = reverse_lazy('College-list')

class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'College_form.html'
    success_url = reverse_lazy('College-list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'College_del.html'
    success_url = reverse_lazy('College-list')

class ProgramList(ListView):
    model = Program
    context_object_name = 'Program'
    template_name = 'Program_list.html'
    paginate_by = 5
    def get_ordering(self):
        allowed = ["prog_name", "college__college_name"]
        sort_by = self.request.GET.get("sort_by")

        if sort_by in allowed:
            return sort_by

        return "prog_name"

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'Program_form.html'
    success_url = reverse_lazy('Program-list')

class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'Program_form.html'
    success_url = reverse_lazy('Program-list')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'Program_del.html'
    success_url = reverse_lazy('Program-list')