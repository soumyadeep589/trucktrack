from rest_framework.views import APIView
from .models import Post


from .utils import json_error, json_success


class PostView(APIView):
    """
    Retrieve, or create a post instance.
    """

    def get(self, request):
        try:
            posts = Post.objects.values()
        except Exception as e:
            print("all post objects not found" + str(e))
            return json_error("all post objects not found")
        return json_success(list(posts))

    def post(self, request):
        data = request.data
        if not data.get("author"):
            return json_error("author is mandatory")
        if not data.get("body"):
            return json_error("body is mandatory")

        try:
            post = Post.objects.create(author=data['author'], body=data['body'])
            print("post created successfully")
        except Exception as e:
            print("Failed to create post: " + str(e))
            return json_error("Failed to create post. " + str(e), status=500)

        return json_success(
            {
                "id": post.id,
                "author": post.author,
                "body": post.body
            }
        )


class PostDetailView(APIView):

    def put(self, request, pk):
        data = request.data
        if not data.get("author"):
            return json_error("author is mandatory")
        if not data.get("body"):
            return json_error("body is mandatory")

        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            print("post not found")
            return json_error("post not found", status=404)
        except Exception as e:
            print("something went wrong: " + str(e))
            return json_error("something went wrong" + str(e), status=500)

        try:
            post.author = data["author"]
            post.body = data["body"]
            post.save()
            print("post updated successfully")
        except Post.DoesNotExist as e:
            print("post does not exist. " + str(e))
            return json_error("post does not exist. " + str(e), status=404)
        except Exception as e:
            print("Failed to update post: " + str(e))
            return json_error("Failed to update post. " + str(e), status=500)

        return json_success(
            {
                "id": post.id,
                "author": post.author,
                "body": post.body
            }
        )

    def delete(self, request, pk):

        try:
            post = Post.objects.get(id=pk)
            post.delete()
            print("post removed successfully")
        except Post.DoesNotExist:
            print("post not found")
            return json_error("post not found", status=404)
        except Exception as e:
            print("something went wrong: " + str(e))
            return json_error("something went wrong" + str(e), status=500)

        return json_success(
            {
                "message": "post removed successfully",
            }
        )