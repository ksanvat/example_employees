from umongo import MotorAsyncIOInstance, Document as UMongoDocument


class Instance(MotorAsyncIOInstance):
    def deinit(self):
        self._db = None


instance = Instance()


def init_instance(db):
    instance.init(db)


def deinit_instance():
    instance.deinit()
