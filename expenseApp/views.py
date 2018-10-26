from django.shortcuts import render, get_object_or_404, redirect
from .models import AccountModel, TransactionModel
from .forms import AccountForm, UserForm, DepositForm, ExpenseForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# ALL OF THE VIEWS LISTED HERE

def index(request):
    user_account = AccountModel.objects.all()
    context = {'user_account': user_account}
    return render(request, 'expenseApp/base.html', context)

def create(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            changeForm = form.save(commit=False)
            changeForm.username = request.user
            changeForm.save()
        return redirect('index')
    else:
        form = AccountForm()
    return render(request, 'expenseApp/create.html', {'form': form})

def deposit(request, pk):
    theModel = get_object_or_404(AccountModel, pk=pk)
    user_account = AccountModel.objects.all()
    if request.method == 'POST':

        form = DepositForm(request.POST, instance=theModel)
        if form.is_valid():
            changeForm = form.save(commit=False)
            changeForm.username = request.user
            dep_amt = (form.cleaned_data['deposit'])
            exp_amt = 0
            new_amt = (dep_amt - exp_amt)
            changeForm.balance += new_amt
            changeForm.save()
            a = TransactionModel(id=None, amount= int(new_amt), transaction='DEPOSIT', account=changeForm)
            a.save()
            return redirect('index')
    else:
        form = DepositForm()
    return render(request, 'expenseApp/deposit.html',{'form':form, 'user_account':user_account})

def expense(request, pk):
    theModel = get_object_or_404(AccountModel, pk=pk)
    user_account = AccountModel.objects.all()
    if request.method == 'POST':

        form = ExpenseForm(request.POST, instance=theModel)
        if form.is_valid():
            changeForm = form.save(commit=False)
            changeForm.username = request.user
            dep_amt = 0
            exp_amt = (form.cleaned_data['expense'])
            new_amt = (dep_amt - exp_amt)
            changeForm.balance += new_amt
            changeForm.save()
            a = TransactionModel(id=None, amount= int(new_amt), transaction='EXPENSE', account=changeForm)
            a.save()
            return redirect('index')
    else:
        form = ExpenseForm()
    return render(request, 'expenseApp/expense.html',{'form':form, 'user_account':user_account})

def edit(request, pk):
    theModel = get_object_or_404(AccountModel, pk=pk)
    user_account = AccountModel.objects.all()
    if request.method == 'POST':

        form = AccountForm(request.POST, instance=theModel)
        if form.is_valid():
            changeForm = form.save(commit=False)
            changeForm.username = request.user
            changeForm.save()

            return redirect('index')
    else:
        form = AccountForm(instance=theModel)
    return render(request, 'expenseApp/edit.html',{'form':form, 'user_account':user_account})

def detail(request, pk):
    theModel = get_object_or_404(AccountModel, pk=pk)
    print(theModel)
    transactions = TransactionModel.objects.filter(account=pk)
    return render(request, 'expenseApp/detail.html', {'theModel': theModel, 'user_account': transactions})


def newUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create_user(request.POST.get("name"), request.POST.get("email"),request.POST.get("password"))
            return redirect('index')
    else:
        form = UserForm()
        return render(request, 'expenseApp/newUser.html', {'form': form})

@login_required
def userList(request):
    user_account = AccountModel.objects.filter(username=request.user)
    context = {'user_account': user_account}
    return render(request, 'expenseApp/base.html', context)