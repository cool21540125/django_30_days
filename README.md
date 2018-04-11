# 鐵人賽 - Django
- 2018/04/11(三)
[Django 鐵人賽 30天](https://ithelp.ithome.com.tw/articles/10157091)

**自學用!!**

```cmd
:: 我在 Win10, 使用 Anaconda3.6版執行~~
> python --version
Python 3.6.0 :: Anaconda 4.3.0 (64-bit)

:: 建立虛擬環境
> 

> pip install django==1.11.12

> django-admin startproject lunch

> cd lunch
```

> *全域變數* 皆為 `[A-Z]+_[A-Z0-9]+`


## Django - MTV
* Models 代表資料，通常是用來與資料庫溝通。
* Templates 代表把東西呈現給使用者的媒介。
* Views 用來處理 models，以將其呈現於 templates 中，或者處理使用者送來的資料（以 HTTP POST 等方式），並存入 models。

```cmd
:: (作者沒提到這個, DB版本控管用)
> python manage.py migrate

> python
:: 完成上述設定後, 進入python, 執行看看, 沒報錯表示資料庫設定OK
from django.db import connection
cursor = connection.cursor()
```


## 目標~
1. 使用者註冊與登入。
2. 列出與顯示店家資訊，包括名稱與菜單圖片。使用者可以自由新增、修改、刪除。
3. 選取一家店，讓每個使用者可以填入自己想吃什麼。


## 1
(先pass, django有內建好一套註冊機制)
```cmd
> python manage.py createsuperuser
```


## 2. 建立 app
- 在 Django 中，網站叫做 _project_，而組成網站的元件則是 _app_, 習慣就好...
- 在 Django 中，通常習慣把 app 取名為它主要功能的 model 的複數形

```cmd
:: 建立 
> python manage.py startapp stores
```


> `Server 收到一個 HTTP request 時，會確認 request 的 URI 應該對應到哪個 view（如果對應不到，直接回傳 404 Not Found），並把 request 交給它。View 要負責處理這個 request，並回傳一個 HTTP response.` 這個過程, 根本就是一個 function 在做的事情!! 

```py
# 這邊是我瞎掰的, 但概念就是這樣
def getRequest():
    response = view(request, data, headers, URL, ...)   # django.http.HttpResponse 物件
    return response
```

#### 改底下幾個個地方
* /lunch/settings/base.py
    * INSTALLED_APPS 內, 增加 `stores`
* /lunch/urls.py
    * from django.conf.urls import url, include
    * url(r'^stores/', include('stores.urls')),
* /lunch/stores/urls.py
    * 增加下面這包

```py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
]
```

> `127.0.0.1:8000/stores/` 就有東西了!!



