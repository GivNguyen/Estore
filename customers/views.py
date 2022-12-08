from django.shortcuts import render, redirect
from .forms import FormDangKy
from .models import Customer

# Create your views here.
def dang_ky(request):
    form = FormDangKy()
    result = ''
    if request.POST.get('first_name'):
        form = FormDangKy(request.POST, Customer)
        if form.is_valid():
            if request.POST.get('confirm_password') == request.POST.get('password'):
                request.POST._mutable = True
                post = form.save(commit=False)
                post.first_name = form.cleaned_data['first_name']
                post.last_name = form.cleaned_data['last_name']
                post.email = form.cleaned_data['email']
                post.password = form.cleaned_data['password']
                post.confirm_password = form.cleaned_data['confirm_password']
                post.phone = form.cleaned_data['phone']
                form.save()

                result = '''
                <div class="alert alert-success" role="alert">
                    Đăng ký thành công
                </div>
                '''
            else: result = '''
                <div class="alert alert-success" role="alert">
                    Mật khẩu và xác nhận mật khẩu không đúng
                </div>
                '''
        else:
            result = '''
                <div class="alert alert-success" role="alert">
                    Dữ liệu nhập không đúng
                </div>
                '''
    return render(request, 'store/signup.html', {
        'form': form,
        'result': result,
    })

def dang_nhap(request):
    #DangNhap
    result = ""
    if request.POST.get('email'):
        email = request.POST.get('email')
        password = request.POST.get('password')

        nguoi_dung = Customer.objects.filter(email = email, password = password)
        
        if nguoi_dung.count() > 0:
            dic_nguoi_dung = nguoi_dung.values()[0]
            del(dic_nguoi_dung['password'])
            request.session['s_khachhang'] = dic_nguoi_dung
            return redirect('store:trang_chu')
            
        else: 
            result = '''
            <div class="alert alert-danger" role="alert">
                Đăng nhập thất bại. Vui lòng kiểm lại thông tin
            </div>
            '''
    return render(request, 'store/login.html', {
        'result': result,
    })
    
def dang_xuat(request):
    if 's_khachhang' in request.session:
        del request.session['s_khachhang']
    return redirect('customers:dang_nhap')

def my_account(request):
    if 's_khachhang' not in request.session:
        return redirect('customer:dang_nhap')
    return render(request, 'store/my_account.html')