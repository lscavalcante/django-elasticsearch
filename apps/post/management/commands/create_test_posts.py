# create_test_posts.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from faker import Faker

from apps.comment.models import Comment
from apps.post.models import Post


class Command(BaseCommand):
    help = 'Create 100000 test posts with comments'

    def handle(self, *args, **kwargs):
        fake = Faker()
        author = User.objects.first()  # Assumindo que você tem pelo menos um usuário no banco de dados
        posts = []
        comments = []

        # Criar 1000 posts
        for _ in range(100000):
            post = Post(
                title=fake.sentence(),
                body=fake.paragraph(),
                author=author,
                published_date=fake.date_time_this_year(),
                created_at=fake.date_time_this_year(),
                updated_at=fake.date_time_this_year(),
            )
            posts.append(post)

        Post.objects.bulk_create(posts)

        # Recuperar os posts criados para adicionar comentários
        created_posts = Post.objects.all().order_by('-id')[:1000]

        for post in created_posts:
            for _ in range(fake.random_int(min=1, max=10)):
                comment = Comment(
                    post=post,
                    author=author,
                    text=fake.paragraph(),
                    created_date=fake.date_time_this_year(),
                    updated_at=fake.date_time_this_year(),
                )
                comments.append(comment)

        Comment.objects.bulk_create(comments)

        self.stdout.write(self.style.SUCCESS('Successfully created 1000 test posts with comments'))
