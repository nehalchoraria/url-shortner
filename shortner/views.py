from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import  get_object_or_404
from .models import GeneratedLinks
import string,random,re
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib import messages

def index(request):
    def validateLink(link):
        match = re.search(settings.EMAILREGEX,link)  
        if match is not None:
            return 'https://' + match.group(0) if 'http' not in match.group(0)  else match.group(0)
        return None

    def generateRandomLink():
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k = settings.DYNAMICSTRINGLENGTH)) 

    shortLink = ''
    if request.method =='POST' and request.POST['link']:
        formattedLink = validateLink(request.POST['link'])
        if formattedLink is None:
            return render(request, 'shortner/index.html', {'error':settings.ERRORMESSAGE})
        print(formattedLink)
        linkObject = GeneratedLinks.objects.filter(full_link=formattedLink).values()
        print(linkObject)
        if len(linkObject) > 0:
            shortLink = linkObject[0]['short_link']
        else:
            shortLink = generateRandomLink()
            linkObject = GeneratedLinks(full_link=formattedLink,short_link=shortLink)
            linkObject.save()
    shortLink = '' if shortLink == '' else settings.DOMAIN+shortLink
    context = {'shortLink': shortLink }

    return render(request, 'shortner/index.html', context)

def redirectToUrl(request,link):
    linkObject = GeneratedLinks.objects.filter(short_link=link).values()
    if len(linkObject) > 0:
        return redirect(linkObject[0]['full_link'])
    else:
        return HttpResponseRedirect('/?err')
        # return render(request, 'shortner/index.html', {'error':'The link is either invalid or destroyed. Please re-create link.'})
