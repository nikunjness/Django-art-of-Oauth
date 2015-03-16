from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import logout
import tweepy
import json
from artofoauth.apps.twittereti import json_response


@login_required
def home(request):
    if request.user and request.user.is_authenticated():
        return redirect("/static/apps/twittereti/home.html")


@login_required
def logout_user(request):
    logout(request)
    return redirect('/accounts/login/')


@json_response
def get_user_details(request):
    user = request.user
    social = user.social_auth.get(provider='twitter')
    details = social.extra_data['access_token']
    auth = tweepy.OAuthHandler(settings.SOCIAL_AUTH_TWITTER_KEY, settings.SOCIAL_AUTH_TWITTER_SECRET)
    auth.set_access_token(details['oauth_token'], details['oauth_token_secret'])
    api = tweepy.API(auth)
    my_profile = api.me()
    my_profile = json.dumps(my_profile._json)
    return my_profile


