def user_dir(instance, filename):
    return 'user_{0}/{1}'.format(instance.owner.username, filename)

def channel_dir(instance, filename):
    return 'channel_{0}/{1}'.format(instance.slug, filename)