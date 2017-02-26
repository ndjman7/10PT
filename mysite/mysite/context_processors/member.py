def user(request):

    user = request.user
    if user is not None:
        return {'userinfo': user.info}
    else:
        return {'userinfo': None}
