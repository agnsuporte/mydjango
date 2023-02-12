""" App Profile
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

import copy

from store.user_profile.models import UserProfile
from store.user_profile import forms


class Baseprofile(View):
    template_name = 'user_profile/create_user.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.car = copy.deepcopy(self.request.session.get('sessionCar', {}))

        self.profile = None

        if self.request.user.is_authenticated:
            self.profile = UserProfile.objects.filter(
                user=self.request.user
            ).first()

            self.contexto = {
                'userform': forms.UserForm(
                    data=self.request.POST or None,
                    user=self.request.user,
                    instance=self.request.user,
                ),
                'profileform': forms.ProfileForm(
                    data=self.request.POST or None,
                    instance=self.profile
                ),
            }
        else:
            self.contexto = {
                'userform': forms.UserForm(
                    data=self.request.POST or None
                ),
                'profileform': forms.ProfileForm(
                    data=self.request.POST or None
                ),
            }

        self.userform = self.contexto['userform']
        self.profileform = self.contexto['profileform']

        self.renderizar = render(
            self.request, self.template_name, self.contexto)

    def get(self, *args, **kwargs):
        return self.renderizar


class CreateUser(Baseprofile):

    def post(self, *args, **kwargs):
        if not self.userform.is_valid() or not self.profileform.is_valid():
            messages.error(
                self.request,
                'Existem erros no formulário de cadastro. Verifique se todos '
                'os campos foram preenchidos corretamente.'
            )

            return self.renderizar

        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('password')
        email = self.userform.cleaned_data.get('email')
        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')

        # Usuário logado
        if self.request.user.is_authenticated:
            user = get_object_or_404(
                User, username=self.request.user.username)

            user.username = username

            if password:
                user.set_password(password)

            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            if not self.profile:
                self.profileform.cleaned_data['user'] = user
                profile = UserProfile(**self.profileform.cleaned_data)
                profile.save()
            else:
                profile = self.profileform.save(commit=False)
                profile.user = user
                profile.save()

        # Usário não logado (novo)
        else:
            user = self.userform.save(commit=False)
            user.set_password(password)
            user.save()

            profile = self.profileform.save(commit=False)
            profile.user = user
            profile.save()

        if password:
            autentica = authenticate(
                self.request,
                username=user,
                password=password
            )

            if autentica:
                login(self.request, user=user)

        self.request.session['sessionCar'] = self.car
        self.request.session.save()

        messages.success(
            self.request,
            'Seu cadastro foi criado ou atualizado com sucesso.'
        )

        messages.success(
            self.request,
            'Você fez login e pode concluir sua compra.'
        )

        return redirect('product_car')


class Login(View):
    template_name = 'user_profile/login_user.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        if not username or not password:
            messages.error(
                self.request,
                'Usuário ou senha inválidos.'
            )
            return redirect('login')

        user = authenticate(
            self.request, username=username, password=password)

        if not user:
            messages.error(
                self.request,
                'Usuário ou senha inválidos.'
            )
            return redirect('login')

        login(self.request, user=user)

        messages.success(
            self.request,
            'Você fez login no sistema e pode concluir sua compra.'
        )
        return redirect('product_car')


class Logout(View):
    def get(self, request, *args, **kwargs):
        carrinho = copy.deepcopy(self.request.session.get('sessionCar'))

        logout(self.request)

        self.request.session['sessionCar'] = carrinho
        self.request.session.save()

        return redirect('product')
