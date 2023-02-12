
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import copy

from store.user_profile.models import UserProfile
from store.user_profile import forms


class Baseprofile(View):
    # template_name = 'store/user_profile/home.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.car = copy.deepcopy(self.request.session.get('sessionCar', {}))

        self.profile = None

        if self.request.user.is_authenticated:
            self.profile = UserProfile.objects.filter(
                user=self.request.user
            ).first()

            print('true')

            self.contexto = {
                'userform': forms.UserForm(
                    data=self.request.POST or None,
                    user=self.request.user,
                    instance=self.request.user,
                ),
                'profileform': forms.profileForm(
                    data=self.request.POST or None,
                    instance=self.profile
                )
            }
        else:
            self.contexto = {
                'userform': forms.UserForm(
                    data=self.request.POST or None
                ),
                'profileform': forms.profileForm(
                    data=self.request.POST or None
                )
            }
            print('falso')
        self.userform = self.contexto['userform']
        self.profileform = self.contexto['profileform']

        if self.request.user.is_authenticated:
            self.template_name = 'store/user_profile/home.html'

        print(self.template_name)

        self.renderizar = render(
            self.request, self.template_name, self.contexto)

    def get(self, *args, **kwargs):
        return self.renderizar

class Atualizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Atualizar')

