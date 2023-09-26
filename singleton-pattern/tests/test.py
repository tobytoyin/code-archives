from src import SingletonContext


def test_same_id_retrieve_same_instance():
    instance1 = SingletonContext("instance-1").get_instance()
    instance2 = SingletonContext("instance-1").get_instance()

    assert instance1 == instance2  # singleton objects
    assert instance1.name == instance2.name  # name are the same


def test_new_id_retrieve_same_instance():
    instance1 = SingletonContext("instance-1").get_instance()
    instance3 = SingletonContext("instance-3").get_instance()

    assert instance1 == instance3  # single objects even when name is different
    assert instance1.name == instance3.name  # defined name won't get changed
