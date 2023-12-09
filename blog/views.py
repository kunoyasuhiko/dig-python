from django.shortcuts import render, redirect
from blog.forms import CommentForm
from blog.forms import PostForm
from .models import Post
from .forms import YourForm

# Create your views here.
def frontpage(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        print("POSTされました。ADDボタンで")
        slugName = "post-" + str(Post.objects.count() + 1)
        Post.objects.create(title="-",slug=slugName,intro="-",body="-")
        return redirect('post_detail', slugName)

    if "query" in request.GET:
    # if request.method == "GET":
        query = request.GET.get('query')
        print("検索クリック", query)
        posts = Post.objects.all().exclude(body__exact="DELETED").filter(body__contains=query).order_by('posted_date').reverse()
        return render(request, "blog/frontpage.html",{"posts":posts})


    # posts = Post.objects.all()
    # posts = Post.objects.all().order_by('posted_date').reverse()
    posts = Post.objects.all().exclude(body__exact="DELETED").order_by('posted_date').reverse()
    return render(request, "blog/frontpage.html",{"posts":posts})

def post_detail(request, slug):
    # posts = Post.objects.all().order_by('posted_date').reverse()
    posts = Post.objects.all().exclude(body__exact="DELETED").order_by('posted_date').reverse()
    post = Post.objects.get(slug=slug)

    # if request.method == "POST":
    #     form = CommentForm(request.POST)

    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.post = post
    #         comment.save()

    #         return redirect("post_detail", slug=post.slug)
    # else:
    #     form =CommentForm()

    # return render(request, "blog/frontpage.html",{"posts":posts, "post":post, "form":form})
    return render(request, "blog/frontpage.html",{"posts":posts, "post":post})


def frontpage_save(request):

    # if request.method == "POST":
    if "saveClick" in request.POST:
        print("SAVEボタンで")
        form = YourForm(request.POST)
        if form.is_valid():
            # フォームが正常に処理された場合、データを保存などの操作を行う
            # 例: フォームのデータを取得
            your_slug_data = request.POST['hidden_data']
            print("your_slug_data:",your_slug_data)
            your_text_data = form.cleaned_data['your_text']
            saveRecord = Post.objects.get(slug=your_slug_data)
            saveRecord.body=your_text_data
            saveRecord.title=your_text_data.split('\n')[0][:25]
            # print(your_text_data.split('\n')[0][:25])
            saveRecord.save()

            # その後、適切なリダイレクトを行う
            return redirect('frontpage')  # 成功した後のページのURLに適切なものを指定
        else:
            # フォームが無効な場合の処理
            # エラーメッセージなどをフォームとともに再度表示する
            return redirect('frontpage') 
 
    if "deleteClick" in request.POST:
        print("Deleteボタンクリック")
        form = YourForm(request.POST)
        if form.is_valid():
            your_slug_data = request.POST['hidden_data']
            print("your_slug_data:",your_slug_data)
            saveRecord = Post.objects.get(slug=your_slug_data)
            saveRecord.body="DELETED"
            saveRecord.save()

            return redirect('frontpage')  # 成功した後のページのURLに適切なものを指定
        else:
            return redirect('frontpage') 

    # else:
    #     form = YourForm()

    # posts = Post.objects.all().order_by('posted_date').reverse()
    posts = Post.objects.all().exclude(body__exact="DELETED").order_by('posted_date').reverse()
    return render(request, "blog/frontpage.html",{"posts":posts})
