from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import JobOpening, JobApplicant
from .forms import JobApplicationForm, JobCreationForm
from django.http import HttpResponseForbidden


def job_list_view(request):
    query = request.GET.get('q')
    if query:
        jobs = JobOpening.objects.filter(
            Q(job_title__icontains=query) |
            Q(job_description__icontains=query) |
            Q(location__icontains=query)
        ).order_by('-created_date')
    else:
        jobs = JobOpening.objects.all().order_by('-created_date')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


@login_required
def job_detail_view(request, pk):
    job = get_object_or_404(JobOpening, pk=pk)
    is_admin = request.user.is_admin
    applicants = None
    form = JobApplicationForm()
    already_applied = False

    if request.user.is_authenticated and not is_admin:
        already_applied = JobApplicant.objects.filter(user=request.user, job=job).exists()

    if is_admin:
        applicants = JobApplicant.objects.filter(job=job)

    return render(request, 'jobs/job_detail.html', {
        'job': job,
        'is_admin': is_admin,
        'applicants': applicants,
        'form': form,
        'already_applied': already_applied,
    })


def apply_for_job(request, pk):
    if request.method == 'POST' and request.user.is_authenticated and not request.user.is_admin:
        job = get_object_or_404(JobOpening, pk=pk)
        if JobApplicant.objects.filter(user=request.user, job=job).exists():
            return redirect('jobs:job_detail', pk=pk)

        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            JobApplicant.objects.create(
                user=request.user,
                job=job,
                resume=form.cleaned_data['resume']
            )
            return redirect('jobs:job_detail', pk=pk)
    return redirect('jobs:job_detail', pk=pk)


class JobCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = JobOpening
    form_class = JobCreationForm
    template_name = 'jobs/job_create.html'

    def test_func(self):
        return self.request.user.is_admin

    def handle_no_permission(self):
        return redirect('401')

    def get_success_url(self):
        return reverse_lazy('jobs:job_list')


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = JobOpening
    form_class = JobCreationForm
    template_name = 'jobs/job_update.html'

    def test_func(self):
        return self.request.user.is_admin

    def handle_no_permission(self):
        return redirect('401')

    def get_success_url(self):
        return reverse_lazy('jobs:job_detail', kwargs={'pk': self.object.pk})


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = JobOpening
    template_name = 'jobs/job_confirm_delete.html'
    success_url = reverse_lazy('jobs:job_list')

    def test_func(self):
        return self.request.user.is_admin

    def handle_no_permission(self):
        return redirect('401')