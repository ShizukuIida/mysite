from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import ContactFrom
from .models import Profile, Experience, Education, Technical, Publications, ScholarShip, Certifications
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
import textwrap


# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by('-id')[0]
        return render(request, 'app/index.html', {
            'profile_data': profile_data
        })

class AboutView(View):
    def get(self, request, *args, **kawargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by('-id')[0]
        publication_data = Publications.objects.order_by('-id')
        education_data = Education.objects.order_by('-id')
        technical_data = Technical.objects.order_by('-id')
        scholar_data = ScholarShip.objects.order_by('-id')
        certification_data = Certifications.objects.order_by('-id')
        return render(request, 'app/about.html', {
            'profile_data': profile_data,
            'publication_data': publication_data,
            'education_data': education_data,
            'technical_data': technical_data,
            'scholar_data': scholar_data,
            'certification_data': certification_data,
        })

class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactFrom(request.POST or None)
        return render(request, 'app/contact.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = ContactFrom(request.POST or None)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'お問合せありがとうございます。'
            contact = textwrap.dedent(f'''
                ※このメールはシステムからの自動送信です。
                
                {name} 様
                
                お問合せありがとうございました。
                以下の内容でお問合せを受け付けいたしました。
                内容を確認させていただき、ご返信させて頂きますので、少々お待ちください。
                
                -------------------
                ■お名前
                {name}
                
                ■メールアドレス
                {email}
                
                ■メッセージ
                {message}
                -------------------            
                ''').format(
                     name=name,
                     email=email,
                     message=message
                )
            to_list = [email]
            bcc_list = [settings.EMAIL_HOST_USER]

            try:
                message = EmailMessage(subject=subject, body=contact, to=to_list, bcc=bcc_list)
                message.send()
            except BadHeaderError:
                return HttpResponse('無効なヘッダが検出されました。')

            return redirect('thanks')

        return render(request, 'app/contact.html', {
            'form': form
        })

class ThanksView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/thanks.html')