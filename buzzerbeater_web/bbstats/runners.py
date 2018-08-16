# Credit:
# http://birdhouse.org/blog/2015/03/25/django-unit-tests-against-unmanaged-databases/
# https://www.caktusgroup.com/blog/2010/09/24/simplifying-the-testing-of-unmanaged-database-models-in-django/

from django.test.runner import DiscoverRunner


class ManagedModelTestRunner(DiscoverRunner):
    """
    Test runner that automatically makes all unmanaged models in your Django
    project managed for the duration of the test run, so that one doesn't need
    to execute the SQL manually to create them.
    """

    def __init__(self, **kwargs):
        from django.apps import apps

        super(ManagedModelTestRunner, self).__init__(**kwargs)

        #for a in apps.get_apps():
        #    print("Found app %s" % (a))

        # NOTE: apps must be registered in INSTALLED_APPS in settings.py before their models appear here
        all_models = apps.get_models()
        for m in all_models:
            print("Found model %s - Managed:%s" % (m, m._meta.managed))

        self.unmanaged_models = [m for m in all_models if not m._meta.managed]

    def setup_test_environment(self, *args, **kwargs):
        for m in self.unmanaged_models:
            m._meta.managed = True
            print("Modifying model %s to be managed for testing - Managed:%s" % (m, m._meta.managed))
        super(ManagedModelTestRunner, self).setup_test_environment(*args, **kwargs)

    def teardown_test_environment(self, *args, **kwargs):
        super(ManagedModelTestRunner, self).teardown_test_environment(*args, **kwargs)
        # reset unmanaged models
        for m in self.unmanaged_models:
            m._meta.managed = False
            # print("Resetting model %s to be unmanaged - Managed:%s" % (m, m._meta.managed))