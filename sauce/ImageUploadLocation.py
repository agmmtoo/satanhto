def user_dir(instance, filename):
    return 'user_{0}/{1}'.format(instance.owner.username, filename)