from django.shortcuts import render, redirect, get_object_or_404
from .models import Qa, Comment
import datetime
# Create your views here.
def post_index(request):
    qa = Qa.objects
    return render(request, 'post_index.html', {'qas':qa})

def post_create(request):
    return render(request, 'post_create.html')
    
def post_new(request):
    qa = Qa()
    qa.title = request.GET['title']
    qa.name = request.GET['name']
    qa.password = request.GET['password']
    qa.body = request.GET['body']
    if(request.GET.get('category') == '예약문의'):
        qa.category = '예약문의'
    elif(request.GET.get('category') == '기타문의'):
        qa.category = '기타문의'
    qa.save()
    return redirect('/')


def post_detail(request, qa_id):
    qa = get_object_or_404(Qa, pk=qa_id)
    comment = Comment.objects
    return render(request, 'post_detail.html', {'qa':qa,'comments':comment})

def post_update(request, qa_id):
    qa = get_object_or_404(Qa, pk=qa_id)
    return render(request, 'post_update.html', {'qa':qa})

def post_updat(request, qa_id):
    qa = get_object_or_404(Qa, pk=qa_id)
    qa.title = request.GET['title']
    qa.body = request.GET['body']
    qa.name = request.GET['name']
    qa.password = request.GET['password']
    qa.date = datetime.datetime.now()
    if(request.GET.get('category') == '예약문의'):
        qa.category = '예약문의'
    elif(request.GET.get('category') == '기타문의'):
        qa.category = '기타문의'
    qa.save()
    return redirect('/post_detail/'+str(qa_id))

def post_delete(request, qa_id):
    qa = get_object_or_404(Qa, pk=qa_id)
    qa.delete()
    return redirect('/')

def ccreate(request):
    if request.method == 'POST':
        comment=Comment()

        comment.cname = request.POST['cname']
        comment.content = request.POST['content']
        comment.post = Qa.objects.get(pk=request.POST['post'])

        comment.save()

        return redirect('post_detail/' + str(comment.post.id))
    return render(request, 'post_detail.html')

def cdelete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post = get_object_or_404(Qa, pk=comment.post.id)
    comment.delete()
    return redirect('/')
    #return render(request, 'detail.html', {'comment':comment})