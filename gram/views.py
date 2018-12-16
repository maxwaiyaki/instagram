from django.shortcuts import render, redirect
from .models import Profile, Image, Comments

# Create your views here.
@login_required(login_url='accounts/login')
def index(request):
    if request.user.is_superuser:
        return redirect('http://localhost:8000/admin')
    else:
        images = Image.get_images()
        comments = Comment.objects.all()
        form = CommentForm()
        return render(request,"index.html",{"images":images,"form":form,"comments":comments})    

@login_required(login_url='accounts/login/')
def profile(request,username):
    current_user = request.user
    try:
        user = User.objects.get(username = username)
        profile = Profile.objects.get(user = user)
        images = Image.objects.filter(profile = profile)
        following = Profile.objects.filter(followers = user).count()
    
    except ObjectDoesNotExist:
        return redirect('edit_profile',current_user)

    if request.method == 'POST':
        form = NewImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.profile = profile
            image.save()
    else:
        form = NewImageForm()
    return render(request,"profile.html",{"profile":profile, "images":images, "form":form,"following":following})
