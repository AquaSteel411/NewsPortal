from django.urls import path

from .views import (
    PostsList, SearchPost, PostDetail, PostCreate, PostUpdate, PostDelete,
    CategoryList, PostCategoryList, subscribe, unsubscribe
)


urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('search', SearchPost.as_view(), name='search_post'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('category_list/', CategoryList.as_view(), name='category_list'),
    path('post_category/<int:pk>', PostCategoryList.as_view(), name='post_category'),
    path('post_category/<int:pk>/subscribe', subscribe, name='subscribe'),
    path('post_category/<int:pk>/unsubscribe', unsubscribe, name='unsubscribe'),
]