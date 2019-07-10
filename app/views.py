from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import Qurilish
from django.forms import BaseModelFormSet
from django.contrib.auth.decorators import login_required


class BaseAuthorFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        self.queryset = Qurilish.objects.filter(author_id=self.request.user.pk)

@login_required
def hi(request):
    QurilishFormSet = modelformset_factory(Qurilish, formset=BaseAuthorFormSet, fields=(
        'id', 'q_type', 'servise_name', 'servise_code', 'soato', 'report_month', 'report_year', 'last_year'), extra=1)
    if request.method == "POST":
        formset = QurilishFormSet(request.POST, request=request)
        if formset.is_valid():
            for form in formset:
                obj = form.save(commit=False)
                obj.author = request.user
                obj.save()
            return redirect('hi')
    form = QurilishFormSet(request=request)
    return render(request, 'app1/home.html', {'form': form})


def destroy(request, id):
    employee = Qurilish.objects.get(id=id)
    employee.delete()
    return redirect("hi")


def delete(request):
    return render(request, 'app1/delete.html')

# def delete(request, pk):
#     forma = Qurilish.objects.get(pk=pk)
#     forma.delete()
#
#     return redirect('hi')
