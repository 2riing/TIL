from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods, require_POST
# 하던일 계속 하고 if 로그인 했으면 else 로그인부터 하고와라
from django.contrib.auth.decorators import login_required
# 회원가입 (및 정보변경) Form
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
# 로그인 Form(HTML / validation)
from django.contrib.auth.forms import AuthenticationForm
# 세션 생성/삭제하는 함수
from django.contrib.auth import login as auth_login, logout as auth_logout
# User 모델을 리턴하는 함수
from django.contrib.auth import get_user_model
from articles.models import Article

from .forms import CustomUserChangeForm

User = get_user_model()


@require_http_methods(['GET', 'POST'])
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()         # 회원가입 완료한 사용자
                auth_login(request, user)  # 해당 사용자로 session 생성 + cookie 발급
                return redirect('articles:article_index')
        else:
            form = UserCreationForm()
        context = { 'form': form }
        return render(request, 'accounts/signup.html', context)
    else:
        # return HttpResponseBadRequest()
        return redirect('articles:article_index')
    


@require_http_methods(['GET', 'POST'])
def login(request):  # /accounts/login/
    # request.GET 은 query string 에 대한 정보!
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                user = form.get_user()     # 로그인 데이터 제출한 사용자 (get_user()는 AuthenticationForm 에만 존재하는 메서드)
                auth_login(request, user)  # 해당 사용자로 session 생성 + cookie 발급
                
                # if request.GET.get('next'):
                #     return redirect(request.GET.get('next'))
                # else:
                #     return redirect('articles:index')
                return redirect(request.GET.get('next') or 'articles:article_index')   
        else:
            form = AuthenticationForm()
        context = { 'form': form }
        return render(request, 'accounts/login.html', context)
    else:
        # return HttpResponseBadRequest()
        return redirect('articles:article_index')


def logout(request):
    auth_logout(request)  # 현재 request에 담긴 사용자 정보의 session 삭제 + cookie 삭제
    return redirect('articles:article_index')


@login_required
def profile(request, username):
    article = Article.objects.order_by('-pk')
    profile_user = get_object_or_404(User, username=username)  # User 모델에서 username으로 검색하여 찾은 객체
    is_follow = request.user.stars.filter(username=username).exists()
    context = {
        'profile_user': profile_user,
        'is_follow' : is_follow,
        'article' : article,
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
        request.user.delete()
        # 선택(교재X)
        auth_logout(request)
    return redirect('articles:article_index')


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

@login_required
@require_POST
def follow(request, username):
    profile_user = get_object_or_404(User, username=username)
    user = request.user
    if user.stars.filter(username=username).exists(): #이미 팔로우 했으면
        user.stars.remove(profile_user)
    else:
        user.stars.add(profile_user)
    return redirect('accounts:profile', profile_user.username)



# Create your views here.
