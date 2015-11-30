from django.contrib.syndication.views import Feed
from .models import Post


class LatestPosts(Feed):
    title = "Oficjalny Blog sieci gabinetów dentystycznych 'Ząbek'"
    link = "/feed/"
    description = "Najnowsze posty"

    def items(self):
        return Post.objects.all()[:5]
