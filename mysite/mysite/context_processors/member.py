def user(request):

    user = request.user
    if user.id is not None:
        return {'userinfo': user.info}
    else:
        return {'userinfo': None}
