
from urllib import request
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

# 하던일 계속 하고 if 로그인 했으면 else 로그인부터 하고와라
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
# 회원가입 (및 정보변경) Form
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

# 로그인 Form(HTML / validation)
from django.contrib.auth.forms import AuthenticationForm

# 세션 생성/삭제하는 함수
from django.contrib.auth import login as auth_login, logout as auth_logout

# User 모델을 리턴하는 함수
from django.contrib.auth import get_user_model

from .forms import CustomUserChangeForm


User = get_user_model()

@require_http_methods(['GET', 'POST'])
def signup(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('articles:index')
        else:
            form = UserCreationForm()
        context = {'form' : form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('articles:index')
    
@require_http_methods(['GET', 'POST'])
# reqest GET은 quesry string에 대한 정보

def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                user = form.get_user()
                auth_login(request, user)
                return redirect(request.GET.get('next') or 'articles:index') 
        else:
            form = AuthenticationForm(request)
        context ={'form': form }
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('articles:index')


def logout(request):
    auth_logout(request)
    return redirect('articles:index')

# Authenticated User(인증된 사용자)에게만 profile 허용? 모두에게 오픈?
@login_required
def profile(request, username):
    profile_user = get_object_or_404(User, username=username)

    context ={
        'profile_user' : profile_user,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:profile', user.username)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'accounts/update.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        # 선택(교재 x)
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index')



@login_required
@require_http_methods(['GET', 'POST'])
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # PasswordChangeForm 은 forms.Form을 상속받았으나, 예외적으로 save 메서드가 존재
            user = form.save()

            from django.contrib.auth import update_session_auth_hash
            # auth_login(request, request.user)
            update_session_auth_hash(request, request.user)
            
            return redirect('accounts:profile', user.username)
    else:    
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'accounts/password.html', context)
