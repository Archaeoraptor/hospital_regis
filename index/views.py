
# from django.contrib.auth.decorators import login_required
#
# # @login_required(redirect_field_name='login')
# @login_required(login_url='/user/login.html')
# def index(request):
# 	username = request.user.username
# 	return render(request, 'index.html', locals())

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from hos.models import *
from haystack.views import SearchView
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required, permission_required

# def index(request):
# 	return redirect('index.html')
#


# 使用login_required和permission_required分别对用户登录验证和用户权限验证
# @login_required(login_url='/user/login.html')
def index(request):

	return render(request, 'index.html', context=locals())


# 使用函数has_perm实现装饰器permission_required功能
# @login_required(login_url='/user/login.html')
# @permission_required(perm='index.visit_Product', login_url='/user/login.html')
# def index(request):
# 	user = request.user
# 	if user.has_perm('index.visit_Product'):
# 		return render(request, 'index.html', locals())
# 	else:
# 		return redirect('/')
		# return redirect('/user/login.html')
def gotoadmin(request):

	return redirect('/admin')


# 视图以通用视图实现
class MySearchView(SearchView):
    # 模版文件
    template = 'search.html'
    # 重写响应方式，如果请求参数q为空，返回模型(Doctor)的全部数据，否则根据参数q搜索相关数据
    def create_response(self):
        if not self.request.GET.get('q', ''):
            show_all = True
            doctor = Doctor.objects.all()
            paginator = Paginator(doctor, settings.HAYSTACK_SEARCH_RESULTS_PER_PAGE)
            try:
                page = paginator.page(int(self.request.GET.get('page', 1)))
            except PageNotAnInteger:
                # 如果参数page的数据类型不是整型，则返回第一页数据
                page = paginator.page(1)
            except EmptyPage:
                # 用户访问的页数大于实际页数，则返回最后一页的数据
                page = paginator.page(paginator.num_pages)
            return render(self.request, self.template, locals())
        else:
            show_all = False
            qs = super(MySearchView, self).create_response()
            return qs


class MySearchView2(SearchView):
    # 模版文件
    template = 'search2.html'
    # 重写响应方式，如果请求参数q为空，返回模型Office的全部数据，否则根据参数q搜索相关数据
    def create_response(self):
        if not self.request.GET.get('q', ''):
            show_all = True
            office = Office.objects.all()
            paginator = Paginator(office, settings.HAYSTACK_SEARCH_RESULTS_PER_PAGE)
            try:
                page = paginator.page(int(self.request.GET.get('page', 1)))
            except PageNotAnInteger:
                # 如果参数page的数据类型不是整型，则返回第一页数据
                page = paginator.page(1)
            except EmptyPage:
                # 用户访问的页数大于实际页数，则返回最后一页的数据
                page = paginator.page(paginator.num_pages)
            return render(self.request, self.template, locals())
        else:
            show_all = False
            qs = super(MySearchView2, self).create_response()
            return qs


# 404页面
def page_not_found(request):

    return render(request, '404.html', status=404)


def page_error(request):

    return render(request, '500.html', status=500)


def HelpView(request):

    return render(request, 'help.html', status=200)
