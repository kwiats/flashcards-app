def user_directory_path(instance, filename):
    """file will be uploaded to MEDIA_ROOT/user_<id>/<filename>"""
    return f"static/images/user_{instance.pk}/{filename}"
