#from blog.models import Post, Author, Tag, User, Comment


# Write a function, which takes a blog post id and returns all
# of the comments for that blog post.
def retrieve_a_posts_comments(post_id_num):
    return Post.objects.get(pk=post_id_num).comments.all()

print retrieve_a_posts_comments(1)

# Write a function, which takes a blog post id and returns the amount
# of votes for that blog post.
def fun2(blog_post_id):
    return Post.objects.get(pk=blog_post_id).user_votes.all().count()

print fun2(1)

# Write a function, which takes a user id and gets all comments by that user.
def fun3(user_id):
    return User.objects.get(pk=user_id).comment_authors.all()

print fun3(2)

# Write a function, which returns all tags for blog posts that have
# been voted on by the user with a pk of 1.
def fun4(user_id):
    return Tag.objects.filter(posts__user_votes__pk=user_id).all()

print fun4(1)

# Write a function, which returns all users that have commented
# on a blog post written by the author with the name 'Dr. Seuss'.
def fun5(user_name):
    return User.objects.filter(comment_authors__comment__author__name=user_name).all()

print fun5('Pavan Patel')


#
#
# Tag.objects.filter(posts__pk__in=post_ids).distinct().count()
#
#     return User.objects.filter(posts__in=post1).all()
